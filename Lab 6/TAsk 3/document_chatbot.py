import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

SelectedConfiguration = None


def configure(selected_configuration):
    """Receive the selected development configuration from the evaluator."""
    global SelectedConfiguration
    SelectedConfiguration = selected_configuration


def search_selected(query_text, top_k=3):
    """Return the top-k chunks from the configured retrieval system."""
    if SelectedConfiguration is None:
        raise RuntimeError("Call configure() with the selected configuration first.")
    if not query_text.strip():
        return []

    Model = SelectedConfiguration["model"]
    SelectedRun = SelectedConfiguration["run"]
    Method = SelectedConfiguration["method"]
    Chunks = SelectedRun["chunks"]
    ChunkVectors = SelectedRun["chunk_vectors"]
    Vectorizer = SelectedRun["vectorizer"]

    if Method == "tfidf":
        QueryVector = Vectorizer.transform([query_text])
        Scores = cosine_similarity(QueryVector, ChunkVectors)[0]
    else:
        QueryVector = Model.encode(
            [query_text],
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False
        )[0]
        Scores = ChunkVectors @ QueryVector

    TopIndices = np.argsort(-Scores, kind="stable")[:top_k]
    return [(Chunks[Index], float(Scores[Index])) for Index in TopIndices]


def document_chatbot():
    """Run the evidence-confirmation chatbot using the configured model."""
    if SelectedConfiguration is None:
        raise RuntimeError("Call configure() with the selected configuration first.")

    Strategy = SelectedConfiguration["strategy"]
    Method = SelectedConfiguration["method"]
    Threshold = SelectedConfiguration["run"]["threshold"]

    print("\n" + "=" * 72)
    print("UNIVERSITY DOCUMENT EVIDENCE ASSISTANT")
    print("Selected:", Strategy, "|", Method)
    print("Type 'exit' to stop.")
    print("=" * 72)

    while True:
        try:
            Question = input("\nYour question: ").strip()
        except EOFError:
            print("\nNo interactive input is available. Chatbot stopped.")
            break

        if Question.lower() in ["exit", "quit"]:
            print("Chatbot stopped.")
            break
        if not Question:
            print("Please enter a question.")
            continue

        Hits = search_selected(Question, top_k=3)
        if not Hits:
            print("No candidate chunks were found.")
            continue

        print("\nTop candidate results:")
        for Rank, (Chunk, Score) in enumerate(Hits, 1):
            print(
                Rank, "|", Chunk["id"],
                "| Score:", round(Score, 4),
                "| Source:", Chunk["doc"],
                "| Offsets:", f'{Chunk["start"]}:{Chunk["end"]}'
            )

        BestChunk, BestScore = Hits[0]
        if BestScore < Threshold:
            print("\nNot enough evidence was found. No answer will be asserted.")
            print("The nearest-neighbour search still returns candidates even when the corpus has no answer.")
            continue

        SourceNames = {Chunk["doc"] for Chunk, Score in Hits}
        if "contractor_policy" in SourceNames and "remote_work_memo" in SourceNames:
            print("\nWarning: Retrieved sources conflict.")
            print("The chatbot cannot determine which source has higher authority.")
            print("Confirm the disagreement with procurement or the policy owner.")

        try:
            Confirm = input("\nDisplay the retrieved source evidence? (yes/no): ").strip().lower()
        except EOFError:
            print("\nNo confirmation input is available. Evidence was not displayed.")
            break

        if Confirm in ["yes", "y"]:
            for Rank, (Chunk, Score) in enumerate(Hits, 1):
                print("\nEvidence", Rank)
                print("Document:", Chunk["doc"])
                print("Chunk ID:", Chunk["id"])
                print("Character offsets:", Chunk["start"], "to", Chunk["end"])
                print("Score:", round(Score, 4))
                print("Text:", Chunk["text"])
        else:
            print("Evidence was not displayed. No answer was asserted.")


if __name__ == "__main__":
    from task3_retrieval import Main

    configure(Main())
    document_chatbot()

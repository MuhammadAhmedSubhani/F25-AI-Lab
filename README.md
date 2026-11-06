# F25 AI Lab

This repository contains assignment documents and Python examples for six AI
lab modules. Tasks are provided as Word documents, Python scripts, and Jupyter
notebooks.

## Repository Contents

| Lab | Tasks |
| --- | --- |
| [Lab 1](./Lab%201/) | [Task 1](./Lab%201/Task%201/Task%20-%201.docx), [Task 2](./Lab%201/Task%202/Task%20-%202.docx) and [Python example](./Lab%201/Task%202/Task%20-%202.py), [Task 3](./Lab%201/Task%203/Lab%20-%203.docx) |
| [Lab 2](./Lab%202/) | [Task 1](./Lab%202/TASK%201/Lab%20-%201.docx), [Task 2](./Lab%202/Task%202/Lab%20-%202.docx), [Task 3](./Lab%202/Task%203/Task%20-%203.docx) and [Python example](./Lab%202/Task%203/Temp_controller.py) |
| [Lab 3](./Lab%203/) | [Task 1](./Lab%203/Task%201/Lab%20-%201.docx) and [Python example](./Lab%203/Task%201/TASK%201.py), [Task 2](./Lab%203/Task%202/Lab%20-%202.docx), [Task 3](./Lab%203/Task%203/Lab%20-%203.docx) |
| [Lab 4](./Lab%204/) | [Task 1](./Lab%204/Task%201/Lab%20-%201.docx), [Task 2](./Lab%204/TASK%202/Lab%20-%202.docx), [Task 3](./Lab%204/Task%203/Lab%20-%203.docx) |
| [Lab 5](./Lab%205/) | [Task 1](./Lab%205/TASK%201/Lab%20-%201.docx), [Task 2](./Lab%205/tASK%202/Lab%20-%202.docx), [Task 3](./Lab%205/Task%203/Re%20Order%20Branches.py) |
| [Lab 6](./Lab%206/) | [Task 1 notebook](./Lab%206/Task%201/Task1.ipynb) and [assignment](./Lab%206/Task%201/Lab%20-%201.docx), [Task 2 notebook](./Lab%206/Task%202/Task_2.ipynb) and [assignment](./Lab%206/Task%202/Lab%20-%202.docx), [Task 3 retrieval](./Lab%206/TAsk%203/task3_retrieval.py) and [chatbot](./Lab%206/TAsk%203/document_chatbot.py) |

## Python Examples

- [Lab 1, Task 2](./Lab%201/Task%202/Task%20-%202.py): checks a student's
  pass status using marks, document completion, attendance, and assignment
  submission.
- [Lab 2, Task 3](./Lab%202/Task%203/Temp_controller.py): selects a
  temperature-control mode based on temperature and occupancy.
- [Lab 3, Task 1](./Lab%203/Task%201/TASK%201.py): demonstrates breadth-first
  search (BFS) and depth-first search (DFS) on a directed graph.
- [Lab 5, Task 2 — Minimax](./Lab%205/tASK%202/MiniMax.py) and
  [Alpha-Beta Pruning](./Lab%205/tASK%202/Alpha%20Beta%20Pruning.py):
  evaluate a binary game tree.
- [Lab 5, Task 3](./Lab%205/Task%203/Re%20Order%20Branches.py): compares
  minimax and alpha-beta pruning, including the effect of reordering branches.
- [Lab 6, Task 1](./Lab%206/Task%201/Task1.ipynb): compares whitespace and
  regular-expression tokenization.
- [Lab 6, Task 2](./Lab%206/Task%202/Task_2.ipynb): explores document retrieval
  with a synthetic policy corpus.
- [Lab 6, Task 3](./Lab%206/TAsk%203/task3_retrieval.py): evaluates document
  chunking and retrieval configurations, reports retrieval metrics, and writes
  a `task3_retrieval_log.csv` results file. The optional
  [document chatbot](./Lab%206/TAsk%203/document_chatbot.py) presents retrieved
  evidence for interactive questions.

## Requirements

- Python 3 for the scripts and notebooks.
- The standalone examples in Labs 1–5 use only the Python standard library.
- Lab 6, Task 2 and Task 3 require NumPy, scikit-learn, and
  sentence-transformers. The Lab 6, Task 2 notebook includes an installation
  cell for these packages.
- Jupyter Notebook or JupyterLab is needed to run the `.ipynb` files.
- Microsoft Word or a compatible document viewer is needed to open the `.docx`
  assignment documents.

## Running the Python Examples

Run commands from the repository root. For example:

```bash
python "Lab 1/Task 2/Task - 2.py"
python "Lab 2/Task 3/Temp_controller.py"
python "Lab 3/Task 1/TASK 1.py"
python "Lab 5/tASK 2/MiniMax.py"
python "Lab 5/tASK 2/Alpha Beta Pruning.py"
python "Lab 5/Task 3/Re Order Branches.py"
```

To run Lab 6, Task 3, first install its third-party dependencies if needed:

```bash
python -m pip install numpy scikit-learn sentence-transformers
```

Then run the retrieval evaluation, or add `--chat` to start the interactive
evidence assistant after evaluation:

```bash
python "Lab 6/TAsk 3/task3_retrieval.py"
python "Lab 6/TAsk 3/task3_retrieval.py" --chat
```

Open the Lab 6 notebooks in Jupyter and run their cells in order. The examples
use built-in sample data and do not require command-line arguments.

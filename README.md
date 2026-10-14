# F25 AI Lab

Coursework repository for the Fall 2025 AI laboratory. Labs are kept in
separate folders so that code, reports, and supporting material stay organized.

> **Submission reminder:** Push your completed work to GitHub, then submit both
> the repository URL and the final commit identifier through the course
> submission channel. Confirm that your instructor can access the repository.

## Repository contents

| Lab | Contents |
| --- | --- |
| [Lab 1](./Lab%201/) | Task documents and the available Python implementation |
| [Lab 2](./Lab%202/) | Task documents and a temperature-controller Python program |
| [Lab 3](./Lab%203/) | Task documents and a breadth-first/depth-first search program |

### Lab 1 file inventory

| File | Purpose |
| --- | --- |
| [`Task - 2.py`](./Lab%201/Task%202/Task%20-%202.py) | Python implementation of the Lab 1 Task 2 pass/fail rules, with built-in test cases |
| [`Task - 2.docx`](./Lab%201/Task%202/Task%20-%202.docx) | Task 2 document |
| [`Task - 1.docx`](./Lab%201/Task%201/Task%20-%201.docx) | Task 1 document |
| [`Lab - 3.docx`](./Lab%201/Task%203/Lab%20-%203.docx) | Task 3 document |

**Submission completeness:** The current Lab 1 folder does not yet contain
separate, clearly named compare and rules source files (or equivalent source
code for both exercises), a separate input-data file, or saved console output /
trace files. The Task 2 test inputs are currently embedded in its Python file.
Add the applicable source files, input data, and captured outputs before
submitting if they are required for your Lab 1 work.

## Setup

The available Python programs use only the Python standard library; no
third-party packages are required. Install Python 3 and verify it is available
from your terminal:

```text
python --version
```

On Windows, if `python` is not recognized, try:

```text
py --version
```

## Run the available Lab 1 program

From the repository root, run:

```text
python "Lab 1/Task 2/Task - 2.py"
```

On Windows, you can use the Python launcher instead:

```text
py "Lab 1/Task 2/Task - 2.py"
```

The script runs its built-in test cases and prints each case's input, expected
and actual result, and the rule explaining the outcome. To keep a copy of the
console output, redirect it to a text file:

```text
python "Lab 1/Task 2/Task - 2.py" > "Lab 1/Task 2/output.txt"
```

## Lab 1 submission checklist

- [ ] Include the source code for each Lab 1 exercise, such as
      `lab1_compare.py` and `lab1_rules.py`, or clearly named equivalents.
- [ ] Include any input data needed to run the programs. Keep it as a separate
      file when the exercise provides external data; otherwise document that
      the test data is built into the source.
- [ ] Include this README with setup and run commands.
- [ ] Capture and include program outputs or trace files.
- [ ] Push the finished files to GitHub and verify the instructor has access.
- [ ] Submit the repository URL and final commit identifier through the course
      submission channel.

## Other lab programs

Run these from the repository root:

```text
python "Lab 2/Task 3/Temp_controller.py"
python "Lab 3/Task 1/TASK 1.py"
```

The Lab 2 program exercises a temperature controller and the Lab 3 program
prints breadth-first and depth-first search paths. The remaining task documents
are stored with their respective lab folders.

# AI Search Algorithms Lab

A beginner-friendly Python project for exploring intelligent agents,
state-space representation, and uninformed search algorithms. This
repository documents the graph-search exercises and the 8-puzzle problem
covered in the lab.

## Contents

-   [Project Overview](#project-overview)
-   [Topics Covered](#topics-covered)
-   [Graph Used in the Search
    Exercises](#graph-used-in-the-search-exercises)
-   [Algorithms Implemented](#algorithms-implemented)
-   [Weighted Graph and UCS
    Comparison](#weighted-graph-and-ucs-comparison)
-   [Requirements](#requirements)
-   [How to Run](#how-to-run)
-   [Important Concepts](#important-concepts)

## Project Overview

The goal of this lab is to understand how search algorithms explore a
state space, how they represent paths, and how their strategies affect
the result. The examples use a small directed graph so that search order
and path costs can be checked manually.

## Topics Covered

-   Intelligent agents and agent types
-   State-space search and representation
-   Initial state, actions, transition model, goal state, and path cost
-   Uninformed search:
    -   Breadth-First Search (BFS)
    -   Depth-First Search (DFS)
    -   Uniform-Cost Search (UCS)
    -   Depth-Limited Search (DLS)
    -   Iterative Deepening Depth-First Search (IDDFS)
-   Informed search concepts
-   The 8-puzzle problem

## Graph Used in the Search Exercises

The original directed graph uses `A` as the start node and `G` as the
goal:

``` text
        A
       / \
      B   C
     / \   \
    D   E   F
         \
          G
```

Original directed edges:

-   `A -> B`
-   `A -> C`
-   `B -> D`
-   `B -> E`
-   `C -> F`
-   `E -> G`

The original graph is unweighted for the BFS, DFS, DLS, and IDDFS
exercises. The root is counted at depth `0`.

### BFS and DFS

On the original graph, both implementations return the path:

`A -> B -> E -> G`

The code prints the path. The visit or processing order depends on the
implementation and the order in which neighbors are explored.

### DLS and IDDFS

The file `dls_iddfs.py` implements Depth-Limited Search and Iterative
Deepening DFS. It uses a path-local cycle check and distinguishes three
outcomes:

-   **FOUND** --- the goal is found.
-   **CUTOFF** --- the depth limit prevents the search from exploring
    further.
-   **FAILURE** --- the search finishes without finding the goal and
    without a depth cutoff.

Expected DLS results:

    Depth limit Status   Path
  ------------- -------- --------------------
              1 CUTOFF   None
              2 CUTOFF   None
              3 FOUND    `A -> B -> E -> G`
              4 FOUND    `A -> B -> E -> G`

Expected IDDFS results, where each run starts again at limit `0` and
stops as soon as it finds the goal:

    Maximum depth Status   Limits attempted
  --------------- -------- ------------------
                1 CUTOFF   `0, 1`
                2 CUTOFF   `0, 1, 2`
                3 FOUND    `0, 1, 2, 3`
                4 FOUND    `0, 1, 2, 3`

The goal is at depth `3`, which is why maximum depths below `3` cannot
find it. IDDFS repeats work because it runs DLS from the root for each
increasing depth limit.

## Algorithms Implemented

  -----------------------------------------------------------------------
  Algorithm               Main data structure or  Main objective
                          strategy                
  ----------------------- ----------------------- -----------------------
  BFS                     FIFO queue              Find a path with the
                                                  fewest edges in an
                                                  unweighted graph

  DFS                     Stack / depth-first     Explore one branch
                          exploration             deeply before
                                                  backtracking

  DLS                     DFS with a depth limit  Prevent exploration
                                                  beyond a specified
                                                  depth

  IDDFS                   Repeated DLS with       Find a shallow solution
                          increasing limits       while limiting memory
                                                  use

  UCS                     Priority queue ordered  Find a minimum-cost
                          by cumulative path cost path when edge costs
                                                  are non-negative
  -----------------------------------------------------------------------

## Weighted Graph and UCS Comparison

The file `ucs_bfs_weighted.py` defines an illustrative weighted version
of the graph. It retains all original edges and adds one explicitly
documented corridor: `C -> G` with cost `10`.

Every edge weight in that version is:

  Edge         Cost Note
  ---------- ------ -------------------------------
  `A -> B`        1 Original edge
  `A -> C`        2 Original edge
  `B -> D`        2 Original edge
  `B -> E`        5 Original edge
  `C -> F`        2 Original edge
  `E -> G`        2 Original edge
  `C -> G`       10 Added corridor for comparison

These are illustrative costs assigned for the exercise, not weights from
the original unweighted graph or from an external specification.

Expected results for this weighted topology:

  Algorithm   Returned path          Number of edges   Total cost
  ----------- -------------------- ----------------- ------------
  BFS         `A -> C -> G`                        2           12
  UCS         `A -> B -> E -> G`                   3            8

Independent cost checks:

-   BFS: `A -> C -> G` = `2 + 10 = 12`
-   UCS: `A -> B -> E -> G` = `1 + 5 + 2 = 8`

BFS minimizes the number of edges, not their weights. UCS prioritizes
cumulative path cost, so the three-edge route is cheaper than the
two-edge route in this example.

Expected processing orders for the stated neighbor order and UCS
tie-breaking implementation:

-   **BFS:** `A, B, C, D, E, F, G`
-   **UCS:** `A, B, C, D, F, E, G`

## Requirements

-   Python 3.8 or newer
-   No third-party packages are required for the graph-search examples;
    the code uses Python's standard library.

## How to Run

Open a terminal in the project directory and run the relevant script:

``` bash
python dls_iddfs.py
python ucs_bfs_weighted.py
```

If your BFS/DFS code is stored in a separate file, run that file using
the same pattern:

``` bash
python your_bfs_dfs_filename.py
```

Replace the example filename with the actual filename in your project.

## Important Concepts

-   **Path vs. processing order:** A returned path shows the route from
    start to goal. Processing order shows the sequence of nodes removed
    from the search frontier and examined.
-   **Depth vs. cost:** Depth counts edges from the root; path cost adds
    the weights of the edges.
-   **BFS vs. UCS:** BFS is appropriate for minimum-edge paths in an
    unweighted graph. UCS is appropriate for minimum-cost paths with
    non-negative edge costs.
-   **DLS vs. IDDFS:** DLS performs one depth-limited search. IDDFS
    repeats DLS with increasing limits, so nodes near the root are
    explored more than once.
-   **Graph consistency:** The weighted exercise uses the same original
    edges plus the one documented `C -> G` corridor. The original
    unweighted graph remains unchanged for the other exercises.

## Notes

This README records the graph definitions, expected outputs, and
assumptions used in the lab exercises. If your instructor's handout
specifies different edge weights or a different controlled extension,
use the handout's values and update the weighted-graph section
accordingly.

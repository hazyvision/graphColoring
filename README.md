graphColoring
=============

Explores the tradeoffs between two algorithms to solve the graph coloring problem
   ..* dfs-based greedy algorithm --->Tradeoffs: Colors used is beyond the chromatic index
   ..* backtracking method----------->Tradeoffs: Nodes generated in the state space tree is excessive
                                                resulting in slower calculations
Input:  The order of a graph to be randomly created and tested.
Output: Returns the number of colors used for the greedy algorithm.
        Also, returns the amount of nodes created from the backtracking algorithm.

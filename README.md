# Sudoku-Solver-Using-Simulated-Annealing

This repository contains a Python script for solving Sudoku puzzles using simulated annealing algorithm. Simulated annealing is a probabilistic optimization algorithm that is inspired by the annealing process in metallurgy. The algorithm works by iteratively changing a solution to a problem to minimize a cost function. It is particularly useful for solving combinatorial optimization problems such as Sudoku puzzles.

### Customizing the Puzzle
You can customize the Sudoku puzzle to be solved by modifying the `board` variable in the `sudoku_solver.py` file. You can input your own Sudoku puzzle by providing a 9x9 grid where empty cells are represented by `0`. Ensure that the puzzle is valid (i.e., it follows Sudoku rules) for accurate solving.

## Algorithm Overview
The solver uses simulated annealing algorithm to solve the Sudoku puzzle. Here's a brief overview of how the algorithm works:
1. **Initialization**: The puzzle is initialized with some initial state.
2. **Cost Calculation**: The cost of the current state is calculated based on the number of repetitions in rows, columns, and sub-grids.
3. **Iterative Improvement**: The solver iteratively generates new states by swapping two random empty cells and calculates the cost of the new state.
4. **Acceptance Probability**: If the new state has a lower cost, it is always accepted. If the new state has a higher cost, it may still be accepted with a certain probability calculated using the simulated annealing formula.
5. **Temperature Cooling**: The temperature parameter decreases over time, controlling the probability of accepting worse solutions. This allows the algorithm to explore the solution space more effectively.

## Examples
The repository includes examples of Sudoku puzzles of varying difficulties. You can uncomment one of the example boards in the `sudoku_solver.py` file to solve it.

Happy Sudoku solving! 🧩

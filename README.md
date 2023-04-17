# Postman's Cipher Problem Solver


This repository contains a Python implementation of a backtracking algorithm to solve the Postman's Cipher Problem (PCP), a word game that involves deciphering a message that has been encoded using homophonic substitution.

## How to Use

To use this solver, simply clone the repository and run the `pcp_solver.py` file. Make sure you have Python installed on your system. The implementation is compatible with Python 3.

```bash
git clone https://github.com/[your-username]/pcp_solver.git
cd pcp_solver
python pcp_solver.py
```
The solver will then prompt you to enter a list of letter pairs separated by commas. For example:
    
```bash
Enter pairs of letters (e.g. a,b,c,d):
a,b,c,d
```
The solver will then search for a solution to the PCP with the provided letter pairs. If a solution is found, it will be printed to the screen. Otherwise, a message indicating that the PCP is not solvable will be printed.

Adrian Sanz, for the subjet of Complexity and Computation Models of the Master in Computer Science of the University of Lleida.
2023
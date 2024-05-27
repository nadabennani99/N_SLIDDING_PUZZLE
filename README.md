# n_sliding_puzzle
Implementation of a solver of the n_sliding puzzle using different search algorithms

## The proposed search algorithms :
This repo proposes the following searh algorithms in solving the n sliding puzzle, for every n configuration :

### Informed search:
- A*
- Bidirectional A*
### Uninformed search :
- UCS
- BFS
- Bidirectional BFS

## Usage :

Please run main.py to launch the main program. You can either input a puzzle (manually or from a file), generate a random puzzle, and then choose
between comparing algorithms or simply finding a solution using a custom algorithm.
A collection of 3x3, 4x4 and 5x5 puzzles can be found in the /test_puzzles folder.
If you want to input a custo file, please make sure that it follows the formatting : 
- the first line should contains a # followed by the n dimension of the puzzle.
- Then input the different numbers in the tiles separated by commas.




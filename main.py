from Astar import *
from bisearch import *
from puzzle import *
from bi_search_astar import *
from BFS import *
import time
import numpy as np




def compare_heuristics(algo,init_state,goal_state):
    print(init_state)
    print(goal_state)
    if algo =="A*":
        solver_m = Astar(init_state,goal_state,"manhattan")
        solver_h = Astar(init_state,goal_state,"misplaced_tiles")
    else:
        solver_m = BiSearchA(init_state,goal_state,"manhattan")
        solver_h = BiSearchA(init_state,goal_state,"misplaced_tiles")
    start = time.time()
    solver_m.solve()
    end = time.time()
    print("Elapsed time for the Manhattan distance with the " + algo + "algorithm" + str(end - start) + "seconds")
    start = time.time()
    solver_h.solve()
    end = time.time()
    print("Elapsed time for the Hamming distance with the " + algo + "algorithm" + str(end - start) + "seconds")


def main():
    print("Do you want to generate a random puzzle (1) or input a puzzle (2)")
    i = int(input())
    if i == 1:
        print("How many tiles (n*n) ?")
        nb_tiles = int(input())
        print("How many shuffles ?")
        nb_shuffles = int(input())
        puzzle = generate_random(nb_tiles,nb_shuffles)
        init_state = puzzle.current_state
        goal_state = puzzle.goal_state
        print("Generated puzzle :")
        puzzle.show_game()
    else:
        print("Do you want to write your puzzle on the terminal (1) or input a puzzle from a file (2)")
        c = int(input())
        if c==1:
            print("How many tiles (n*n) ?")
            nb_tiles = int(input())
            print("For each row of the puzzle, input the numbers separated by spaces then press enter")
            init_state = []
            for i in range(nb_tiles):
                row = input()
                row = row.split()
                init_state.append([])
                for j in range(nb_tiles):
                    init_state[i].append(int(row[j]))
            init_state = np.array(init_state)
            goal_state = get_goal_state(nb_tiles)

        else:
            print("please input the path of the file")
            filename = input()
            init_state,nb_tiles = get_from_txt(filename)
            goal_state = get_goal_state(nb_tiles)

        print("Puzzle to be solved :")
        puz = Puzzle(init_state,goal_state)
        puz.show_game()
        print("Checking if this puzzle is solvable...")
        if not puz.is_solvable():
            print("This puzzle is not solvable")
            return 0
        else:
            print("This puzzle is solvable ! Moving to the next choices...")
    print("Compare algorithms (1) or find a solution (2) ?")
    i = int(input())
    if i ==2:
        print("What algorithm do you want to use ? 1 - A* 2 - Bidirectional search BFS 3- Bidirectional search A* 4- BFS 5- UCS")
        i = int(input())
        if i == 1:
            print("Which heuristic ? manhattan / misplaced_tiles/ 0 {for no heuristic -> UCS}")
            heuristic = input()
            solver = Astar(init_state,goal_state,heuristic)
        elif i == 2:
            solver = BiSearch(init_state,goal_state)
            maxx=solver.solve()
            print("space complexity ; max frontier size for BiSearch BFS for frontier1:",maxx[0])
            print("space complexity ; max frontier size for BiSearch BFS for frontier2:",maxx[1])
        elif i ==3:
            print("Which heuristic ? manhattan / misplaced_tiles/ 0 {for no heuristic -> UCS}")
            heuristic = input()
            solver = BiSearchA(init_state,goal_state,heuristic)
        elif i == 4:
            solver = BFS(init_state,goal_state)
        else: #UCS
            solver = Astar(init_state,goal_state,None)
        start = time.time()
        solver.solve(True)
        end = time.time()
        print("elapsed time : ",end - start)
    else:
        print("Do you want to compare heuristics (1), or algorithms (2)?")
        i = int(input())
        if i == 1:
            print("A* (1) or Bidirectional search A* (2) ? ")
            i = int(input())
            if i == 1:
                compare_heuristics("A*",init_state,goal_state)
            else:
                compare_heuristics("BiA",init_state,goal_state)
        else:
            print("Which heuristic ? manhattan / misplaced_tiles/ 0 {for no heuristic -> UCS}")
            heuristic = input()
            solver_1 = Astar(init_state,goal_state,heuristic)
            start = time.time()
            max_queue,path=solver_1.solve()
            end = time.time()
            print("elapsed time for A*:",end-start)
            print("space complexity ; max frontier size for A*:",max_queue)
            solver_2 = BiSearchA(init_state,goal_state,heuristic)
            start = time.time()
            max_queue=solver_2.solve()
            end = time.time()
            print("elapsed time for BiSearch A*:",end-start)
            print("space complexity ; max frontier size for BiSearch A* for frontier1:",max_queue[0])
            print("space complexity ; max frontier size for BiSearch A* for frontier2:",max_queue[1])
            solver_2 = BiSearch(init_state,goal_state)
            start = time.time()
            max_queue=solver_2.solve()
            end = time.time()
            print("elapsed time for BiSearch BFS:",end-start)
            print("space complexity ; max frontier size for BiSearch BFS for frontier1:",max_queue[0])
            print("space complexity ; max frontier size for BiSearch BFS for frontier2:",max_queue[1])
            solver_1 = Astar(init_state,goal_state,None)
            start = time.time()
            max_queue,path=solver_1.solve()
            end = time.time()
            print("elapsed time for UCS:",end-start)
            print("space complexity ; max frontier size for A*:",max_queue)
            solver_2 = BFS(init_state,goal_state)
            start = time.time()
            max_queue,path=solver_2.solve()
            end = time.time()
            print("elapsed time for BFS:",end-start)
            print("space complexity ; max frontier size for BFS:",max_queue)


main()
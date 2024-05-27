import math
from operator import length_hint 
from colorama import Fore, Back, Style
import numpy as np
import copy
import random


class Puzzle():
    def __init__(self,initial_state,goal_state):
        #Current configuration
        self.current_state = initial_state
        #Goal configuration
        self.goal_state = goal_state
        #Dimension of the puzzle
        self.dim = initial_state.shape[0]
        for i in range(self.dim):
            for j in range(self.dim):
                if self.current_state[i][j]==0:
                    #Dimension of the empty tile
                    self.empty_tile = [i,j]
                    break
    
    #Comparing two puzzles
    def __eq__(self,puzzle):
        return np.array_equal(self.current_state,puzzle.current_state)
                
    #Checking if a puzzle reached its goal state
    def is_goal_state(self):
        return np.array_equal(self.current_state,self.goal_state)
    #Converting numpy arrays to strings
    def __str__(self):
        return str(self.current_state)

    #Hashing the puzzles to put them in the closed set
    def __hash__(self):
        return hash(tuple(map(tuple,(self.current_state))))
    
    #Printing the puzzle in the terminal
    def show_game(self):
        print("Current state of the game : \n")
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[i])):
                if self.current_state[i][j]:
                    print("[" + str(self.current_state[i][j]) + "]",end ="")
                else:
                    print("[ ]",end="")
                print(",",end="")
            print("\n")
    
    def game_as_str(self):
        str = "Current state of the game: \n"
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[i])):
                if self.current_state[i][j]:
                    str += ("[" + str(self.current_state[i][j]) + "]")
                else:
                    str += ("[ ]")
                str += (",")
            str += ("\n")

    #Writing the puzzle in a text file
    def put_txt(self,filename):
        file = open(filename,'w')
        file.write("# " + str(self.dim) + "\n")
        st = ""
        for i in range(self.dim):
            for j in range(self.dim):
                st += str(self.current_state[i][j])
                st += ","
            st += "\n"
        file.write(st)



    #Checking if a puzzle is solvable. Please check the report for more details
    def is_solvable(self):
        flat_list = [elem for sublist in self.current_state for elem in sublist ]
        inv_nb = 0
        for i in range(len(flat_list)):
            temp = flat_list[i]
            for j in range(i,len(flat_list)):
                if flat_list[j] < temp and flat_list[j] != 0:
                    inv_nb += 1
        # If the dim is odd
        #We need an even number of inversions
        if self.dim %2 != 0:
            if inv_nb % 2 == 0:
                return True
            else:
                return False
        else: # If the dim is even, then inv_nb + row index of the empty tile need to be odd

            pos_from_bottom = self.dim - self.empty_tile[0]
            print("inv nb",inv_nb)
            print("pos",pos_from_bottom)
            if inv_nb % 2 == 0 and pos_from_bottom % 2 != 0:
                return True
            elif inv_nb %2 != 0 and pos_from_bottom %2 == 0:
                return True
            return False

    
    #Available actions given the current configuration
    def available_actions(self):
        x,y = self.empty_tile
        available_actions = []
        #Checking if we are in the corners
        #Up
        up,down,left,right = False,False,False,False
        if x == 0:
            up = True
        if x == self.dim -1:
            down = True
        if y == self.dim -1:
            right = True
        if y == 0:
            left = True
        if not up:
            #Move empty tile up
            available_actions.append([x-1,y])
        if not down:
            #Move empty tile down
            available_actions.append([x+1,y])
        if not left:
            available_actions.append([x,y-1])
        if not right:
            available_actions.append([x,y+1])
        
        return available_actions
    

    #Doing an action, returning a new puzzle
    def act(self,action):
        tmp = np.copy(self.current_state)
        i,j = self.empty_tile[0],self.empty_tile[1]
        tmp[i][j] = tmp[action[0]][action[1]]
        tmp[action[0]][action[1]] = 0
        return Puzzle(tmp,self.goal_state)

    #Printing a puzzle with colors, worls only for 3x3 configurations
    def print_puzzle(self):
        left_down= '\u2514'
        right_down= '\u2518'
        right_up= '\u2510'
        left_up = '\u250C'
        middle = '\u253C'
        top = '\u252C'
        bottom= '\u2534'
        right= '\u2524'
        left= '\u251C'
            
            #line color
        line = Style.BRIGHT + Fore.GREEN+ '\u2502' + Fore.RESET + Style.RESET_ALL
        dash = '\u2500'

            #Line draw code
        f_line = Style.BRIGHT  + Fore.GREEN+ left_up + dash + dash + dash +(top+ dash + dash + dash)*(len(self.current_state)-1) + right_up + Fore.RESET + Style.RESET_ALL

        m_line = Style.BRIGHT + Fore.GREEN+ left + dash + dash + dash + (middle+ dash + dash + dash)*(len(self.current_state)-1) + right+ Fore.RESET + Style.RESET_ALL

        l_line = Style.BRIGHT + Fore.GREEN + left_down + dash + dash + dash + (bottom+ dash + dash + dash)*(len(self.current_state)-1)  + right_down + Fore.RESET + Style.RESET_ALL
        print(f_line)
        for i in range(len(self.current_state)):
            for j in self.current_state[i]:
                if j == 0:
                    print(line, Back.WHITE + ' ' + Back.RESET, end=' ')
                else:
                    print(line, j, end=' ')
            print(line)
            if i == len(self.current_state)-1:
                print(l_line)
            else:
                print(m_line)


#Getting a numpy array representing the goal state given the number of tiles of the puzzle.
#The convention is that the empty tile is in the bottom right corner
#And the numbers are ordered
def get_goal_state(nb_tiles):
        #Starting from the goal state
    init_state = []
    cpt = 1
    for i in range(nb_tiles):
        init_state.append([])
        for j in range(nb_tiles):
            if (i == nb_tiles -1) and (j == nb_tiles -1):
                init_state[i].append(0)
                break
            init_state[i].append(cpt)
            cpt += 1
    return np.array(init_state)
   
                
#Generating a random nb_tiles x nb_tiles puzzle, doing nb_move random actions.

def generate_random(nb_tiles,nb_moves):
    init_state = get_goal_state(nb_tiles)
    goal_state = np.copy(init_state)
    puz = Puzzle(init_state,goal_state)
    #Generating random actions
    visited_states = set()
    visited_states.add(str(puz))
    for i in range(nb_moves):
        while(str(puz) in visited_states):
            actions = puz.available_actions()
            rand_action = actions[random.randint(0,len(actions) - 1)]
            puz = puz.act(rand_action)
        visited_states.add(str(puz))
    return puz


#Getting a puzzle from a txt file
def get_from_txt(filename):
    file = open(filename,'r')
    lines = file.readlines()
    init_state = []

    for i in range(len(lines)):
        if i == 0:
            line = lines[i].split()
            dim = int(line[1])
        else:
            line = lines[i].split(",")
            init_state.append([])
            for elem in line:
                if elem != "\n":
                    init_state[i-1].append(int(elem))
    return (np.array(init_state),dim)
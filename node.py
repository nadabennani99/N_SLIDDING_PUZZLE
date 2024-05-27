from puzzle import *
import copy


# Finding the indexes (i,j) of elem in the mat
def find_elem(mat,elem):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==elem:
                return i,j
    return None 
    
class Node():
    def __init__(self,state,goal_state,action = None,nb_iter = 0,parent_node= None,heuristic = "manhattan"):
        #Puzzle configuration
        self.state = Puzzle(state,goal_state)
        #Action that was done to get to this node
        self.action = action
        #Depth of the node
        self.depth=nb_iter
        #Total cost of the node
        self.f = nb_iter

        self.parent_node = parent_node
        self.heuristic = heuristic
        #Adding the heuristic to the total cost
        self.compute_heuristic()
    
    def expand(self):
        available_actions = self.state.available_actions() # List of available actions
        node_list = [] # List of children nodes
        for action in available_actions:
            state = self.state.act(action)
            node_list.append(Node(state.current_state,goal_state = self.state.goal_state,action = action,nb_iter = copy.deepcopy(self.depth) +1,parent_node = self,heuristic = self.heuristic))
        return node_list
    
    def __eq__(self,node):
        if self.state == node.state and self.action == node.action and self.f == node.f and self.parent_node == node.parent_node:
            return True
        return False

    def __lt__(self,node):
        if self.f < node.f:
            return True
        return False
                
                
    def heuristicNull(self):
        return 0

    def manhattan(self, x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
    
    #number of displaced tiles     
    def compute_heuristic(self):
            if self.heuristic== "misplaced_tiles": #Hamming distanec
                for current_state, goal_state in zip(self.state.current_state, self.state.goal_state):
                    if not np.array_equal(current_state, goal_state):
                        self.f+= 1
            elif self.heuristic == "manhattan": #Manhattan distance
                for i in range(len(self.state.current_state )):
                    for j in range(len(self.state.current_state )):
                        x,y=find_elem(self.state.goal_state,self.state.current_state[i][j])
                        self.f+=self.manhattan(i, j, x, y) 
                        
            else: #UCS
                self.f+=0
                #print('Unknown heuristic function is being used.')

def get_action(state,x_1,y_1): # Transforming the tuple actions into textual ones for the display of the path
    x,y = state.empty_tile
    if x_1 == x-1:
        return "left"
    if x_1 == x+1:
        return "right"
    if y_1 == y-1:
        return "up"
    if y_1 == y+1:
        return "down"


def show_family(node):
    #Storing the solution
    curr = node
    cost = node.f
    ret = []
    while curr.parent_node:
        ret.append(curr)
        curr = curr.parent_node
    if curr:
        ret.append(curr)
    print("Final cost",cost)
    ret = list(reversed(ret))
    for i in range(len(ret)):
        nod = ret[i]
        print("step",i)
        if i>= 1:
            temp = ret[i-1]
            x,y = nod.action
            print("Action",get_action(temp.state,x,y))
        if(node.state.dim)==3:
            print(nod.state.print_puzzle())
        else:
            print(nod.state.show_game())


def store_path(node):
    #Storing the solution
    curr = node
    cost = node.f
    ret = []
    while curr.parent_node:
        ret.append(curr)
        curr = curr.parent_node
    if curr:
        ret.append(curr)
    ret = list(reversed(ret))
    return ret





def show_path_two_sides(node_1,node_2):
    #Storing the solution
    curr = node_1
    cost = node_1.f + node_2.f
    ret = []
    while curr.parent_node:
        ret.append(curr)
        curr = curr.parent_node
    if curr:
        ret.append(curr)
    print("Final cost",cost)
    ret = list(reversed(ret))
    for i in range(len(ret)):
        nod = ret[i]
        print("step",i)
        if i>= 1:
            temp = ret[i-1]
            x,y = nod.action
            print("Action",get_action(temp.state,x,y))
        if(nod.state.dim)==3:
            print(nod.state.print_puzzle())
        else:
            print(nod.state.show_game())
    #Storing the path to the goal node from the intersection node
    #But no reverse to the list this time
    n = len(ret)
    curr = node_2
    ret = []
    while curr.parent_node:
        ret.append(curr)
        curr = curr.parent_node
    if curr:
        ret.append(curr)
    for i in range(len(ret) - 1):
        nod = ret[i+1]
        print("step",i+n)
        if i>= 1:
            temp = ret[i-1]
            if nod.action:
                x,y = nod.action

                print("Action",get_action(temp.state,x,y))
            else:
                print("Action: undefined")
        if(nod.state.dim)==3:
            print(nod.state.print_puzzle())
        else:
            print(nod.state.show_game())


            




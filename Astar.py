
from node import *
from puzzle import *
import heapq

class Astar:

    def __init__(self,init_state,goal_state,heuristic):
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic

    def solve(self,show_path = False):
        #Set of explored states
        explored_states = set()
        #Using a list for the priority queue in order to use the heapq library
        pt_queue = []
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        #Putting the initial node with a cost of 0
        pt_queue.append((0,debut_node))
        #Storing the different queue sizes in the algorithm
        max_number=0
        while pt_queue:
            #Getting the node from the value (node.f,node)
            popped_node = heapq.heappop(pt_queue)[1]
            if len(pt_queue)>max_number:
                max_number=len(pt_queue)

            #If the node was already explored
            if popped_node.state in explored_states:
                continue
            else:
                explored_states.add(popped_node.state)        
            #If the node contains the goal state
            if popped_node.state.is_goal_state():
                print("ok")
                #Displaying the path
                if show_path:
                    print(show_family(popped_node))
                path = store_path(popped_node)
                break
            #Getting the next states
            neighbours = popped_node.expand()
            for son in neighbours:
                if son.state in explored_states:
                    continue
                heapq.heappush(pt_queue,(son.f,son))
        #Getting the maximum size of the queue throughout the algorithm execution
        return max_number,path

            


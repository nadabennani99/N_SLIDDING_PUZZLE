
from node import *
from puzzle import *
import heapq

class BiSearchA:
    def __init__(self,init_state,goal_state,heuristic):
        #Source and destination frontiers
        self.src_queue = []
        self.dest_queue = []
        #Dictionaries in order to keep track of the nodes to retrace the path
        self.src_dict = {}
        self.dest_dict = {}
        #Set of closed states
        self.src_visited = set()
        self.dest_visited = set()
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic
    

    def solve(self,show_path = False):
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        goal_node = Node(self.goal_state,self.init_state,heuristic=self.heuristic)
        self.src_queue.append((0,debut_node))
        self.dest_queue.append((0,goal_node))
        max_number_src=0
        max_number_dest=0
        while (self.src_queue and self.dest_queue):
            
            
            #Checking if a common state is found --> A path is found
            intersection = self.src_visited.intersection(self.dest_visited)
            if len(intersection) != 0:
                if show_path:
                    #Getting the common state in the both closed states sets
                    meeting_state = intersection.pop()
                    left_path_start = self.src_dict[meeting_state]
                    right_path_start = self.dest_dict[meeting_state]
                    #Displaying the path
                    print(show_path_two_sides(left_path_start,right_path_start))
                break
            if len(self.src_queue)>max_number_src:
                max_number_src=len(self.src_queue)
            #Starting the search from the source node
            popped_node = heapq.heappop(self.src_queue)[1]
            if popped_node.state not in self.src_visited:
                self.src_visited.add(popped_node.state)
                self.src_dict[popped_node.state] = popped_node
                neighbours = popped_node.expand()
                for son in neighbours:
                    if son.state in self.src_visited:
                        continue
                    heapq.heappush(self.src_queue,(son.f,son))
            if len(self.dest_queue)>max_number_dest:
                max_number_dest=len(self.dest_queue)
            #Starting the search from the goal node
            popped_node = heapq.heappop(self.dest_queue)[1]
            if popped_node.state not in self.dest_visited:
                self.dest_visited.add(popped_node.state)
                self.dest_dict[popped_node.state] = popped_node
                neighbours = popped_node.expand()
                for son in neighbours:
                    if son.state in self.dest_visited:
                        continue
                    heapq.heappush(self.dest_queue,(son.f,son))
        return max_number_src,max_number_dest


from node import *
from puzzle import *
from queue import Queue

class BFS:
	
	def __init__(self,init_state,goal_state):
		self.init_state = init_state
		self.goal_state = goal_state
				
	def solve(self,show_path= False):
		#Set of visited states
		visited=set()
		#Frontier
		queue=Queue()
		debut_node=Node(self.init_state,self.goal_state,heuristic=None)
		queue.put(debut_node)
		path_found = False
		max_number=0
		while not queue.empty():
			if queue.qsize()>max_number:
				max_number=queue.qsize()
			popped_node = queue.get()
			if popped_node.state in visited:
				continue
			if popped_node.state.is_goal_state():
				print("ok")
				if show_path:
					print(show_family(popped_node))
				
				path = store_path(popped_node)
				break
			for node_next in popped_node.expand():
				if node_next.state not in visited:
					queue.put(node_next)
			visited.add(popped_node.state)
		return max_number,path


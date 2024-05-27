from puzzle import *
import random


#Generating random puzzles in files
for i in range(50):
    shuffles = random.randint(15,25)
    puz = generate_random(5,shuffles)
    puz.put_txt("puzzle_5x5_"+str(i)+".txt")






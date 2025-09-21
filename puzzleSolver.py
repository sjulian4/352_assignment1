import sys
from queue import PriorityQueue
from TileProblem import TileProblem
from Heuristics import manhattan_distance, misplaced_tiles
import heapq
from itertools import count
 

def a_star(H, tile_problem):
    explored = []
    actions = []
    counter = count()
    start = tile_problem.initial_state

   # Code from slides
    frontier = PriorityQueue()
    frontier.put((0, next(counter),start, "Start"))  
    while not frontier.empty():
        current_frontier = frontier.get()
        current = current_frontier[2]
        actions.append(current_frontier[3])
        if tile_problem.goal_test(current):
            return current
        if current not in explored:
            explored.append(current)
            for action in tile_problem.actions(current):
                new_node = tile_problem.result(current,action)
                if int(H) == 1:
                    heuristic = manhattan_distance(new_node, tile_problem.goal_state)
                else:
                    heuristic = misplaced_tiles(new_node, tile_problem.goal_state)
                frontier.put((heuristic,next(counter),new_node, action))
 
   ###################



# def rbfs(tile_problem):






def main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH):
    #Get the initial state from the input file
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.readlines()
        initial_state = []
        for line in lines:
            row = [int(x) if x != '' else None for x in line.strip().split(',')]
            initial_state.append(row)
    print("Initial State:" + str(initial_state))

    tile_problem = TileProblem(initial_state)
    print(tile_problem.actions(initial_state))
    if int(A) == 1:
        print("here")
        output = a_star(H, tile_problem)
        print("final output:" + str(output))
    # else:
    #     output = rbfs(tile_problem)

    #then write the output to the output file here


if __name__ == '__main__':
    A = sys.argv[1]  # A=1 is A*, A=2 is RBFS
    N = sys.argv[2] # size of puzzle, 3 is 8-puzzle, 4 is 15-puzzle
    H = sys.argv[3] # H=1 is manhattan distance, H=2 is misplaced tiles
    INPUT_FILE_PATH = sys.argv[4] #input file name
    OUTPUT_FILE_PATH = sys.argv[5] #output file name
    main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH)
import sys
from queue import PriorityQueue
from TileProblem import TileProblem
from Heuristics import manhattan_distance, misplaced_tiles
import heapq
from itertools import count
import math
 

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
        if current_frontier[3] != "Start":
            actions.append(current_frontier[3])
        if tile_problem.goal_test(current):
            return (current,actions)
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



def rbfs(H, tile_problem, node, f-limit):

function RBFS(problem, node, f-limit)
returns a solution or failure and a new f-cost limit
if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
successors ← [ ]
for each action in problem.ACTIONS(node.STATE) do
    add CHILD-NODE(problem, node, action) into successors
if successors is empty then return failure, ∞
for each s in successors do
    /* update f with value from previous search, if any */
    s.f ← max (s.g + s.h, node.f))
loop do
    best ← the lowest f-value in successors
    if best.f > f-limit then return failure, best.f
    alternative ← the second lowest f-value among successors
    result, best.f ← RBFS (problem, best, min(f-limit,alternative))
    if result != failure then return result




def main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH):
    #Get the initial state from the input file
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.readlines()
        initial_state = []
        for line in lines:
            row = [int(x) if x != '' else None for x in line.strip().split(',')]
            initial_state.append(row)

    tile_problem = TileProblem(initial_state)
    if int(A) == 1:
        (output_state, actions) = a_star(H, tile_problem)

    else:
        (output_state, actions) = rbfs(H, tile_problem, tile_problem.initial_state, math.inf)


    print("final output:" + str(output_state))
    print("actions:" + str(actions))
    with open(OUTPUT_FILE_PATH, 'w') as f:
        f.write(','.join(actions))

if __name__ == '__main__':
    A = sys.argv[1]  # A=1 is A*, A=2 is RBFS
    N = sys.argv[2] # size of puzzle, 3 is 8-puzzle, 4 is 15-puzzle
    H = sys.argv[3] # H=1 is manhattan distance, H=2 is misplaced tiles
    INPUT_FILE_PATH = sys.argv[4] #input file name
    OUTPUT_FILE_PATH = sys.argv[5] #output file name
    main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH)
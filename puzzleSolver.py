import sys
from queue import PriorityQueue
from TileProblem import TileProblem
from Heuristics import manhattan_distance, misplaced_tiles
import heapq
from itertools import count
import math
 
class Node:
    def __init__(self, problem, state, action, parent, g, h, f):
        self.problem = problem
        self.state = state
        self.action = action
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f


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



def rbfs(H, tile_problem, node, f_limit, solution):
    if tile_problem.goal_test(node.state):
        return (node.state,node.f, solution)
    successors = []
    for action in tile_problem.actions(node.state):
        new_state = tile_problem.result(node.state, action)
        if node.parent and new_state == node.parent.state:
            continue
        if int(H) == 1:
            heuristic = manhattan_distance(new_state, tile_problem.goal_state)
        else:
            heuristic = misplaced_tiles(new_state, tile_problem.goal_state)
        child_node = Node(
            problem=tile_problem,
            state=new_state, 
            action=action, 
            parent=node,
            g=node.g + tile_problem.step_cost(node.state,action,new_state), 
            h=heuristic, 
            f=math.inf,
            )
        successors.append(child_node)
    if not successors:
        return ("failure", math.inf)
    for s in successors:
        #  update f with value from previous search, if any 
        s.f = max (s.g + s.h, node.f)
    while True:
        best = min(successors, key=lambda node: node.f)
        if best.f > f_limit:
            return ("failure", best.f, solution)
        alternative = min((s.f for s in successors if s is not best), default=math.inf)
        new_f = min(f_limit, alternative)
        actions = solution + [best.action]
        result, best.f, temp_solution = rbfs(H, tile_problem, best, new_f, actions)
        if result[0] != "failure":
            return (result, best.f, temp_solution)




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
        if int(H) == 1:
            heuristic = manhattan_distance(tile_problem.initial_state, tile_problem.goal_state)
        else:
            heuristic = misplaced_tiles(tile_problem.initial_state, tile_problem.goal_state)
        start_node = Node(
            problem=tile_problem, 
            state=tile_problem.initial_state, 
            action="start",
            parent=None,
            g=0, 
            h=heuristic, 
            f=heuristic,
            )
        (output_state, f, actions) = rbfs(H, tile_problem, start_node, math.inf,[])


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
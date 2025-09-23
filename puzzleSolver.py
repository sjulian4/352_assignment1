import sys
from queue import PriorityQueue
from TileProblem import TileProblem
from Heuristics import manhattan_distance, misplaced_tiles
import math
from itertools import count
# import time
# explored_states_counter = 0
# time.perf_counter()
class Node:
    def __init__(self, problem, state, action, parent, g, h, f):
        self.problem = problem
        self.state = state
        self.action = action
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f


def a_star(H, tile_problem, start_node):
    explored = set()
    counter = count()
    frontier = PriorityQueue()
    frontier.put((start_node.f,next(counter),start_node))  
    while not frontier.empty():
        current_frontier = frontier.get()[2]
        current = current_frontier.state
        if tile_problem.goal_test(current):
            actions = []
            while current_frontier.parent is not None:
                actions.append(current_frontier.action)
                current_frontier = current_frontier.parent
            actions.reverse()
            # print("states explored:" + str(len(explored)))
            # print("Memory: " + str(sys.getsizeof(explored)))
            return (current,actions)
        tuple_current = tuple(tuple(row) for row in current)
        if tuple_current not in explored:
            explored.add(tuple_current)

            for action in tile_problem.actions(current):
                if int(H) == 1:
                    heuristic = manhattan_distance(tile_problem.result(current,action), tile_problem.goal_state)
                else:
                    heuristic = misplaced_tiles(tile_problem.result(current,action), tile_problem.goal_state)
                new_node = Node(
                    problem=tile_problem,
                    state=tile_problem.result(current,action),
                    action=action,
                    parent=current_frontier,
                    g=current_frontier.g + tile_problem.step_cost(current_frontier.state,action,tile_problem.result(current,action)),
                    h=heuristic,
                    f=current_frontier.g + tile_problem.step_cost(current_frontier.state,action,tile_problem.result(current,action)) + heuristic,
                )
                frontier.put((new_node.f,next(counter),new_node))
    return ("failure", [])



def rbfs(H, tile_problem, node, f_limit, solution):
    # global explored_states_counter
    # explored_states_counter +=1
    if tile_problem.goal_test(node.state):
        # print("Memory: " + str(sys.getsizeof(solution)))
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
        if result != "failure":
            return (result, best.f, temp_solution)




def main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH):
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.readlines()
        initial_state = []
        for line in lines:
            row = [int(x) if x != '' else None for x in line.strip().split(',')]
            initial_state.append(row)

    tile_problem = TileProblem(initial_state)
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
    if int(A) == 1:
        # start_time = time.perf_counter()
        (output_state, actions) = a_star(H, tile_problem, start_node)
        # end_time = time.perf_counter()
    else:
        # start_time = time.perf_counter()
        (output_state, f, actions) = rbfs(H, tile_problem, start_node, math.inf,[])
        # end_time = time.perf_counter()
    # print("Time taken (in milliseconds): " + str((end_time - start_time) * 1000))


    # print("final output:" + str(output_state))
    # print("actions:" + str(actions))
    # print("number of states explored:" + str(explored_states_counter))
    with open(OUTPUT_FILE_PATH, 'w') as f:
        f.write(','.join(actions))

if __name__ == '__main__':
    A = sys.argv[1]  # A=1 is A*, A=2 is RBFS
    N = sys.argv[2] # size of puzzle, 3 is 8-puzzle, 4 is 15-puzzle
    H = sys.argv[3] # H=1 is manhattan distance, H=2 is misplaced tiles
    INPUT_FILE_PATH = sys.argv[4] #input file name
    OUTPUT_FILE_PATH = sys.argv[5] #output file name
    main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH)
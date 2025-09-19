import sys
from TileProblem import TileProblem
 

def a_star(tile_problem):
   
   # Code from slides
   frontier = priority_queue()
   frontier = frontir + make-node(start)
   while not frontier.is-empty():
       current <- pop(frontier)
       if goal-test(current) return success
       for each action in current.actions():
            new <- action(current.state)
            new-node <- make-node(new,current,action)
            frontier = frontier + new-node
        


   ###################



def rbfs(tile_problem):






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
    if A == 1:
        output = a_star(tile_problem)
    else:
        output = rbfs(tile_problem)

    #then write the output to the output file here


if __name__ == '__main__':
    A = sys.argv[1]  # A=1 is A*, A=2 is RBFS
    N = sys.argv[2] # size of puzzle, 3 is 8-puzzle, 4 is 15-puzzle
    H = sys.argv[3] # H=1 is manhattan distance, H=2 is misplaced tiles
    INPUT_FILE_PATH = sys.argv[4] #input file name
    OUTPUT_FILE_PATH = sys.argv[5] #output file name
    main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH)
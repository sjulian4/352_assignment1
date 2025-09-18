import sys
from TileProblem import TileProblem
from 



def main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH):



if __name__ == '__main__':
    A = sys.argv[1]  # A=1 is A*, A=2 is RBFS
    N = sys.argv[2] # size of puzzle, 3 is 8-puzzle, 4 is 15-puzzle
    H = sys.argv[3] # H=1 is manhattan distance, H=2 is misplaced tiles
    INPUT_FILE_PATH = sys.argv[4] #input file name
    OUTPUT_FILE_PATH = sys.argv[5] #output file name
    main(A,N,H,INPUT_FILE_PATH,OUTPUT_FILE_PATH)
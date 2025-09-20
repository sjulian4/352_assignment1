def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != None: 
                print(state[i][j])
                goal_state = [cell for row in state for cell in row]
                print(goal_state)
                goal_row, goal_col = divmod(goal_state.index(state[i][j]), len(state))
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance
def misplaced_tiles(state, goal_state):
    misplaced = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != None and state[i][j] != goal_state[i][j]:  
                misplaced += 1
    return misplaced
def manhattan_distance(state, goal_state):
    distance = 0
    flat_goal = [cell for row in goal_state for cell in row]
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != None: 
                goal_row, goal_col = divmod(flat_goal.index(state[i][j]), len(state))
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance
def misplaced_tiles(state, goal_state):
    misplaced = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != None and state[i][j] != goal_state[i][j]:  
                misplaced += 1
    return misplaced
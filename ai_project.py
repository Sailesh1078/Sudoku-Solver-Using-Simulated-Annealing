import random
import math

# function to print the sudoku puzzle
def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# funcction to store the locations of empty cells
def get_all_empty_cells(board):
    empty_cells = []

    for y, row in enumerate(board):
        for x in range(len(row)):
            if board[y][x] == 0:
                empty_cells.append((y, x))

    return empty_cells

# function to calculate the cost of given list based on no of repetitions
def get_list_cost(arr):
    cost = 0
    size = len(arr)
    
    for i in range(size): 
        for j in range(i + 1, size): 
            if arr[i] == arr[j]: 
                cost += 1 

    return cost

# function to calculate the cost of given entire boardd based on no of repetitions
def get_sudoku_cost(board):
    cost = 0
    
    # iterate over each row in the board
    for y, row in enumerate(board):
        cost += get_list_cost(row)
    
    # iterate over each column in the board
    for x in range(9):
        col = [board[y][x] for y in range(9)]
        cost += get_list_cost(col)
    
    # iterate over each sub-grid in the board
    for i in range(3):
        for j in range(3):
            subgrid = [board[y][x] for y in range(i*3, (i+1)*3) for x in range(j*3, (j+1)*3)]
            cost += get_list_cost(subgrid)
    
    return cost
 
# funtion to initialize the board by filling the empty cells
def initialize_sudoku_board(board):
    # create a copy of the input board to avoid modifying the original board
    new_board = [row[:] for row in board]

    for y, row in enumerate(board):
        numbers = [] # list to store the non zero numbers in the row.

        # get all current non zero numbers in the row
        for x, col in enumerate(row):
            if col != 0:
                numbers.append(col)
        # print(numbers)

        # iterate over each column in the row.
        for x, col in enumerate(row):
            if col == 0: 
                while True: 
                    candidate = random.randint(1, 9) 

                    if candidate not in numbers: 
                        new_board[y][x] = candidate # fill the random number if its not repeated 
                        numbers.append(candidate)

                        break

    return new_board

# generate a random state by swapping 2 random to be filled cells
def generate_neighbor(board, empty_cells):
    # make a copy of the board
    new_board = [row[:] for row in board]  

    # choose two empty cells at random
    cell1, cell2 = random.sample(empty_cells, 2)

    # swap their values
    new_board[cell1[0]][cell1[1]], new_board[cell2[0]][cell2[1]] = new_board[cell2[0]][cell2[1]], new_board[cell1[0]][cell1[1]]  
    
    return new_board

def solve_sudoku(board, max_iteration=100000, initial_temperature=0.1, cooling_rate=0.999):
    empty_cells = get_all_empty_cells(board)
    initial_board = initialize_sudoku_board(board)

    # make a copy of the board
    current_state = [row[:] for row in initial_board]

    # get the cost of the initial board
    current_cost = get_sudoku_cost(current_state)

    current_temperature = initial_temperature
    iteration = 0

    print("\nSolving Sudoku board...\n")

    while iteration < max_iteration:
        # sudoku is solved if the current cost is 0
        if current_cost == 0:
            print("\nThe Sudoku puzzle has been solved!\n")
            print(f"Iterations taken: {iteration}\nCurrent temperature: {current_temperature}\nThe solved puzzle :")
            
            return current_state

        # generate a new state 
        new_state = generate_neighbor(current_state, empty_cells)

        # get the cost of the newly generated neighbor
        new_cost = get_sudoku_cost(new_state)

        delta_cost = new_cost - current_cost
        
        # change if the new state cost is kower than the currnt state
        if delta_cost < 0:
            current_state = [row[:] for row in new_state]
            current_cost = new_cost
        else:
            # even if the new cost is greater than the current cost, calculate the probability to accept it
            acceptance_probability = math.exp(-delta_cost / current_temperature)
            
            if random.random() < acceptance_probability:
                current_state = [row[:] for row in new_state]
                current_cost = new_cost

        iteration += 1

        # update the temperature
        current_temperature = current_temperature * cooling_rate

    print(f"\nSudoku could not be solved even after {iteration} iterations.\n Either the no of iterations was not enough (or)\n the Sudoku may be invalid (or)\n need to update the parameters.\n Current state :")
    
    return current_state

# main code:

# medium puzzle
'''board = [
    [5, 7, 0, 1, 8, 6, 2, 9, 3],
    [2, 6, 8, 3, 7, 9, 1, 0, 0],
    [9, 0, 0, 0, 0, 0, 8, 7, 6],
    [0, 0, 0, 2, 5, 8, 7, 6, 1],
    [0, 5, 1, 0, 0, 0, 9, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 5, 4, 8, 2],
    [3, 4, 7, 8, 2, 1, 0, 5, 9]
]'''

# easy puzzle
board = [
    [6, 8, 0, 2, 5, 0, 0, 0, 7],
    [5, 7, 1, 6, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [3, 1, 0, 7, 8, 0, 0, 0, 6],
    [0, 4, 0, 0, 0, 5, 1, 9, 8],
    [8, 6, 5, 0, 0, 0, 0, 0, 3],
    [0, 3, 2, 9, 1, 8, 6, 5, 0],
    [0, 9, 0, 5, 0, 7, 8, 2, 0],
    [0, 0, 0, 4, 2, 0, 7, 3, 9]
]

'''
# invalid puzzle
board = [
    [6, 8, 0, 2, 5, 0, 7, 0, 7],
    [5, 7, 1, 6, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [3, 1, 0, 7, 8, 0, 0, 0, 6],
    [0, 4, 0, 0, 0, 5, 1, 9, 8],
    [8, 6, 5, 0, 0, 0, 0, 0, 3],
    [0, 3, 2, 9, 1, 8, 6, 5, 0],
    [0, 9, 0, 5, 0, 7, 8, 2, 0],
    [0, 0, 0, 4, 2, 0, 7, 3, 9]
]
'''

solved_board = solve_sudoku(board)
print_sudoku(solved_board)

from queue import PriorityQueue  # Importing PriorityQueue for implementing the priority queue data structure
import math  # Importing math module for mathematical operations

# Initialize an empty matrix (will be built in the build_matrix function)
matrix = []

def build_matrix():
    """
    Builds a 16x10 matrix where each element is a tuple representing its coordinates.
    """
    matrix = []  # Initialize the matrix as an empty list
    for row in range(0, 16):  # Iterate over the rows from 0 to 15
        rows = []  # Initialize the current row as an empty list
        for col in range(0, 10):  # Iterate over the columns from 0 to 9
            rows.append((row, col))  # Append the tuple (row, col) to the current row
        matrix.append(rows)  # Append the current row to the matrix
    return matrix  # Return the completed matrix

# Define the list of obstacles as tuples representing their coordinates
obstacles = [
    (1, 1), (1, 2), (2, 1), (2, 2), (3, 1),
    (3, 2), (1, 7), (1, 8), (2, 7), (2, 8),
    (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2),
    (3, 4), (3, 5), (4, 4), (4, 5), (5, 4), (5, 5), (6, 4), (6, 5),
    (7, 7), (7, 8), (7, 9), (7, 10), (8, 8), (8, 9), (8, 10)
]

def get_distance(position, goal):
    """
    Calculates the Euclidean distance between the current position and the goal.
    """
    return math.sqrt(math.pow((goal[0] - position[0]), 2) + math.pow((goal[1] - position[1]), 2))  # Calculate and return the Euclidean distance

def is_goal(curr, goal):
    """
    Checks if the current position is the goal position.
    """
    return curr == goal  # Return True if the coordinates match the goal

def is_valid(position):
    """
    Checks if a position is within bounds and not an obstacle.
    """
    x, y = position  # Unpack the position into x and y
    return (0 <= x <= 15) and (0 <= y <= 9) and position not in obstacles  # Check if the position is within bounds and not an obstacle

def find_path(start, goal):
    """
    Finds a path from the start position to the goal position using the A* algorithm.
    """
    pq = PriorityQueue()  # Create a priority queue
    pq.put((0, start))  # Put the initial state (cost, start position) in the priority queue
    came_from = {start: None}  # Dictionary to keep track of the path
    cost_so_far = {start: 0}  # Dictionary to keep track of the cost to reach each position

    while not pq.empty():  # Continue until the priority queue is empty
        _, current = pq.get()  # Get the position with the lowest cost from the priority queue

        if is_goal(current, goal):  # Check if the current position is the goal
            break  # If it is, break out of the loop

        x, y = current  # Unpack the current position into x and y

        # Generate possible moves (right, left, up, down)
        for move in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if is_valid(move):  # Check if the move is valid
                new_cost = cost_so_far[current] + 1  # Calculate the new cost to reach the move
                if move not in cost_so_far or new_cost < cost_so_far[move]:
                    cost_so_far[move] = new_cost  # Update the cost to reach the move
                    priority = new_cost + get_distance(move, goal)  # Calculate the priority using the new cost and heuristic
                    pq.put((priority, move))  # Put the move in the priority queue with the calculated priority
                    came_from[move] = current  # Update the path

    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()  # Reverse the path to get it from start to goal
    return path  # Return the path found

# Print the path found from (4, 1) to (4, 9)
print(find_path((4, 1), (4, 9)))

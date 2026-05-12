# --- PUZZLE 4: AUTONOMOUS NAVIGATION ---

def navigate_maze(start_x, start_y, command_list):
    # 1. Create variables to track current position
    x = start_x
    y = start_y
    
    # 2. Loop through the list of commands
    for command in _________:
        
        # 3. Use logic and operations to change X and Y based on the command
        if command == "UP":
            y = y + 1
        elif command == "DOWN":
            y = _______
        elif command == _______:
            x = x - 1
        # Add the final condition for "RIGHT"
        ____________________
            ________________
            
    # 4. Return the final coordinates as a list
    return [x, y]

# --- TEST AREA ---
movements = ["UP", "UP", "RIGHT", "DOWN", "RIGHT"]
# Starting at x=0, y=0. 
# Expected final position should be [2, 1]
final_position = navigate_maze(0, 0, movements)
print("Robot's final location is:", final_position)
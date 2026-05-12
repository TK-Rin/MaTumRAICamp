def navigate_maze(start_x, start_y, command_list):
    x = start_x
    y = start_y
    
    for command in command_list:
        
        if command == "UP":
            y = y + 1
        elif command == "DOWN":
            y = y - 1
        elif command == "LEFT":
            x = x - 1
        elif command == "RIGHT":
            x = x + 1
            
    return [x, y]

movements = ["UP", "UP", "RIGHT", "DOWN", "RIGHT"]
final_position = navigate_maze(0, 0, movements)
print("Robot's final location is:", final_position)
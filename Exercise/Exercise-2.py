# --- EXERCISE 2: DELIVERY CALCULATOR ---

# 1. Define a function called 'calculate_time' that takes two parameters: distance and speed
_____ calculate_time(_____, _____):
    
    # 2. Use the division operator (/) to find the time (distance divided by speed)
    delivery_time = _____ _____ _____
    
    # 3. Use the built-in round() function to round the time to 2 decimal places
    rounded_time = _____(delivery_time, 2)
    
    # 4. Return the final rounded time
    _____ rounded_time

# --- TEST AREA ---
table_distance = 15.5 # meters
teenoi_speed = 1.2 # meters per second

# Call your function here
time_to_table = calculate_time(table_distance, teenoi_speed)
print("Time to deliver: ", time_to_table, "seconds")
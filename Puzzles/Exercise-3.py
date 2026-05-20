# --- EXERCISE 3: SERVING TABLES ---

tables_to_serve = [4, 7, 2, 9]
battery = 30

# 1. Use a for loop to iterate through 'tables_to_serve'
_____ table _____ tables_to_serve:
    
    # 2. Check if the battery is greater than 10 using an if-else statement
    _____ battery > 10:
        print("Serving table number", table)
        
        # 3. Decrease the battery by 10 for every table served
        battery = battery - _____
        
    _____:
        print("Battery too low! Cannot serve table", table)

print("Final battery level:", battery)

# 4. Now, use a while loop to recharge the robot back to 50
print("Heading to charging station...")
_____ battery < 50:
    battery = battery + 10
    print("Charging... Battery at:", battery)
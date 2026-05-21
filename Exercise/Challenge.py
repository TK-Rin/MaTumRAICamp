# --- FINAL CHALLENGE: TEENOI'S FULL SHIFT ---

# 1. Ask user to name the robot
robot_name = _____

# 2. Define a function to process deliveries
def run_deliveries(orders, starting_battery):
    current_battery = starting_battery
    
    # 3. Loop through the orders list
    for _____ in _____:
        
        # 4. Logic: If battery is 0, break the loop and print a warning
        if __________:
            print("CRITICAL: Out of battery! Stopping.")
            _____ # Use this keyword to exit the loop early
            
        print(robot_name, "is delivering to table", order)
        # 5. Decrease battery by 15 per delivery
        current_battery = ____________
        
    return current_battery

# --- EXECUTION ---
# 6. Create a list of 4 table numbers
table_orders = [___, ___, ___, ___]

# 7. Call the function with a starting battery of 50 and save the result
final_battery = run_deliveries(________, 50)

print("Shift complete. Remaining battery:", final_battery)
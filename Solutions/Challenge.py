robot_name = input("Enter robot name: ")

def run_deliveries(orders, starting_battery):
    current_battery = starting_battery
    
    for order in orders:
        if current_battery <= 0:
            print("CRITICAL: Out of battery! Stopping.")
            break 
            
        print(robot_name, "is delivering to table", order)
        current_battery = current_battery - 15
        
    return current_battery

table_orders = [12, 5, 8, 3]

final_battery = run_deliveries(table_orders, 50)

print("Shift complete. Remaining battery:", final_battery)
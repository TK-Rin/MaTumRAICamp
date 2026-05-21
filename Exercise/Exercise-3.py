# --- EXERCISE: TEENOI'S STATE MACHINE DEBUGGING ---
# GOAL: Fix the 4 bugs so Teenoi can finish all 3 deliveries and power off!

state = "IDLE"
battery = 50
orders_left = 3

print("Booting up Teenoi...")

# The main system loop keeps running until the state is POWER_OFF
while state != "POWER_OFF":
    
    if state == "IDLE":
        if orders_left > 0:
            print("New order received! Changing state to DELIVERING.")
            state = "DELIVERING"
        else:
            print("All orders finished. Shutting down.")
            state = "POWER_OFF"
            
    # BUG 1: Syntax error here! Look closely at the comparison.
    elif state = "DELIVERING":
        print("Delivering food...")
        orders_left = orders_left - 1
        battery = battery - 25
        print("Order complete! Battery left:", battery)
        
        # BUG 2: Logic error! If battery is 25 or less, we need to transition 
        # to the charging state, not go back to idle.
        if battery <= 25:
            print("Warning: Battery low!")
            state = "IDLE" 
        else:
            state = "IDLE"

    # BUG 3: Syntax error! What punctuation is missing at the end of this line?
    elif state == "LOW_BATTERY"
        print("Returning to dock to charge...")
        
        # BUG 4: Logic error! Teenoi never actually recharges, and never leaves 
        # this state. This causes an infinite loop! Add code to fix this.
        print("Charging...")
        
        
print("System offline. Great job debugging!")
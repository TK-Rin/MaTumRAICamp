# --- PUZZLE 3: INVENTORY SCANNER ---

# 1. Define a function named 'calculate_weight' that takes a list called 'items'
_____ calculate_weight(_____):
    total_weight = 0
    
    # 2. Create a loop to go through every 'item' in the 'items' list
    _____ item _____ items:
        # 3. Add the item's weight to the total
        total_weight = total_weight + _____
        
    return total_weight

# --- TEST AREA ---
# Do not change the code below, just run it to test your function!
scavenged_parts = [10, 5, 20, 2]
final_weight = calculate_weight(scavenged_parts)
print("Total Cargo Weight:", final_weight)
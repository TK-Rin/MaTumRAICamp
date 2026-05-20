# --- EXERCISE 4: DEBUGGING ---
# GOAL: Teenoi should return 5 empty trays to the kitchen, one by one.

empty_trays = 5

print("Returning trays to kitchen...")

# BUG 1 & 2 & 3 are in this loop block! Fix them.
while empty_trays > 0
    print("Returned a tray. Trays left:", empty_trays)
    
    if empty_trays = 0:
        print("All trays returned!")
        
# Hint: If you run this code as-is, what happens to the 'empty_trays' variable? 
# Why does the loop never stop?
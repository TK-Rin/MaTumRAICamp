empty_trays = 5

print("Returning trays to kitchen...")

# FIX 1: Added the missing colon (:) at the end of the while statement
# FIX 2: Decremented the empty_trays variable so it doesn't loop infinitely
# FIX 3: Changed = to == in the if statement (comparison, not assignment)
while empty_trays > 0:
    print("Returned a tray. Trays left:", empty_trays)
    empty_trays = empty_trays - 1 
    
    if empty_trays == 0:
        print("All trays returned!")
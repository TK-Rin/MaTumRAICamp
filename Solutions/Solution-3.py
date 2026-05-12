def calculate_weight(items):
    total_weight = 0
    
    for item in items:
        total_weight = total_weight + item
        
    return total_weight

scavenged_parts = [10, 5, 20, 2]
final_weight = calculate_weight(scavenged_parts)
print("Total Cargo Weight:", final_weight)
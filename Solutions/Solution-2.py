def calculate_time(distance, speed):
    delivery_time = distance / speed
    rounded_time = round(delivery_time, 2)
    return rounded_time

table_distance = 15.5 
teenoi_speed = 1.2 

time_to_table = calculate_time(table_distance, teenoi_speed)
print("Time to deliver: ", time_to_table, "seconds")
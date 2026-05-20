tables_to_serve = [4, 7, 2, 9]
battery = 30

for table in tables_to_serve:
    if battery > 10:
        print("Serving table number", table)
        battery = battery - 10
    else:
        print("Battery too low! Cannot serve table", table)

print("Final battery level:", battery)

print("Heading to charging station...")
while battery < 50:
    battery = battery + 10
    print("Charging... Battery at:", battery)
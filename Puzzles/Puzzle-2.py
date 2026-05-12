# --- PUZZLE 2: ENERGY CALCULATION ---

base_energy = 50
distance_km = 12
energy_per_km = 3.5

# 1. Calculate the energy needed for the trip (distance * energy_per_km)
trip_energy = _____

# 2. Calculate the total energy required (base_energy + trip_energy)
total_energy = _____

# 3. If the robot has a battery capacity of 100, calculate how much energy is left over
# (Hint: Use the modulo operator '%' or simple subtraction '-')
energy_remaining = 100 _____ total_energy

print("Total Energy Needed:", total_energy)
print("Energy Remaining:", energy_remaining)
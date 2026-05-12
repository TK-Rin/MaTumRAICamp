base_energy = 50
distance_km = 12
energy_per_km = 3.5

trip_energy = distance_km * energy_per_km
total_energy = base_energy + trip_energy
energy_remaining = 100 - total_energy 

print("Total Energy Needed:", total_energy)
print("Energy Remaining:", energy_remaining)
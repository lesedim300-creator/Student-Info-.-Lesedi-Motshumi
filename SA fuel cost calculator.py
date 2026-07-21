# Get user input 

kilometers = float(input("Enter the number of kilometers you want to drive: "))
petrol_price = float(input("Enter the petrol price per liter (R): "))

# Calculate liters needed
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Round the total cost to 2 decimal places
total_cost = round(total_cost, 2)

# Display results

print(f"Distance to travel: {kilometers} km")
print(f"Petrol price: R{petrol_price} per liter")
print(f"Liters needed: {liters_needed} liters")
print(f"Total fuel cost: R{total_cost}")
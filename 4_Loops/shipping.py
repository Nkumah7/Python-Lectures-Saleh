weight = 41.5

# Ground shipping
if weight <= 2:
    ground_cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    ground_cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    ground_cost = weight * 4.00 + 20.00
elif weight > 10:
    ground_cost = weight * 4.75 + 20.00
 
premium_cost = weight * 125
# print(premium_cost)

# Drone Shipping
if weight <= 2:
    drone_cost = weight * 4.5 + 0.00
elif weight > 2 and weight <= 6:
    drone_cost = weight * 9.00 + 0.00
elif weight > 6 and weight <= 10:
    drone_cost = weight * 12.00 + 0.00
elif weight > 10:
    drone_cost = weight * 14.25 + 0.00
    
print(f"Ground Shipping Cost: ", ground_cost)
print(f"Ground Premium Cost: ", premium_cost)
print(f"Drone Shipping Cost: ", drone_cost)

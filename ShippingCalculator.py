import os
import platform

# Getting the package weight
while True:
    package_weight = input("What's your package weight (lb)? ")
    try: 
        float(package_weight)
        package_weight = float(package_weight)
        if package_weight > 0:
            break
        else:
            print("Write a valid value")
    except ValueError:
        print("Write a valid value")
        continue
    
# Ground Shipping
ground_shipping = 20 # Flat Charge
if package_weight <= 2:
    ground_shipping += 1.5 * package_weight
elif 2 < package_weight <= 6:
    ground_shipping += 3 * package_weight
elif 6 < package_weight <= 10:
    ground_shipping += 4 * package_weight
elif package_weight > 10:
    ground_shipping += 4.75 * package_weight

# Ground Shipping Premium
ground_shipping_premium = 125 # Flat Charge (only)

# Drone Shipping
drone_shipping = 0 # Flat Charge
if package_weight <= 2:
    drone_shipping += 4.5 * package_weight
elif 2 < package_weight <= 6:
    drone_shipping += 9 * package_weight
elif 6 < package_weight <= 10:
    drone_shipping += 12 * package_weight
elif package_weight > 10:
    drone_shipping += 14.25 * package_weight

shipping_methods = {
    "Ground Shipping": ground_shipping,
    "Ground Shipping Premium": ground_shipping_premium,
    "Drone Shipping": drone_shipping
}
cheapest = min(shipping_methods, key=shipping_methods.get)

os.system('cls' if platform.system() == 'Windows' else 'clear')
print("===========================================")
print(f'Ground Shipping:   ${ground_shipping:.2f}')
print(f'Ground Shipping Premium:   ${ground_shipping_premium:.2f}')
print(f'Drone Shipping:   ${drone_shipping:.2f}')
print(f'Cheapest Shipping:   {cheapest}')
print("===========================================")

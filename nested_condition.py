print("Step 1 : Pick your vehicle")
print("1. Bike")
print("2. Car")
print()

choice = int(input("Enter 1 or 2"))

if choice == 1:
    print("Step 2 : Pick your bike")
    print("1. Scooty")
    print("2 .Mountain bike")
    print()

    bike_type = int(input("Enter 1 or 2"))

    if bike_type == 1:
        print("You picked : Scooty")
        print("Top speed : 80 kp/h")
        print("Best for : City roads")
    else:
        print("You picked : Mountain Bike")
        print("Top speed : 40 kp/h")
        print("Best for : Off-road trails")

elif choice == 2:
    print("Step 2 : Pick your car type ")
    print("1. Sedan")
    print("2. SUV")

    car_type = int(input("Enter 1 or 2"))

    if car_type == 1:
        print("You picked : Sedan")
        print("Seats : 5")
        print("Best for : Family trips")
    else:
        print("You picked : SUV")
        print("Seats : 7")
        print("Best for : Off-trail Adventures")

else:
    print("That was not a valid choice")
    print("Please enter 1 for Bike and 2 for Car")
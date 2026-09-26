print("   Welocome to the holiday planner!   ")

print("Step 1: Pick your holiday type")
print("1. Beach holiday")
print("2. Mountain holiday")
print()

choice = int(input("Enter 1 or 2"))

if choice == 1:
    print("Step 2: Pick your beach activity")
    print("1. Swimming")
    print("2. Sandcastle building")
    print()

    beach_activity = int(input("Enter 1 or 2"))

    if beach_activity == 1:
        print("You picked : Swimming")
        print("Best time : Morning")
        print("Remember : Carry sunscreen and water")
    else:
        print("You picked : Sandcastle building")
        print("Best time : Evening")
        print("Remember : Carry a bucket and a spade")
elif choice == 2:
    print("Step 2: Pick your mountain activity ")
    print("1. Hiking")
    print("2. Camping")
    print()

    mountain_activity = int(input("Enter 1 or 2"))

    if mountain_activity == 1:
        print("You picked : Hiking")
        print("Best for : Exploring trails")
        print("Remember : Wear comfortable shoes")
        print()
    else:
        print("You picked : Camping")
        print("Best for : Staying close to nature")
        print("Remember : Carry a flashlight and a tent")

else:
    print("That was not a valid choice")
    print("Please enter 1 for beach holiday or enter 2 for mountain holiday")

print("Your holiday plan is ready")
print("Enjoy your trip")
print("=== ATM Cash dispencer ===\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_sevred = 0
total_dispenced = 0

severing = True
while severing:
    name = input("What's your name?")
    amount = int(input("Hello {name}! Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive amount\n")
        continue

    print("\nDispencing {amount} units for {name}")
    remaining = amount
    idx = 1
    while idx <= 6:
        if idx == 1:
            value = 100
        elif idx == 2:
            value = 50
        elif idx == 3:
            value = 20
        elif idx == 4:
            value = 10
        elif idx == 5:
            value = 5
        else:
            value = 1
        count = remaining // value
        if count > 0:
            print("{count} x {value}-unit note(s) = {count * value}")
            remaining -= count * value
            if value == 100:
                total_100 += count
            elif value == 50:
                total_50 += count
            elif value == 20:
                total_20 += count
            elif value == 10:
                total_10 += count
            elif value == 5:
                total_5 += count
            else:
                total_1 += count
        idx += 1
    customers_sevred += 1
    total_dispenced += amount
    print("Transaction Complete, {name}!\n")
    again = input("Next customer (Yes/No):").strip().lower()
    if again != "Yes":
        severing = False

print("\n=== Daily Denomation Report ===")
for slot in range(1, 7):
    if slot == 1:
        value,total = 100,total_100
    elif slot == 2:
        value,total = 50,total_50
    elif slot == 3:
        value,total = 20,total_20
    elif slot == 4:
        value,total = 10,total_10
    elif slot == 5:
        value,total = 5,total_5
    else:
        value,total = 1,total_1
    if total > 0:
        print(" {value}-unit notes dispenced : {total}", end="")
    for note in range(total):
        print("=", end="")
    print()

print("Customers sevred : {customers_sevred}")
print("Total dispenced : {total_dispenced}")
print("ATM session closed. Goodbye")

print("=== Grocery Billing Queue\n")
low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_sevred = 0
total_sales = 0
billing = True

while billing:
    name = input("What's Your name?")
    item_count = int(input("Hello {name}! How many items?"))
    if item_count <= 0:
        print("Invalid number.Please choose a positive number")
        continue
    print("Billing items for {name}")
    customer_total = 0
    item_number = 1
    while item_number <= item_count:
        item_name = input("Item name : ")
        Price = int(input("Price : "))
        quantity = int(input("Quantity : "))

        if Price <= 0 or quantity <= 0:
            print("Invalid price or quantity.Please enter again.\n")
            continue
        item_total = quantity * Price
        print("{item_name} : {quantity} X {Price} = {item_total}")
        customer_total += item_total

        if Price < 50:
            low_price_items += quantity
        elif Price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    customers_sevred += 1
    total_sales += customer_total
    print("\nTotal bill for {name}: {customer_total}" )
    print("Billing complete!\n")

    again = input("Next customer (Yes/No)")

    if again != "Yes":
        billing = False

print("\n=== Grocery bill report ===")

for slot in range(1, 4):
    if slot == 1:
        Price,total = "low_price_items",low_price_items
    elif slot == 2:
        Price,total = "medium_price_items",medium_price_items
    else:
        Price,total = "High_price_items",high_price_items
    if total > 0:
        print("{Price}: {total}", end="")
        for item in range(total):
            print("*", end="")
        print()

print("\nCustomers sevred: {customers_sevred}")
print("\nTotal sales: {total_sales}")
print("Grocery billing closed.Goodbye!")
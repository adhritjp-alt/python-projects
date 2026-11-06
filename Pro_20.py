
valid = False
while not valid:

    try:
        bill = float(input("Bill amount: "))
        discount = float(input("Discount percent: "))
        people = int(input("Number of people: "))

        discount_amount = bill * discount / 100
        final_bill = bill - discount_amount
        each = final_bill / people

    except ValueError:
        print("Please type numbers only.")
    except ZeroDivisionError:
        print("People cannot be 0.")

    else:
        print("Final bill:", final_bill)
        print("Each person pays:", each)
        valid = True
    finally:
        print("Attempt finished.")

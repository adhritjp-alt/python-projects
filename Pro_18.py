def total_bill(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print("Please pay $ ", total)
    return total

total_bill(150,20)

def seating_arrangements(guests):
    '''This is a recursive function to find the number of seating arragements for guests'''

    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * seating_arrangements(guests - 1)

print(seating_arrangements.__doc__)

print("Seating arrangements for 1 guest: ", seating_arrangements(1))
print("Seating arrangements for 2 guest: ", seating_arrangements(2))
print("Seating arrangements for 3 guest: ", seating_arrangements(3))
print("Seating arrangements for 4 guest: ", seating_arrangements(4))
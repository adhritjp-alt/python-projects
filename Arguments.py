def total_calc(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print("Please pay $ ", total)

total_calc(150,20)

def cube(number):
     return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print(by_three(989))
print(by_three(333))

def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial.__doc__)
print("The factorial of 0 is: ", factorial(0))
print("The factorial of 1 is: ", factorial(1))
print("The factorial of 2 is: ", factorial(2))
print("The factorial of 5 is: ", factorial(5))
print("The factorial of 10 is: ", factorial(10))
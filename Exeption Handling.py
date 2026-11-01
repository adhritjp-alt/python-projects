# try:
#     number = int(input("Enter a number: "))
#     print("The number is: ", number)

# except ValueError as ex:
#     print("Exception: ", ex)

# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print("The result is: ", result)
# except ZeroDivisionError:
#     print("Division by Zero is not possible!!")
# except ValueError:
#     print("Please enter whole numbers")
# except:
#     print("Wrong input!")
# else:
#     print("No exception!")
# finally:
#     print("This excute no matter what!")

valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("Bye!")
            n = int(input("Enter a number: "))
        valid = True
    except ValueError:
        print("Invalid")
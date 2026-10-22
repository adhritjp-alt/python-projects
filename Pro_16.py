secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print("NUMBER GUESSING GAME")
print("=" * 42)
print("I have secret number between 1 to 50.")
print("You have 5 attempts to guess it.")
print("After, each wrong guess I will give you a hint.")
print()

while count < max_attempts and guess != secret:
    guess = int(input("Enter your guess"))
    count = count + 1

    if guess == secret:
        print()
        print("Correct! You have guessed it in ", count, "Attempt(s)")
        print("Well done - you are number wizard!")
    else:
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print("Ice cold - You have a far way")
        elif diff >= 10:
            print("Cold - Still quite a distance to go")
        elif diff >= 5:
            print("Warm -Getting Close!")
        else:
            print("Hot - Almost there!")

        remaining = max_attempts - count
        if remaining > 0:
            print("Lives left: ", end="")
            for i in range(remaining):
                print("O ", end="")
            print()
            print()

if guess != secret:
    print("=" * 42)
    print("Game over!You used all 5 attempts!")
    print("The secret number was ", secret)
    print("=" * 42)
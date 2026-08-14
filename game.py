import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Invalid input! Please guess between 1 and 100.")
    else:
        if guess == secret_number:
            print("Correct! You win!")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
             print("Thanks for playing!")
             break
            else:
                secret_number = random.randint(1, 100)
        elif guess < secret_number:
            print("Too low! increase your guess")
        else:
            print("Too high! decrease your guess")


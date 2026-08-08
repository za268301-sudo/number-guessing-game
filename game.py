import random
secret_number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))
if guess < 1 or guess > 100:
    print("Invalid input! Please guess between 1 and 100.")
else:
  if guess == secret_number:
    print("Correct! You win!")
  elif guess < secret_number:
    print("Too low!")
  else:
    print("Too high!")
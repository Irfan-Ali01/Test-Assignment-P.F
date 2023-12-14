import random
number = random.randint(1, 100)
guesses = 0
while guesses < 5:
  guess = int(input("Enter your guess: "))
  guesses += 1
  if guess == number:
    print("Correct!")
    print("Congratulations! You guessed the number.")
    break
  elif guess > number:
    print("Too high")
  else:
    print("Too low")
if guesses == 5:
  print("Game over! You ran out of guesses.")
  print("The number was", number)
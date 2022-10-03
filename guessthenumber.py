import random

guess = random.randint(1,10)

while True:
 question = int(input("Guess a number from 1 to 10: "))
 if question > guess:
  print("You too high !\n")
 elif question < guess:
    print("You are too low !\n")
 else:
    print(f"THE NUMBER {guess} IS CORRECT, CONGRATULATIONS !!!")
    break








    






import random

def difficulty():
   match difficultyQuestion:
      case "A":
         veryEasy()
      case "B":
         easy()
      case "C":
         medium()
      case "D":
         difficult()
      case "E":
         veryDifficult()
      case "Q":
         quit()
      case _:
         print("Invalid Letter!\n")

def veryEasy():
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

def easy():
   tries = 5
   guess = random.randint(1,10)
   print(f"You have {tries} tries!")
   while tries > 0:
    question = int(input("Guess a number from 1 to 10: "))
    if question > guess:
     print("You too high !\n")
     tries -= 1
     print(f"You have {tries} tries!")
    elif question < guess:
     print("You are too low !\n")
     tries -= 1
     print(f"You have {tries} tries!\n")
    elif tries == 0:
      print("NO MORE TRIES, GAME OVER!")
      quit()
    else:
     print(f"THE NUMBER {guess} IS CORRECT, CONGRATULATIONS !!!")
     break
   print("NO MORE TRIES, GAME OVER!")
   quit() 

def medium():
   tries = 5
   guess = random.randint(1,100)
   print(f"You have {tries} tries!")
   while tries > 0:
    question = int(input("Guess a number from 1 to 100: "))
    if question > guess:
     print("You too high !\n")
     tries -= 1
     print(f"You have {tries} tries!")
    elif question < guess:
     print("You are too low !\n")
     tries -= 1
     print(f"You have {tries} tries!\n")
    elif tries == 0:
      print("NO MORE TRIES, GAME OVER!")
      quit()
    else:
     print(f"THE NUMBER {guess} IS CORRECT, CONGRATULATIONS !!!")
     break
   print("NO MORE TRIES, GAME OVER!")
   quit()

def difficult():
   tries = 8
   guess = random.randint(1,500)
   print(f"You have {tries} tries!")
   while tries > 0:
    question = int(input("Guess a number from 1 to 500: "))
    if question > guess:
     print("You too high !\n")
     tries -= 1
     print(f"You have {tries} tries!")
    elif question < guess:
     print("You are too low !\n")
     tries -= 1
     print(f"You have {tries} tries!\n")
    elif tries == 0:
      print("NO MORE TRIES, GAME OVER!")
      quit()
    else:
     print(f"THE NUMBER {guess} IS CORRECT, CONGRATULATIONS !!!")
     break 
   print("NO MORE TRIES, GAME OVER!")
   quit()

def veryDifficult():
   tries = 9
   guess = random.randint(1,1000)
   print(f"You have {tries} tries!")
   while tries > 0:
    question = int(input("Guess a number from 1 to 1000: "))
    if question > guess:
     print("You too high !\n")
     tries -= 1
     print(f"You have {tries} tries!")
    elif question < guess:
     print("You are too low !\n")
     tries -= 1
     print(f"You have {tries} tries!\n")
    else:
     print(f"THE NUMBER {guess} IS CORRECT, CONGRATULATIONS !!!")
     break 
   print("NO MORE TRIES, GAME OVER!")
   quit()


while True:
 print("Welcome to guess the number game!")
 print("The diffulties are:\n\n (A)Very easy: Unlimited trials: 1 to 10 \n (B)Easy: 5 tries: 1 to 10 \n (C)Medium: 5 tries, 1 to 100 \n (D)Difficult: 8 tries, 1 to 500 \n (E)Very difficult: 9 tries, 1 to 1000 \n (Q)quit")
 print("")
 difficultyQuestion = input("What Difficulty will you choose?\n").upper()

 difficulty()

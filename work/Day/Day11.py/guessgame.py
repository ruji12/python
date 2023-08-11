logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
import random
print(logo)
random_integer=random.randint(1,100)
# print(random_integer)
print("Welcome to the number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose=input(" Choose a difficulty.Type 'easy'or 'hard':")
# attempt_number = 0
if choose ==  "hard":
    attempt_number = 5
else:
    attempt_number = 10


if choose=='easy':
    def easy_level():
        global attempt_number
        while attempt_number>=1:
            print(f"You  have {attempt_number} attempts remaining to guess the number .")
            guess=int(input("Make a guess :"))
            attempt_number =attempt_number-1
            if guess==random_integer:
                print("Congratulations you gues it right!!")
            elif guess!=random_integer and guess>50:
                print("too high.")
                print("Guess again.")
                # easy_level()
            elif guess!=random_integer and guess<30:
                print("too low.")
                print("Guess again.")
                # easy_level()
        print("Please try again.You have no guesses left!")
    easy_level()

if choose=='hard':
    def hard_level():
        global attempt_number
        while attempt_number>=1:
            print(f"You  have {attempt_number} attempts remaining to guess the number .")
            guess=int(input("Make a guess :"))
            attempt_number = attempt_number-1
            if guess==random_integer:
                print("Congratulations you guess it right!!")
                break
            elif guess!=random_integer and guess>60:
                print("too high.")
                print("Guess again.")
                # hard_level()
            elif guess!=random_integer and guess<30:
                print("too low.")
                print("Guess again.")
                # hard_level()
        print("All of your chances are mistake.Please try again!")
    hard_level()



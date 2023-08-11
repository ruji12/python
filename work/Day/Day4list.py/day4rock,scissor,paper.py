rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]




user_choice=int(input("what do you choose?Type 0 for Rock,1for paper or 2 for Scissors"))
print(game_images[user_choice])

    


import random
computer_choice=random.randint(0,2)
print(f"computer's choice is {computer_choice}")
print(game_images[computer_choice])



if (user_choice==0) and (computer_choice == 1):
    print("you lose!")

elif (user_choice==0) and( computer_choice == 2):
    print("you win!")


elif (user_choice==1) and (computer_choice == 0):
    print("you win!")


elif (user_choice==1) and (computer_choice == 2):
    print("you lose!")

elif (user_choice==2) and (computer_choice == 0):
    print("you lose!")

elif (user_choice==2) and (computer_choice == 1):
    print("you win!")

elif user_choice == computer_choice:
    print("it's a draw")
import random
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

scisssors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock,paper,scisssors]
user_choice = int(input("What do you choose? 0 for rock 1 for paper and 2 for scissors.\n"))

if user_choice >=3 or user_choice < 0 :
 print("You typed an invalid number,you lost!")
else :
 print(game_image[user_choice])

computer_choice=random.randint(0,2)
print("computer choise")
print(game_image[computer_choice])

if user_choice == 0 and computer_choice == 2:
 print("You win@@@")
elif computer_choice == 0 and user_choice == 2:
 print("You lose***")
elif computer_choice > user_choice:
 print("You win!")
elif computer_choice == user_choice :
 print("Its a draw^^")
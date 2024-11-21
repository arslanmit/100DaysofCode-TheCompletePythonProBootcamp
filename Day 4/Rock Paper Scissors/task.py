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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]

user_choice=int(input('0 Rock, 1 Paper,2, Scissors\n'))

print(print(game[user_choice]))
computer_choice=random.randint(0,2)

print(computer_choice)
print(game[computer_choice])


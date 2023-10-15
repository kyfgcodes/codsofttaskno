#A game of rock paper scissors

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
 
user = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
computer = random.randint(0,2)
 
choices = [rock, paper, scissors]
 
print(choices[user])
print("The computer chose:")
print(choices[computer])
 
if ((user + 1) % 3 == computer):
  print("You lost!")
elif(user == computer):
  print("It's a tie!")
else:
  print("You win!")
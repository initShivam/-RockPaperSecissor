print("Rock Paper Scissors Game")
import random

rock = """

rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """

paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissor = """

scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


list1 = [rock, paper, Scissor]
user_1 = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
user_value = list1[user_1]
print("You chose:", user_value)


#code which converte the computer input to list value
user_2 = random.randint(0,2)
# print("Computer chose:", user_2)
vaules = list1[user_2] 
print("Computer Chose : ",vaules)



if user_1 == user_2:
    print("It's a tie!")

elif user_1 == 0 and user_2 == 1:
    print("Paper covers Rock! You lose!")

elif user_1 == 0 and user_2 == 2:
    print("Rock crushes Scissors! You win!")

elif user_1 == 1 and user_2 == 0:
    print("Paper covers Rock! You win!")

elif user_1 == 1 and user_2 == 2:
    print("Scissors cuts Paper! You lose!")

elif user_1 == 2 and user_2 == 0:
    print("Rock crushes Scissors! You lose!")

elif user_1 == 2 and user_2 == 1:
    print("Scissors cuts Paper! You win!")

else:
    print("Invalid input!")



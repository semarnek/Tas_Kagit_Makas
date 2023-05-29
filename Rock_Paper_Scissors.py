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


choose_list = [rock, paper, scissors]

human_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
human_choose = int(human_choose)

computer_choose = random.randint(0, 2)

print(choose_list[human_choose])

print("Computer chose:")
print(choose_list[computer_choose])


if human_choose == computer_choose:
  print("It's a draw")

elif human_choose == 0 and computer_choose == 1:
  print("You lose")

elif human_choose == 0 and computer_choose == 2:
  print("You win")

elif human_choose == 1 and computer_choose == 0:
  print("You win")

elif human_choose == 1 and computer_choose == 2:
  print("You lose")

elif human_choose == 2 and computer_choose == 0:
  print("You lose")

elif human_choose == 2 and computer_choose == 1:
  print("You win")
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

#Write your code below this line 👇
choice=int(input("What do you choose?Type 0 for rock,1 for scissors,2 for paper"))
computer_choice=random.randint(0,2)
if choice==0:
    print(rock)
    if computer_choice==0:
        print(rock)
        print("It is a draw")
    elif computer_choice==1:
        print(scissors)
        print("You win")
    else:
        print(paper)
        print("You lose")
elif choice==1:
    print(scissors)
    if computer_choice==0:
        print(rock)
        print("You lose")
    elif computer_choice==1:
        print(scissors)
        print("It is a draw")
    else:
        print(paper)
        print("You win!")
else:
    print(paper)
    if computer_choice==0:
        print(rock)
        print("You win")
    elif computer_choice==1:
        print(scissors)
        print("You lose")
    else:
        print(paper)
        print("It is a draw")
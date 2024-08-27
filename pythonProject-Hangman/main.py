import random
from art import logo
print(logo)
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6
# print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(word_length):
    display += "_"

while '_' in display and lives>0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You've already guessed {guess}")
    if guess in chosen_word:
     for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    else:
            lives-=1
            print(f"Wrong choice!!,you have {lives} lives left")
            from art import stages
            print(stages[lives])
    print(display)
if lives==0:
  print(f"You lose.Word was {chosen_word}")
else:
  print("You win")
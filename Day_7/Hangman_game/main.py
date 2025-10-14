# import random

# word_list = ["apparel", "resistance", "cardinal", "phlegm", "optimist"]
# chosen_word = random.choice(word_list)

# placeholder = ""
# word_length = len(chosen_word)

# for position in range(word_length):
#   placeholder += "_"
# print(placeholder)
 
# user_guess = input("Guess a letter ").lower().strip()

# wrong_guess = False
# display = []

# attempts = 3

# while wrong_guess not True:
  
#   while user_guess in chosen_word:
#     for letter in chosen_word:
#       if letter == user_guess:
#         display += letter
        
#       else:
#         display += "_"
#         trials -= attempts
#         print(f"Try again! You have {trials} more chance(s)")

# print(display)
import random
import os
import urllib.request#makes a HTTP request to the MIT website
word_file = "wordlist.txt"
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

# Download the word list only if the file doesn't exist
if not os.path.exists(word_file):
    print("Downloading word list...")
    try:
        response = urllib.request.urlopen(word_site)
        txt = response.read().decode()
        with open(word_file, "w", encoding="utf-8") as f:
            f.write(txt)
        print("Word list downloaded successfully!")
    except:
        print("Could not download word list. Using default words...")
        word_list = ["python", "hangman", "programming", "developer", "computer"]
else:
    # Read word list from file
    try:
        with open(word_file, "r", encoding="utf-8") as f:
            word_list = [word.strip().lower() for word in f 
                        if word.strip().isalpha() and len(word.strip()) >= 4]
    except:
        word_list = ["python", "hangman", "programming", "developer", "computer"]

chosen_word = random.choice(word_list)
attempts = 6

# Initialize display list with underscores
# display = ["_" for _ in range(len(chosen_word))]
display = ["_"] * len(chosen_word)
game_over = False

print("Welcome to Hangman!")
print(" ".join(display))


while not game_over:
    user_guess = input("Guess a letter: ").lower().strip()
    
    if not user_guess.isalpha() or len(user_guess) != 1:
      print("Please enter a single letter!")
      continue

    if user_guess in display:
      print("You've already guessed that letter.")
      continue

    if user_guess in chosen_word:
      for position in range(len(chosen_word)):
        if chosen_word[position] == user_guess:
          display[position] = user_guess
    else:
      attempts -= 1
      print(f"Wrong guess! You have {attempts} lives left.")
    
    print(" ".join(display))
    
    # Check win condition
    if "_" not in display:
        game_over = True
        print("You win!")
    
    # Check lose condition
    if attempts == 0:
        game_over = True
        print(f"You lose! The word was {chosen_word}")

  
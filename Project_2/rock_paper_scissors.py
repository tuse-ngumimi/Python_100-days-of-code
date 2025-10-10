import random

print("Welcome To The Rock Paper Scissors Game! ")
name : str = input("What should I call you? ").title()
to_play = input(f"Nice to meet you {name}! Do you want to play? (yes/no) ").lower().strip()


if to_play in ["yes", "y"]:
    print(f"Let's play {name}! 🎉")

    while True:
        
       player_choice : str = input("Choose: rock, paper, or scissors? ").lower().strip()
       if player_choice == "rock":
          print("""
      _______
      ---'   ____)
            (_____)
            (_____)
             (____)
      ---.__(___)
                """)
       elif player_choice == "paper":
          print("""
    _______
      ---'   ____)____
                ______)
                _______)
                _______)
      ---.__________)
                  """)
       elif player_choice == "scissors":
          print("""
    _______
      ---'   ____)____
                ______)
             __________)
             (____)
      ---.__(___)
                """)
          

        # Validate player input
       if player_choice not in ["rock", "paper","scissors"] :
          print("Invalid choice! Please select either rock, paper, or scissors.")
          continue
            
        # Computer choice
       computer_choice = random.choice(["rock", "paper", "scissors"])
        
       print(f"\n{name} chose: {player_choice.title()} 🕹️")
       print(f"Computer chose: {computer_choice.title()} 🤖")

       if player_choice == computer_choice:
          print("It's a tie")
       elif player_choice == "rock" and computer_choice == "paper":
          print(f"Rock covers paper! {name} wins!")
       elif player_choice == "scissors" == computer_choice == "paper":
          print(f"Scissors cuts paper! {name} wins!")
       elif player_choice == "rock" == computer_choice == "scisssors":
          print(f"Rock crushes scissors! {name} wins!")

       else:
          print(f"Computer wins! Better luck next time, {name}! 🤖")
    
       pass
       play_again = input("Would you like to play again? (yes/no) ")
       if play_again not in ["yes" or "y"]:
         break
       
    print(f"Thanks for playing {name}! Till next time!")

    
elif to_play in ["no", "n"]:
    print(f"Goodbye {name}! See you soon! ") 

else:
    print("I didn't understand that. Please run the program again and answer 'yes' or 'no'.")


          

      



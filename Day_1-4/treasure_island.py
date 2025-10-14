def treasure_island():
    print('''
*******************************************************************************
          |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
    ''')
    print("=" * 50)
    print("     Welcome to the Treasure Island Game 🏝️")
    print(" ✨ Your Mission is to find the Treasure ✨")
    print("=" * 50)
    print()

   
    direction = input("""You're stuck at a two-way tunnel.
What way do you choose (left or right)? """).lower().strip()

    if direction == "right":
        print("💀 You have fallen into a hole and can't climb out!")
        print("Game Over! 💀")
        return 
    
    elif direction == "left":
        print("🌊 You chose the left path and made it through the tunnel safely!")
        
        choice_two = input("\nThere's a river ahead. Do you want to swim or wait for a boat? (swim or wait) ").lower().strip()
        
        if choice_two == "swim":
            print("🐋 You have been swallowed by a whale! Goodbye")
            print("Game Over! 💀")
            return
        
        elif choice_two == "wait":
            print("⛵ A friendly boatman arrives and takes you safely across the river!")
          
            choice_three = input("\n🚪 You've found three doors. Choose wisely. (red or blue or yellow) ").lower().strip()
            
            if choice_three == "red":
                print("🔥 Burned by fire. Game over! 💀")
                return
            
            elif choice_three == "blue":
                print("🐺 Eaten by beasts. Game over! 💀")
                return
            
            elif choice_three == "yellow":
                print("🏆 Congratulations! You've found the treasure! You win! 🎉")
                print("💰 The golden treasure chest is yours! 💰")
                return
            
            else:
                print("❌ Invalid choice! The ground opened up and swallowed you!")
                print("Game Over! 💀")
                return
        
        else:
            print("❌ Invalid choice! The current sweeps you away.")
            print("Game Over! 💀")
            return
    
    else:
        print("❌ Invalid direction! You wander around confused and get lost.")
        print("Game Over! 💀")
        return


def play_again():
    """Ask if the player wants to play again."""
    while True:
        play_again_choice = input("\n Do you want to play again? (yes or no) ").lower().strip()
        if play_again_choice == "y" or play_again_choice == "yes":
            return True
        elif play_again_choice == "n" or play_again_choice == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main game loop with replay functionality."""
    print("🌟 Welcome to the Adventure! 🌟")
    
    while True:
        treasure_island()
        
        if not play_again():
            print("\n👋 Thanks for playing! Goodbye! 👋")
            break
        
        print("\n" + "="*50)
        print("🔄 Starting a new adventure... 🔄")
        print("="*50)


if __name__ == "__main__":
    main()
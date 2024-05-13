from utils.user_manager import UserManager
from utils.dice_game import DiceGame
import sys

def main():
    while True:
        print("\nWelcome to Dice Roll Game")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please enter your command: ")
        try:
            choice = int(choice)
            if choice == 1:
                if UserManager().register():
                    print("Registration successful.")
                else:
                    print("Registration cancelled.")
            elif choice == 2:
                username = UserManager().login()
                if username:
                    DiceGame(UserManager).menu(username)
                else:
                    print("Login cancelled.")
            elif choice == 3:
                sys.exit()
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
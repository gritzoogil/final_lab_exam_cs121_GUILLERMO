from utils.user_manager import UserManager
import sys

def main():
    print("\nWelcome to Dice Roll Game")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    while True:
        choice = input("Please enter your command: ")
        try:
            choice = int(choice)
            if choice == 1:
                UserManager().register()
                break
            elif choice == 2:
                UserManager().login()
                break
            elif choice == 3:
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
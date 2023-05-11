#Login: skylearn
#Password: root

from datetime import datetime
from colorama import init, Fore, Style
from user_functions import (register_new_user, login , load_user_data , save_user_data)
from user_actions import handle_deposit, top_up_main_balance, withdraw_main_balance, display_balance, display_transaction_history, deposit_options , transfer

# Initialize the colorama library
init()

# Print a welcome message
print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to the Bank of Jusan!{Style.RESET_ALL}")
print(f"{Fore.RED}Attention! Please use only numeric value when you write your answer{Style.RESET_ALL}")

def main():
  # Initialize user data
  user_data = load_user_data()

  # Initialize user session
  user_session = None

  while True:
    if user_session is not None:
      print_main_menu()
      user_choice = get_user_input("Choose an action: ", int)

      if user_choice == 1:  # Deposit
        handle_deposit(deposit_options(), get_user_transaction_history(user_data, user_session), get_user_balance(user_data, user_session))
      elif user_choice == 2:  # Top up main balance
        top_up_main_balance(user_data, user_session)
      elif user_choice == 3:  # Withdraw from main balance
        withdraw_main_balance(user_data, user_session)
      elif user_choice == 4:  # Display balance
        display_balance(get_user_balance(user_data, user_session))
      elif user_choice == 5:  # Transaction history
        display_transaction_history(user_data, user_session)
      elif user_choice == 6:  # Transfer
        transfer(user_data, user_session)
      elif user_choice == 7:  # Log out
        user_session = None
    else:
      print_login_menu()
      user_choice = get_user_input("Choose an action: ", int)
      if user_choice == 1:  # Login
        user_session = login(user_data)
      elif user_choice == 2:  # Register
        register_new_user(user_data)
      elif user_choice == 3:  # Exit
        break
      save_user_data(user_data)


# Function to get transaction history
def get_user_transaction_history(user_data, user_session):
    return user_data[user_session]['transaction_history']
  
# Function to get user balance
def get_user_balance(user_data, user_session):
    return user_data[user_session]['balance']

# Function to get user input
def get_user_input(prompt , type=str):
  while True:
    try:
      user_input = type(input(prompt))
      return user_input
    except ValueError:
      print("Invalid input. Please try again.")


# Function to print the main menu
def print_main_menu():
    print("Main Menu")
    print("1. Deposit")
    print("2. Top up main balance")
    print("3. Withdraw from main balance")
    print("4. Check balance")
    print("5. Transaction history")
    print("6. Transfer")
    print("7. Log out")

# Function to print the login menu
def print_login_menu():
    print("1. Login")
    print("2. Register")
    print("3. Exit")
  
if __name__ == "__main__":
    main()
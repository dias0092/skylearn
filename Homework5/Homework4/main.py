#Login: skylearn
#Password: root

from colorama import init, Fore, Style
from user_functions import load_user_data , save_user_data , login , register_new_user 
from user_actions import get_user_balance, get_user_input , deposit_options , transfer , top_up_main_balance , get_user_transaction_history, handle_deposit , withdraw_main_balance, display_balance , display_transaction_history

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
      user_session = logged_in_menu(user_data, user_session)
    else:
      user_session = logged_out_menu(user_data)

  save_user_data(user_data)


# Funtion to choose in main menu
def logged_in_menu(user_data, user_session):
  print_main_menu()
  
  user_choice = get_user_input("Choose an action: ", int)
  balance = get_user_balance(user_data, user_session)

  if user_choice == 1:  # Deposit
    
    options = deposit_options()
    transaction_history = get_user_transaction_history(user_data, user_session)
  
    handle_deposit(options, transaction_history, balance)
  elif user_choice == 2:  # Top up main balance
    top_up_main_balance(user_data, user_session)
  elif user_choice == 3:  # Withdraw from main balance
    withdraw_main_balance(user_data, user_session)
  elif user_choice == 4:  # Display balance
    display_balance(balance)
  elif user_choice == 5:  # Transaction history
    display_transaction_history(user_data, user_session)
  elif user_choice == 6:  # Transfer
    transfer(user_data, user_session)
  elif user_choice == 7:  # Log out
    return None
  
  return user_session


# Funtion to choose in login menu
def logged_out_menu(user_data):
  print_login_menu()

  user_choice = get_user_input("Choose an action: ", int)
  if user_choice == 1:  # Login
    return login(user_data)
  elif user_choice == 2:  # Register
    register_new_user(user_data)
  elif user_choice == 3:  # Exit
    exit(0)

  return None
  
# Function to print the main menu
def print_main_menu():
    print("\nMain Menu\n")
    print("1. Deposit")
    print("2. Top up main balance")
    print("3. Withdraw from main balance")
    print("4. Check balance")
    print("5. Transaction history")
    print("6. Transfer")
    print("7. Log out\n")

# Function to print the login menu
def print_login_menu():
    print("\n1. Login")
    print("2. Register")
    print("3. Exit\n")
  
if __name__ == "__main__":
    main()




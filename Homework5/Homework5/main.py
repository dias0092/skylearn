#Login: skylearn
#Password: root

from colorama import init, Fore, Style
from user_functions import (
    load_user_data, save_user_data, login, register_new_user
)
from user_actions import (
    get_user_balance, get_user_input, deposit_options, transfer, 
    top_up_main_balance, get_user_transaction_history, handle_deposit, 
    withdraw_main_balance, display_balance, display_transaction_history
)

# Initialize the colorama library
init()

# Print a welcome message
print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to the Bank of Jusan!{Style.RESET_ALL}")
print(f"{Fore.RED}Attention! Please use only numeric value when you write your answer{Style.RESET_ALL}")

def main():
    user_data = load_user_data()
    user_session = None
    
    while True:
        user_session = logged_in_menu(user_data, user_session) if user_session else logged_out_menu(user_data)
    
    save_user_data(user_data)
  
# Funtion to choose in main menu
def logged_in_menu(user_data, user_session):
    print_main_menu()
    user_choice = get_user_input("Choose an action: ", int)
    balance = get_user_balance(user_data, user_session)

    actions = {
        1: lambda: handle_deposit(deposit_options(), get_user_transaction_history(user_data, user_session), balance),  # Deposit
        2: lambda: top_up_main_balance(user_data, user_session), # Top up main balance
        3: lambda: withdraw_main_balance(user_data, user_session), # Withdraw from main balance
        4: lambda: display_balance(balance), # Display Balance
        5: lambda: display_transaction_history(user_data, user_session), # Display History
        6: lambda: transfer(user_data, user_session), # Transfer
        7: lambda: None  # Log out
    }
  
    return actions.get(user_choice, lambda: user_session)()
  
# Funtion to choose in login menu
def logged_out_menu(user_data):
    print_login_menu()

    actions = {
        1: lambda: login(user_data),
        2: lambda: register_new_user(user_data),
        3: lambda: exit(0)
    }
    
    return actions.get(get_user_input("Choose an action: ", int), lambda: None)()

def print_main_menu():
    print("\nMain Menu\n")
    print("1. Deposit")
    print("2. Top up main balance")
    print("3. Withdraw from main balance")
    print("4. Check balance")
    print("5. Transaction history")
    print("6. Transfer")
    print("7. Log out\n")

def print_login_menu():
    print("\n1. Login")
    print("2. Register")
    print("3. Exit\n")
  
if __name__ == "__main__":
    main()
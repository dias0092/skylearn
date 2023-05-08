#Login: skylearn
#Password: root

import getpass
from datetime import datetime
from colorama import init, Fore, Style

# Initialize the colorama library
init()
# Print a welcome message
print(
  f"{Fore.CYAN}{Style.BRIGHT}Welcome to the Bank of Jusan!{Style.RESET_ALL}")
print(
  f"{Fore.RED}Attention! Please use only numeric value when you write your answer{Style.RESET_ALL}"
)

# User credentials and account information
user_data = {
    "skylearn": {
        "password": "root",
        "balance": {"Tenge": 0, "Dollar": 0, "Main": 0},
        "transaction_history": []
    }
}


# Function to register a new user
def register(user_data):
  print("Please enter your registration details.")
  username = input("Username: ")
  if username in user_data:
    print("This username is already taken.")
    return None
  password = getpass.getpass("Password: ")
  user_data[username] = {
        "password": password,
        "balance": {"Tenge": 0, "Dollar": 0, "Main": 0},
        "transaction_history": []
    }
  print(f"Registration successful! Welcome, {username}.")
  return username


# Function to handle user login
def login(user_credentials):
  print("Please log in.")
  username = input("Username: ")
  password = getpass.getpass("Password: ")

  if username in user_credentials and user_credentials[username][
      "password"] == password:
    return username
  else:
    print("Invalid username or password.")
    return None


# Function to display the main menu
def main_menu(logged_in_user, main_balance=None):
    print("Main Menu")
    if logged_in_user and main_balance is not None:
        print(f"Your main balance: {main_balance}")
    print("1. Deposit")
    if logged_in_user:
        print("2. Log out")
    else:
        print("2. Sign in")
    print("3. Register")
    print("4. Check balance")
    print("5. Transaction history")
    if logged_in_user:
        print("6. Withdraw from main balance")
        print("7. Top up main balance")
    print("8. Exit")
    choice = int(input("Select an option: "))
    return choice

# Function to handle main balance withdrawal
def withdraw_main_balance(username, user_data):
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
    print(f"Your main balance: ₸{user_data[username]['balance']['Main']}")
    withdrawal_amount = int(input("Enter the amount to withdraw: ₸"))
    if withdrawal_amount <= user_data[username]['balance']['Main']:
        user_data[username]['balance']['Main'] -= withdrawal_amount
        user_data[username]['transaction_history'].append(("Withdrawal", withdrawal_amount, "Main", current_time))
        print(f"Withdrawal successful! Your new main balance: ₸{user_data[username]['balance']['Main']}")
    else:
        print("Insufficient balance. Please try again.")
# Function to handle main balance top up
def top_up_main_balance(username, user_data):
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
    print(f"Your current main balance: ₸{user_data[username]['balance']['Main']}")
    top_up_amount = int(input("Enter the amount to top up: ₸"))
    if top_up_amount > 0:
        user_data[username]['balance']['Main'] += top_up_amount
        user_data[username]['transaction_history'].append(("Top Up", top_up_amount, "Main", current_time))
        print(f"Top-up successful! Your new main balance: ₸{user_data[username]['balance']['Main']}")
    else:
        print("Invalid top-up amount. Please try again.")
# Function to handle deposit options
def deposit_options():
  print("What deposit do you want?")
  print(
    "1. You have 10% interest every year, and at the end of each year, your interest rate increases by 5%. The currency of this deposit is Tenge ₸."
  )
  print(
    "2. You get 5% interest every month, but this deposit can only be open for 1 year. The currency of this deposit is Dollar $."
  )
  answer = int(input("Your answer: "))
  return answer


# Function to handle analytics
def deposit_analytics(answer, balance):
  if answer == 1:
    years = int(input("Enter the number of years for analytics: "))
    initial_interest = 10
    estimated_balance = balance['Tenge']
    for i in range(years):
      interest_rate = initial_interest + i * 5
      estimated_balance += estimated_balance * interest_rate / 100
    print(
      f"Your estimated balance after {years} years: ₸{estimated_balance:.2f}")
  elif answer == 2:
    months = int(
      input("Enter the number of months for analytics (maximum 12): "))
    if months > 12:
      print("The maximum number of months for this deposit is 12.")
      months = 12
    estimated_balance = balance['Dollar']
    interest_rate = 5
    for i in range(months):
      estimated_balance += estimated_balance * interest_rate / 100
    print(
      f"Your estimated balance after {months} months: ${estimated_balance:.2f}"
    )
  else:
    print("Invalid option. Please try again.")


# Function to handle deposits and transaction history
def handle_deposit(answer, transaction_history, balance):
  current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
  if answer == 1:
    # Tenge deposit option
    print("1. Analytics")
    print("2. Withdrawal")
    action_choice = int(input("Choose an action: "))
    if action_choice == 1:
      deposit_analytics(answer, balance)
    elif action_choice == 2:
      print(f"Your balance for this deposit: ₸{balance['Tenge']}")
      income = int(input("How much do you want to deposit: ₸"))
      balance['Tenge'] += income
      transaction_history.append(("Deposit", income, "Tenge", current_time))
      return income
    else:
      print("Invalid option. Please try again.")
      return None
  elif answer == 2:
    # Dollar deposit option
    print("1. Analytics")
    print("2. Withdrawal")
    action_choice = int(input("Choose an action: "))
    if action_choice == 1:
      deposit_analytics(answer, balance)
    elif action_choice == 2:
      print(f"Your balance for this deposit: ${balance['Dollar']}")
      income = int(input("How much do you want to deposit: $"))
      balance['Dollar'] += income
      transaction_history.append(("Deposit", income, "Dollar", current_time))
      return income

  # Function to display balance
def display_balance(balance):
  print(f"Your balance for Tenge deposit: ₸{balance['Tenge']}")
  print(f"Your balance for Dollar deposit: ${balance['Dollar']}")


  # Function to display transaction history
def display_transaction_history(user_data, username):
    transaction_history = user_data[username]['transaction_history']
    if not transaction_history:
        print("No transactions found.")
    else:
        for transaction in transaction_history:
            action, amount, currency, time = transaction
            print(f"{action}: {currency} {amount} at {time}")

def main():
    logged_in_user = None

    while True:
        if logged_in_user:
            menu_choice = main_menu(logged_in_user, user_data[logged_in_user]['balance']['Main'])
        else:
            menu_choice = main_menu(logged_in_user)
        
        if menu_choice == 1:  # Deposit
            if logged_in_user:
                deposit_choice = deposit_options()
                handle_deposit(deposit_choice, user_data, logged_in_user)
            else:
                print("You need to be logged in to deposit.")
        elif menu_choice == 2:  # Sign in / Log out
            if not logged_in_user:
                logged_in_user = login(user_data)
            else:
                logged_in_user = None
                print("You have logged out.")
        elif menu_choice == 3:  # Register
            register(user_data)
        elif menu_choice == 4:  # Check balance
            if logged_in_user:
                display_balance(user_data, logged_in_user)
            else:
                print("You need to be logged in to check the balance.")
        elif menu_choice == 5:  # Transaction history
          if logged_in_user:
            display_transaction_history(user_data, logged_in_user)
          else:
            print("You need to be logged in to view transaction history.")
        elif menu_choice == 6:  # Withdraw from main balance
            if logged_in_user:
                withdraw_main_balance(logged_in_user, user_data)
            else:
                print("You need to be logged in to withdraw from your main balance.")
        elif menu_choice == 7:  # Top up main balance
            if logged_in_user:
                top_up_main_balance(logged_in_user, user_data)
            else:
                print("You need to be logged in to top up your main balance.")
        elif menu_choice == 8:  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        

if __name__ == "__main__":
    main()
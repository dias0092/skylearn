from datetime import datetime

# Function to handle main balance withdrawal
def withdraw_main_balance(user_data, username):
    """
    Handles the withdrawal of the user's main balance.

    Parameters:
    user_data (dict): A dictionary containing all user data.
    username (str): The username of the user making the withdrawal.

    Returns:
    None
    """
  
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
    print(f"\nYour main balance: ₸{user_data[username]['balance']['main']}")
    withdrawal_amount = get_user_input("Enter the amount to withdraw: ₸", int)
    if withdrawal_amount <= user_data[username]['balance']['main']:
        user_data[username]['balance']['main'] -= withdrawal_amount
        user_data[username]['transaction_history'].append(("Withdrawal", withdrawal_amount, "main", current_time))
        print(f"Withdrawal successful! Your new main balance: ₸{user_data[username]['balance']['main']}")
    else:
        print("Insufficient balance. Please try again.")


# Function to handle main balance top up
def top_up_main_balance(user_data, username):
  
    """
    Handles topping up the user's main balance.

    Parameters:
    user_data (dict): A dictionary containing all user information.
    username (str): The username of the user.
    """
  
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
    print(f"\nYour main balance: ₸{user_data[username]['balance']['main']}")
    top_up_amount = get_user_input("Enter the amount to top up: ₸", int)
    if top_up_amount > 0:
        user_data[username]['balance']['main'] += top_up_amount
        user_data[username]['transaction_history'].append(("Top Up", top_up_amount, "main", current_time))
        print(f"Top-up successful! Your new main balance: ₸{user_data[username]['balance']['main']}")
    else:
        print("Invalid top-up amount. Please try again.")


# Function to handle transfer
def transfer(user_data, sender_username):
  
    """
    Handles the transfer of balance from the sender to the recipient.

    Parameters:
    user_data (dict): A dictionary containing all user information.
    sender_username (str): The username of the sender.
    """
  
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
  
    recipient_username = input("\nEnter recipient username: ")
    if recipient_username not in user_data:
        print("Recipient username not found.")
        return
    transfer_amount = get_user_input("Enter the amount to transfer: ", int)
    if transfer_amount <= 0:
        print("Invalid transfer amount.")
        return

    if transfer_amount > user_data[sender_username]['balance']['main']:
        print("Insufficient balance. Please try again.")
        return

    # Update sender balance
    user_data[sender_username]['balance']['main'] -= transfer_amount
    user_data[sender_username]['transaction_history'].append(("Transfer to " + recipient_username, transfer_amount, "main", current_time))

    # Update recipient balance
    user_data[recipient_username]['balance']['main'] += transfer_amount
    user_data[recipient_username]['transaction_history'].append(("Transfer from " + sender_username, transfer_amount, "main", current_time))

    print("Transfer successful!")


# Function to handle deposit options
def deposit_options():
  print("\nWhat deposit do you want?")
  print(
    "1. 10% , each year your interest +5%. The currency is Tenge ₸."
  )
  print(
    "2. 5% every mounth, deposit can only be open for 1 year. The currency is Dollar $."
  )
  answer = get_user_input("\nYour answer: ",int)
  return answer

# Function to handle analytics
def deposit_analytics(answer, balance):
  
  """
  Handles the calculation and display of estimated balance based on the chosen deposit option.

  Parameters:
  answer (int): The chosen deposit option.
  balance (dict): The current balance of the user.
  """

  if answer == 1:
    years = get_user_input("\nEnter the number of years for analytics: ", int)
    initial_interest = 10
    estimated_balance = balance['tenge']
    for i in range(years):
      interest_rate = initial_interest + i * 5
      estimated_balance += estimated_balance * interest_rate / 100
    print(
      f"Your estimated balance after {years} years: ₸{estimated_balance:.2f}")
  elif answer == 2:
    months = get_user_input("\nEnter the number of months for analytics (maximum 12): ",int)
    if months > 12:
      print("The maximum number of months for this deposit is 12.")
      months = 12
    estimated_balance = balance['dollar']
    interest_rate = 5
    for i in range(months):
      estimated_balance += estimated_balance * interest_rate / 100
    print(
      f"\nYour estimated balance after {months} months: ${estimated_balance:.2f}"
    )
  else:
    print("Invalid option. Please try again.")


# Function to handle deposits and transaction history
def handle_deposit(answer, transaction_history, balance):

  """
  Handles the deposit action based on the chosen deposit option.

  Parameters:
  answer (int): The chosen deposit option.
  transaction_history (list): The transaction history of the user.
  balance (dict): The current balance of the user.
  """
  
  current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
  if answer == 1:
    
    # Tenge deposit option
    print("\n1. Analytics")
    print("2. Deposit\n")
    action_choice = get_user_input("Choose an action: ", int)
    if action_choice == 1:
      deposit_analytics(answer, balance)
    elif action_choice == 2:
      print(f"Your balance for this deposit: ₸{balance['tenge']}")
      income = int(input("How much do you want to deposit: ₸"))
      balance['tenge'] += income
      transaction_history.append(("deposit", income, "tenge", current_time))
      return income
    else:
      print("Invalid option. Please try again.")
      return None
  elif answer == 2:
    
    # Dollar deposit option
    print("\n1. Analytics")
    print("2. Deposit\n")
    action_choice = get_user_input("Choose an action: ", int)
    if action_choice == 1:
      deposit_analytics(answer, balance)
    elif action_choice == 2:
      print(f"\nYour balance for this deposit: ${balance['dollar']}")
      income = int(input("How much do you want to deposit: $"))
      balance['dollar'] += income
      transaction_history.append(("deposit", income, "dollar", current_time))
      return income


# Function to display balance
def display_balance(balance):
  print(f"\nYour balance for Main: ₸{balance['main']}")
  print(f"Your balance for Tenge deposit: ₸{balance['tenge']}")
  print(f"Your balance for Dollar deposit: ${balance['dollar']}")


# Function to display transaction history
def display_transaction_history(user_data, username):
    transaction_history = user_data[username]['transaction_history']
  
    if not transaction_history:
      print("No transactions found.")
    else:
      print("\nTransaction history:")
      for transaction in transaction_history:
        action, amount, currency, time = transaction
        print(f"{action}: {currency} {amount} at {time}")



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





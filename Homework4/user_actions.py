from datetime import datetime

# Function to handle main balance withdrawal
def withdraw_main_balance(user_data, username):
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
    print(f"Your main balance: ₸{user_data[username]['balance']['main']}")
    withdrawal_amount = int(input("Enter the amount to withdraw: ₸"))
    if withdrawal_amount <= user_data[username]['balance']['main']:
        user_data[username]['balance']['main'] -= withdrawal_amount
        user_data[username]['transaction_history'].append(("Withdrawal", withdrawal_amount, "main", current_time))
        print(f"Withdrawal successful! Your new main balance: ₸{user_data[username]['balance']['main']}")
    else:
        print("Insufficient balance. Please try again.")


# Function to handle main balance top up
def top_up_main_balance(user_data, username):
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
    print(f"Your main balance: ₸{user_data[username]['balance']['main']}")
    top_up_amount = int(input("Enter the amount to top up: ₸"))
    if top_up_amount > 0:
        user_data[username]['balance']['main'] += top_up_amount
        user_data[username]['transaction_history'].append(("Top Up", top_up_amount, "main", current_time))
        print(f"Top-up successful! Your new main balance: ₸{user_data[username]['balance']['main']}")
    else:
        print("Invalid top-up amount. Please try again.")


# Function to handle transfer
def transfer(user_data, sender_username):
    current_time = datetime.now().strftime("%H:%M %d/%m/%Y")
  
    recipient_username = input("Enter recipient username: ")
    if recipient_username not in user_data:
        print("Recipient username not found.")
        return
    transfer_amount = int(input("Enter the amount to transfer: "))
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
    estimated_balance = balance['tenge']
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
    estimated_balance = balance['dollar']
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
    print("2. Deposit")
    action_choice = int(input("Choose an action: "))
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
    print("1. Analytics")
    print("2. Deposit")
    action_choice = int(input("Choose an action: "))
    if action_choice == 1:
      deposit_analytics(answer, balance)
    elif action_choice == 2:
      print(f"Your balance for this deposit: ${balance['dollar']}")
      income = int(input("How much do you want to deposit: $"))
      balance['dollar'] += income
      transaction_history.append(("deposit", income, "dollar", current_time))
      return income



# Function to display balance
def display_balance(balance):
  print(f"Your balance for Main: ₸{balance['main']}")
  print(f"Your balance for Tenge deposit: ₸{balance['tenge']}")
  print(f"Your balance for Dollar deposit: ${balance['dollar']}")


# Function to display transaction history
def display_transaction_history(user_data, username):
    transaction_history = user_data[username]['transaction_history']
  
    if not transaction_history:
      print("No transactions found.")
    else:
      print("Transaction history:")
      for transaction in transaction_history:
        action, amount, currency, time = transaction
        print(f"{action}: {currency} {amount} at {time}")




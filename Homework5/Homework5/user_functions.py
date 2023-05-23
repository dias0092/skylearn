import getpass
import json

# Function to load user data from a JSON file
def load_user_data():
    """
    Loads user data from a JSON file.

    Returns:
    dict: A dictionary containing all user data. If the file is not found, returns an empty dictionary.
    """
  
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

# Function to save user data to a JSON file
def save_user_data(user_data):
    """
    Saves user data to a JSON file.

    Parameters:
    user_data (dict): A dictionary containing all user data.

    Returns:
    None
    """
  
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

# Function to register a new user
def register_new_user(user_data):
    """
    Registers a new user.

    Parameters:
    user_data (dict): A dictionary containing all user data.

    Returns:
    str: The username of the newly registered user. If the username is taken, returns None.
    """
  
    print("\nPlease enter your registration details.")
    username = input("Username: ")
    if user_data.get(username) != None:
        print("\nThis username is already taken.\n")
        return None
    password = getpass.getpass("Password: ")
    user_data[username] = {
        "password": password,
        "balance": {"tenge": 0, "dollar": 0, "main": 0},
        "transaction_history": []
    }
    print(f"\nRegistration successful! Welcome, {username}.")
    save_user_data(user_data)
    return username

# Function to handle user login
def login(user_data):
    print("\nPlease log in.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if user_data.get(username) and user_data[username]["password"] == password:
      return username
    else:
      print("Invalid username or password.")
      return None
import getpass
import json

# Function to load user data from a JSON file
def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

# Function to save user data to a JSON file
def save_user_data(user_data):
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

# Function to register a new user
def register_new_user(user_data):
    print("Please enter your registration details.")
    username = input("Username: ")
    if user_data.get(username) != None:
        print("This username is already taken.")
        return None
    password = getpass.getpass("Password: ")
    user_data[username] = {
        "password": password,
        "balance": {"tenge": 0, "dollar": 0, "main": 0},
        "transaction_history": []
    }
    print(f"Registration successful! Welcome, {username}.")
    save_user_data(user_data)
    return username

# Function to handle user login
def login(user_data):
    print("Please log in.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if username in user_data and user_data[username]["password"] == password:
      return username
    else:
      print("Invalid username or password.")
      return None
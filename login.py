"""
This module provides a login function to check if the provided username and password are valid.
"""

def login(username, password):
    """
    Check if the provided username and password are valid.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        bool: True if the username and password are correct, False otherwise.
    """
    return bool(username == "admin" and password == "password")

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

if login(username, password):
    print("Login successful")
else:
    print("Invalid username or password")


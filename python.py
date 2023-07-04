def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

if login(username, password):
    print("Login successful")
else:
    print("Invalid username or password")

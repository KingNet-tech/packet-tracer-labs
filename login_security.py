username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "Cyber123!"

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Login failed")

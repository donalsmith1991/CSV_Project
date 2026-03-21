login_data = {"admin": "12345", "user1": "p@ssword"}

attempts = 0
authenticated = False  # We use this "flag" to track if they got in

while attempts < 3 and not authenticated:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Step 1: Check if the username exists
    if username in login_data:
        # Step 2: Check if the password matches that specific user
        if password == login_data[username]:
            print("Login successful! Welcome.")
            authenticated = True # This will stop the loop
        else:
            print("Incorrect password.")
            attempts += 1
    else:
        print("Username not found.")
        attempts += 1

    # Show remaining attempts
    if not authenticated and attempts < 3:
        print(f"Attempts remaining: {3 - attempts}")

if not authenticated:
    print("Too many failed attempts. Access denied.")
valid_passwords = ["python123","secret789","admin000"]
your_guess = input("guess the password: ")
attempts = 0

print(valid_passwords[0]) # for testing purposes, you can remove this line later

# The loop runs as long as the guess is wrong
while your_guess not in valid_passwords:
    # 1. Ask for a new guess INSIDE the loop
    print("wrong password, try again")
    your_guess = input("guess the password: ")
    attempts += 1
    if attempts >=2 and your_guess not in valid_passwords:
        print("too many attempts, try again later")
        break
if your_guess in valid_passwords:
    print("correct password, welcome!")
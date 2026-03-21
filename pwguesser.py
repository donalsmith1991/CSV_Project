password = "python123"
your_guess = input("guess the password: ")
attempts = 0

# The loop runs as long as the guess is wrong
while your_guess != password:
    # 1. Ask for a new guess INSIDE the loop
    print("wrong password, try again")
    your_guess = input("guess the password: ")
    attempts += 1
    if attempts >=2 and your_guess != password:
        print("too many attempts, try again later")
        break
if your_guess == password:
    print("correct password, welcome!")
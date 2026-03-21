password = "python123"
your_guess = input("guess the password: ")

# The loop runs as long as the guess is wrong
while your_guess != password:
    # 1. Ask for a new guess INSIDE the loop
    your_guess = input("guess the password: ")


# 3. This runs only after the loop condition (your_guess != password) becomes False
print("well done")
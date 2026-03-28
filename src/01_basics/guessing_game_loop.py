the_number = 7
your_guess = int(input("guess the number"))
if your_guess == the_number:
    print("well done")
elif your_guess>the_number:
    print("too high")
elif(your_guess<the_number):
    print("too low")
else:
    print("try again")
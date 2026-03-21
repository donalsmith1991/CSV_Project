# Python 6-Week Study Plan: Beginner to NumPy/Pandas

**Context for AI Tutor:** I am a complete beginner learning Python in VS Code. We are executing a 6-week, project-based study plan. Please review my roadmap and current progress below. When you reply, acknowledge where we are and ask me a guiding question to help me complete the "Current Task." Do not give me the final code; guide me step-by-step.

## The 6-Week Project-Based Roadmap
* **Week 1: Python Basics** (Variables, Data Types, Strings, Input/Output) - *Completed*
* **Week 2: Control Flow** (If/Else, For/While Loops) - *In Progress*
* **Week 3: Data Structures** (Lists, Dictionaries, Tuples) - *Upcoming*
* **Week 4: Functions & Modules** (Defining Functions, Scope, Standard Libraries) - *Upcoming*
* **Week 5: Intro to NumPy** (Arrays, Vector Math, Basic Statistics) - *Upcoming*
* **Week 6: Intro to Pandas** (DataFrames, Reading CSVs, Filtering Data) - *Upcoming*

---

## Completed Projects 🏆

### Week 1, Project 1: Tip Calculator
```python
bill = float(input("What is the total? "))
tip = float(input("What percentage tip would you like to give? "))

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount

print(f"your total bill is: ${total_bill:.2f}")
```

### Week 1, Project 2: Mad Libs Story Generator
```python
adj = input("Enter the adjective: ")
noun = input("Enter the noun: ")
past_tense_verb = input("Enter the past tense verb: ")

story = f"the {adj} {noun} {past_tense_verb} over the fence"
print(story)
```

---

## Current Status: In Progress 🚧

### Week 2, Project 3: Number Guessing Game
**Objective:** Teach the program to loop so the player can keep guessing until they win.
**Current Task:** Wrap the existing input and `if`/`elif` logic inside a `while your_guess != the_number:` loop.

**Current Code Draft:**
```python
the_number = 7
your_guess = 0 # Dummy value so the while loop has something to check initially

# TODO: Add the while loop here and indent the code below!

your_guess = int(input("guess the number: "))

if your_guess == the_number:
    print("well done")
elif your_guess > the_number:
    print("too high")
elif your_guess < the_number:
    print("too low")
else:
    print("try again")
```

**Next Step for AI:** Ask me how I plan to apply the `while` loop and indentation to the current code draft.
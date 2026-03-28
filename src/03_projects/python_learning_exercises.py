"""Python learning exercises starter script.
Run with: python python_learning_exercises.py
"""

# 1. Basics

def basics_exercises():
    print("\n--- Basics Exercises ---")

    # 1. Print your name and age with formatted sentence
    name = "Student"
    age = 20
    print(f"Hello, my name is {name} and I am {age} years old.")

    # 2. Add two numbers from user input
    a, b = 7, 5
    print(f"Sum of {a} and {b} is {a+b}")

    # 3. Convert '3.14' to float and multiply by 2
    pi_string = "3.14"
    result = float(pi_string) * 2
    print(f"{pi_string} as float times 2 is {result}")


# 2. Conditionals

def conditionals_exercises():
    print("\n--- Conditionals Exercises ---")

    # 1. Positive/negative/zero
    x = -2
    if x > 0:
        print(f"{x} is positive")
    elif x < 0:
        print(f"{x} is negative")
    else:
        print(f"{x} is zero")

    # 2. Age category
    age = 16
    if age < 13:
        category = "kid"
    elif age <= 17:
        category = "teen"
    else:
        category = "adult"
    print(f"Age {age} -> {category}")

    # 3. Do you like Python? (simulated answer)
    answer = "yes"
    if answer.lower() in ["yes", "y"]:
        print("Great!")
    else:
        print("No problem!")


# 3. Loops and lists

def loops_lists_exercises():
    print("\n--- Loops and Lists Exercises ---")

    # 1. Print 1..10
    print("Numbers 1 to 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

    # 2. Sum list [5, 10, 15]
    values = [5, 10, 15]
    total = 0
    for v in values:
        total += v
    print(f"Sum of {values} is {total}")

    # 3. Build list of evens <= 20
    evens = [n for n in range(1, 21) if n % 2 == 0]
    print(f"Even numbers up to 20: {evens}")


# 4. Functions and files

def double(x):
    return x * 2


def is_palindrome(s):
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]


def functions_files_exercises():
    print("\n--- Functions and Files Exercises ---")

    print("double(6) =", double(6))

    test_strings = ["radar", "Python"]
    for s in test_strings:
        print(f"is_palindrome('{s}') = {is_palindrome(s)}")

    out_path = "exercise_output.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    print(f"Wrote 3 lines to {out_path}")

    with open(out_path, "r", encoding="utf-8") as f:
        print("Read lines:")
        for line in f:
            print(f"  {line.strip()}")


# 5. CSV / text parsing (folder-specific)

def csv_text_exercises():
    print("\n--- CSV/Text Parsing Exercises ---")

    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"words.txt has {len(lines)} lines")
    except FileNotFoundError:
        print("words.txt not found in workspace")

    try:
        from collections import Counter
        with open("romeo.txt", "r", encoding="utf-8") as f:
            content = f.read().lower()
        words = [w.strip("\n.,!?\"'()[])" ) for w in content.split() if w.strip(",.!?\"'()[]")]
        counter = Counter(words)
        top = counter.most_common(3)
        print("Top 3 words in romeo.txt:", top)
    except FileNotFoundError:
        print("romeo.txt not found in workspace")

    try:
        import csv
        with open("testimport.csv", "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                print("Row:", r)
    except FileNotFoundError:
        print("testimport.csv not found in workspace")
    except Exception as e:
        print("Could not read testimport.csv:", e)


if __name__ == "__main__":
    basics_exercises()
    conditionals_exercises()
    loops_lists_exercises()
    functions_files_exercises()
    csv_text_exercises()

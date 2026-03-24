try:
    with open("words.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    # 1. Print the raw list (the "Python view")
    print("Raw list from readlines:")
    print(lines)
    
    # 2. Print line by line (the "Human view")
    print("\nFormatted lines:")
    for line in lines:
        print(line, end="") # We use end="" because lines already have \n
        
except FileNotFoundError:
    print("words.txt not found!")
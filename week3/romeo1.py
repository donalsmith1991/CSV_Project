fh = None

while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break 
    except FileNotFoundError:
        print(f"File not found. Please try again.")

lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"

# Safely open the file
try:
    handle = open(name)
except FileNotFoundError:
    print("File not found:", name)
    quit()

counts = dict()

# Step 1: Read the file and parse the hours
for line in handle:
    line = line.rstrip()
    
    # We only want the lines starting exactly with "From "
    if not line.startswith('From '):
        continue
    
    # Split the line into words
    words = line.split()
    
    # The time is always the 6th item in the list (index 5)
    # Example: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    time_string = words[5]
    
    # Split the time string by the colon ':'
    time_parts = time_string.split(':')
    
    # The hour is the first part (index 0)
    hour = time_parts[0]
    
    # Add the hour to our histogram dictionary
    counts[hour] = counts.get(hour, 0) + 1

# Step 2: Sort the dictionary by hour and print
# .items() gives us a list of (hour, count) tuples. 
# sorted() automatically sorts them by the first item in the tuple (the hour).
for hour, count in sorted(counts.items()):
    print(hour, count)
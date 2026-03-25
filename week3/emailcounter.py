fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found:", fname)
    quit()

counts = dict()

# Step 1: Read the file and populate the dictionary
for line in fh:
    line = line.rstrip()
    
    # We only care about lines that start with exactly "From "
    if not line.startswith('From '):
        continue
    
    words = line.split()
    email = words[1]
    
    # Add the email to the dictionary or increase its count by 1
    counts[email] = counts.get(email, 0) + 1

# Step 2: Find the most prolific committer
max_email = None
max_count = None

for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

# Step 3: Print the final result
print(max_email, max_count)
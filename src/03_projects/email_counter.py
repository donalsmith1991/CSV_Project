fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found:", fname)
    quit()
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1
max_email = None
max_count = None
for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count
print(max_email, max_count)
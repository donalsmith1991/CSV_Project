fhand=open('load.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('from'):
        print(line)


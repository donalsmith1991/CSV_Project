# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
input = fh.read()
print(input)

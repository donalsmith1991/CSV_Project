largest = None
smallest = None
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
    except:
        print('Invalid input')
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print('Maximum:', largest)
print('Minimum:', smallest)

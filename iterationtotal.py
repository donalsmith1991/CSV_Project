count = 0
total = 0.0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + num

if count > 0:
    print(total, count, total / count)
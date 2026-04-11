import re

input_file = 'data/regex_sum_2386935.txt'
with open(input_file, 'r') as hand:
    total_sum = 0
    for line in hand:
        numbers = re.findall('[0-9]+', line)
        for num in numbers:
            total_sum += int(num)

print("The final sum is:", total_sum)

with open(input_file, 'r') as hand:
    print(sum(int(i) for i in re.findall('[0-9]+', hand.read())))
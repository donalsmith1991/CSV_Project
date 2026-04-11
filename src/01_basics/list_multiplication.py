# Lists cannot be multiplied together.
list_a = [1, 2, 3]
list_b = [2, 4, 6]

#list_a * list_b

list_c = []
for i in range(len(list_a)):
    list_c.append(list_a[i] * list_b[i])

print(list_c)
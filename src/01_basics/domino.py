# Create an empty list to store the dominoes
dominoes = []

# Nested loops to generate all combinations (0 to 6)
for left in range(7):
    for right in range(left, 7):
        # Package the numbers as a tuple and add them to the list
        dominoes.append((left, right))

# Print the final list to the screen so you can see the result
print(dominoes)

pips_from_loop = []
#for domino in dominoes:
   # pips_from_loop.append(domino[0] + domino[1])
#print(pips_from_loop)

pips_from_list_comp = [domino[0] + domino[1] for domino in dominoes]

print(pips_from_list_comp)
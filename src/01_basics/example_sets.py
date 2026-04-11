example_a = [1, 2, 2.0, '2']
print(set(example_a))

example_b = ('apple', (1, 2, 2, 2, 3), 2)
set(example_b)
print(set(example_b))



example_d = {'mother', 'hamster', 'father'}
example_d.add('elderberries')
example_d
print(example_d)

example_e = [1.5, frozenset(['a', 'b', 'c']), 1.5]
set(example_e)
print(set(example_e))
# Create a list of tuples, each representing the name, age, and position of a
# player on a basketball team.
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ]

def player_position(team):
    result = []
    for name, age, position in team:
        result.append('Name: {:>19} \nPosition: {:>15}\n'.format(name, position))

    return result

print(player_position(team))
for player in player_position(team):
    print(player)
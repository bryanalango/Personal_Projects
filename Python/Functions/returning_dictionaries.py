def build_person(first_name, last_name):
    """Returns a dictionary of information about person"""
    person = {'first': first_name, 'last': last_name}
    return person


player = build_person(first_name='John', last_name='Muganda')
print(player)


def build_person(first_name, last_name, middle_name = '', age=''):
    """Returns a dictionary of information about person"""
    person = {'first_name': first_name, 'last_name': last_name}
    if middle_name:
        person['middle_name'] = middle_name
    if age:
        person['age'] = age

    return person


player = build_person('bryan', 'otieno', middle_name="Alang'o", age='27')
player_1 = build_person('james', 'clifford', 'opiyo', '37')
print(player_1)
print(player)
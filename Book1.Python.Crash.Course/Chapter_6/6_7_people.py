person01 = {
    'first_name': 'Ragnhild',
    'last_name': 'Friis Tveit',
    'age': 24,
    'city': 'Bergen'
}
person02 = {
    'first_name': 'tristan',
    'last_name': 'gjelletveit',
    'age': 3,
    'city': 'Bergen'
}
person03 = {
    'first_name': 'Osfv',
    'last_name': 'Oseland tveit',
    'age': 30,
    'city': 'Bergen'
}

persons = [person01, person02, person03]

for person in persons:
    print("First name: {}".format(person['first_name'].title()))
    print("Last name: {}".format(person['last_name'].title()))
    print("Age: {}".format(person['age']))
    print("City: {}".format(person['city'].title()))
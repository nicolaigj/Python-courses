languages = {
    'sarah': 'haskell',
    'robert': 'python',
    'nicola': 'c++',
    'pete': 'cobol',
    'belinda': 'python',
    'clark': 'r',
    'hillary': 'c#'
}

people = ['lars', 'hillary', 'clark', 'sarah', 'robert', 'nicola', 'pete', 'belinda', 'mark', 'precious']

people_who_responded = [name.lower() for name in languages]

for person in people:
    if person.lower() in people_who_responded:
        print("Great! Thank you {} for taking the poll!".format(person.title()))
    else:
        print("We haven't registered your response, please take the poll {}.".format(person.title()))
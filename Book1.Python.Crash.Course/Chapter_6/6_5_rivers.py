rivers = {
    'nile': 'egypt',
    'tigris': 'iraq',
    'amazonas': 'brazil',
    'rhine': 'france'
}

for river, country in rivers.items():
    print("The river {} runs through {}.".format(river.title(),country.title()))
    
for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())
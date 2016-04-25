# A list of my friends names
my_friends = ['ragnhild', 'fredrik', 'øyvind', 'stina']
# A message to my friends
message = "Hi there {}, welcome to my Python program!"
# For in loop to print message to all of my friends
for f in my_friends:
    print(message.format(f.title()))
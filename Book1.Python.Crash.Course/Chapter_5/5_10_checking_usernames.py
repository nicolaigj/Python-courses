current_users = ['john', 'st. kitts', 'nevis', 'admin', 'freddy']
new_users = ['candi', 'funnybones', 'john', 'john mcclane', 'freddy']

for new_user in new_users:
    if new_user.lower() in [name.lower() for name in current_users]:
        print("The username {} is already taken, please enter a new username".format(new_user))
    else:
        print("The username {} is available".format(new_user))

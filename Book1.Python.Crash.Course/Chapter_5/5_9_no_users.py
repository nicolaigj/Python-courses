usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello {}, would you like a status report?".format(username))
        else:
            print("Hello {}, thank you for logging in again".format(username))
else:
    print("No users, we have to find someone!")
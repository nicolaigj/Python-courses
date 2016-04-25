# A guest list of people I want to invite to a dinner
guest_list = ['Prince', 'David Bowie', 'Alan Rickman', 'Ronnie Corbett']
# Dinner invitation
invitation = "Dear {}, would you attend my dinner party?"
# A loop to print all the invitations
for g in guest_list:
    print(invitation.format(g.title()))
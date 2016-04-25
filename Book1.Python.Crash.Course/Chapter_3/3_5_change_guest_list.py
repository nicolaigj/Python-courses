# A guest list of people I want to invite to a dinner
guest_list = ['Prince', 'David Bowie', 'Alan Rickman', 'Ronnie Corbett']
# Dinner invitation
invitation = "Dear {}, would you attend my dinner party?"
# A loop to print all the invitations
for g in guest_list:
    print(invitation.format(g.title()))
# Alan Rickman couldn't seem to make it 
declined_invitation = 'Alan Rickman'
guest_list.remove(declined_invitation)
print("Seems like {} wasn't able to attend".format(declined_invitation.title()))
# Inviting Freddy Mercury instead
new_guest = 'Freddy Mercury'
guest_list.append(new_guest)
# Printing a new set of invitations
for g in guest_list:
    print(invitation.format(g.title()))

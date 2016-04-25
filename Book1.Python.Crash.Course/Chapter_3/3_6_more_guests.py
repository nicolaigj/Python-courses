def print_guest_list(invitation_to_print, guest_list_to_print):
    """Accept a invitation and a guest list to invite guests"""
    for g in guest_list_to_print:
        print(invitation_to_print.format(g.title()))

# A guest list of people I want to invite to a dinner
guest_list = ['Prince', 'David Bowie', 'Alan Rickman', 'Ronnie Corbett']
# Dinner invitation
invitation = "Dear {}, would you attend my dinner party?"
# A loop to print all the invitations
print_guest_list(invitation, guest_list)
# Alan Rickman couldn't seem to make it 
declined_invitation = 'Alan Rickman'
guest_list.remove(declined_invitation)
print("\nSeems like {} wasn't able to attend".format(declined_invitation.title()))
# Inviting Freddy Mercury instead
new_guest = 'Freddy Mercury'
guest_list.append(new_guest)
# Printing a new set of invitations
print_guest_list(invitation, guest_list)
# Inviting more people because I found a bigger table
print('\nFound a bigger table, inviting more guests!!')
guest_list.insert(0, 'Nelson Mandela')
guest_list.insert(int(len(guest_list)/2), 'Mahatma Ghandi')
guest_list.append('Dolly Parton')
print_guest_list(invitation, guest_list)

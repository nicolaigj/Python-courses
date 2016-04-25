# List of favorite hops
hops = ['willamette', 'nugget', 'cascade', 'centennial']
# Message stating my opinion about the hops
message = "Oh my, {} smells so good dry hopped!"
# Loop to print all messages
for h in hops:
    print(message.format(h.title()))
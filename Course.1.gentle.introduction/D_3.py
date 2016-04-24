seq = {'x':1,'y':3,'z':4}

for x in seq:
    print(seq[x])

print("Exiting")

for x in range(2,10,2):
    print(x)
    
s = 'hello'

for index,c in enumerate(s):
    print(index,c)
total = 0
t = "1,2,3,100,100"
for f in t.split(','):
    total = total + int(f)

print(total)
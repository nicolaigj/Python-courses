def add(*numbers, **kwargs):
    print(numbers)
    print(kwargs)
    return sum(numbers) + sum(kwargs.values())
    
x = add(1,2,3,k=100,s=3)
print(x)
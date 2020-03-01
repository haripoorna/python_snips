def medthoception(fn):
    return fn


def add_two_num(x, y):
    return x+y

# filter method 
my_list = [23, 9, 87, 65]
print(list(map(lambda x: x*x,my_list)))

#method 1
print((lambda x: x*3)(5))

# method 2
def f(x):
    return x*3

print(f(5))
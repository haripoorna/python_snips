my_variables = "I'm alone"
print(my_variables)

# lists
grades = [10, 20, 30, 40, 60]
print(sum(grades) / len(grades))
print(grades.append(4000))
print(grades.pop())

print('*****************')

# tuples
tuples = (10, 20, 40, 580, 900)  # unchanged
print(tuples)
tuples = (100,) + tuples
print(tuples)
print('*****************')

# sets
sets = {10, 20, 40, 580, 900, 900}  # unique & immutable
print(sets)
sets.add(60)
print(sets)

# sets operation

lottery_numbers = {789, 342, 3487, 123}
winning_numbers = {789, 123, 443534, 333, 323}
print(winning_numbers.intersection(lottery_numbers))
print((winning_numbers.union(lottery_numbers)))
print({1,2,3,4}.difference({2,1}));


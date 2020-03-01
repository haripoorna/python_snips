# loops

# for loop
my_list = {10, 30, 50, 89, 78}
for item in my_list:
    if item == 30:
        print(item)

user_input = input("please tell me you name.. we will print your name ..... ")
print(user_input + " " + "Hellooo you are unsucessfull person")

# if loop

age = {1, 30, 30, 46}
for item in age:
    if item == 46:
        print(item)

# check = True
# if(check):
#     print('herewrzd')

known_people = ['hari', 'bindu']
person = input('enter your name')
if person in known_people:
    print('yes i know {}'.format(person))
else:
    print('yes i dont know {}'.format(person))

dummyArray = [1, 0, 90, 123, 9989]

getEachElement = [x * 3 for x in dummyArray]

print(getEachElement)

for x in range(1, 100):
    print(x)

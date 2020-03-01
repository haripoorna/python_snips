class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @staticmethod
    def averageMarks(marks):
        return sum(marks) / len(marks)

    def friend(self, friend_name):
        return Student(friend_name, self.school)


##

student = Student('hari', 'stanns')
print(student.name)
friend = student.friend('prem')
print(friend.name)
print(friend.school)
print(student.school)

##


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("anna", "stanford", "$2000")
print(anna.salary)

annaFriend = anna.friend('binnu')
print(annaFriend.name)
print(annaFriend.school)




#Mixin 案例

class Person():
    name = "liuying"
    age = 18

    def eat(self):
        print("eating")

    def drink(self):
        print("drinking")

    def sleep(self):
        print("sleeping")

class Teacher(Person):
    def work(self):
        print("working")

class Student(Person):
    def study(self):
        print("studying")

class Tutor(Teacher,Student):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("*" * 20)
class TeacherMixin():
    def work(self):
        print("work")

class StudentMixin():
    def study(self):
        print("studying")

class TutorMixin(Person,TeacherMixin,StudentMixin):
    pass

tt = TutorMixin()
print(TutorMixin.__mro__)
print(tt.__dict__)
print(TutorMixin.__dict__)
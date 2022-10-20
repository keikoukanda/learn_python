class Student:
    def avg(self):
        print((80 + 70) / 2)
        
a001 = Student()
a001.avg()

class Student1:
    def avg(self, math, eng):
        print((math + eng) / 2)
        
a002 = Student1()
a002.avg(80, 40)

a002.name = "John"
print(a002.name)

a002.gender = "male"
print(a002.gender)

a003 = Student1()
a003.avg(40, 60)
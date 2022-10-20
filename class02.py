class Student1:
    
    def __init__(self):
        self.name = ""
        
    def avg(self, math, eng):
        print((math + eng) / 2)
        
a001 = Student1()
a001.name = "John"
print(a001.name)

a002 = Student1()
a001.name = "Tenz"
print(a002.name)

class Student2:
    
    def __init__(self, name):
        self.name = name
        
    def avg(self, math, eng):
        print((math + eng) / 2)
        
a001 = Student2("John")
print(a001.name)

a002 = Student2("Tenz")
print(a002.name)
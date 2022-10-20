class Student():
    
    def __init__(self, name):
        self.name = name
        
    def calcAVG(self, math, eng, phys):
        avg = (math + eng + phys) / 3
        
        print(avg)
        if avg >= 60:
            print("path")
        else:
            print("failed")
                
a001 = Student("Sinatra")
a001.calcAVG(90, 70, 30)

a002 = Student("John")
a002.calcAVG(50, 20 ,10)

print(type(a001.name))
print(type(a001.calcAVG))
class Student():
    
    def __init__(self, name):
        self.name = name
        
    def calcAVG(self, data):
        sum = 0
        for num in data:
            sum += num
        
        avg = sum / len(data)
        return avg
    
    def jedge(self, avg):
        
        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"
        return result
    
list_name = ["June", "Flower", "Blod"]
a001 = Student(list_name[1])
data = [60, 20, 70, 30, 50]
avg = a001.calcAVG(data)
result = a001.jedge(avg)

print(avg)
print(a001.name + " " + result)
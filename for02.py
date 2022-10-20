# for i in range(3):
#     for j in range(3):
#         print(i, j, sep="-")
        
from re import S


arr = [2, 4, 6, 8, 10]
sum = 0
for i in arr:
    # print(i)
    sum += i
    print(sum)
    
print("total",sum)
print(type(sum))
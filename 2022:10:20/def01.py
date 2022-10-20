def say_hello(greeting):
    print(greeting)
    
say_hello("hello world")

def said_hello():
    print("hello guys")
    
said_hello()

hello = say_hello
hello("Good Morning")

def add(num01, num02):
    print(num01 + num02)
    
add(6, 2)

def add1(num01, num02):
    return(num01 + num02)
    
print(add1(4, 2))

def add2(num01, num02):
    return(num01 + num02)

add_result = add2(5, 9)
print(add_result)
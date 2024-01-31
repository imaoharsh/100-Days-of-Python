def greet(n="None"):
    print("Hello user :",n)

n=input("Enter your Name :")

greet(n)

print('-'*40)

#Addition Function

def suma(a=0,b=0):
    return (a+b)


x=suma(9,8)
print(x)

#Multi -Return Function

def arithmetic( x=0, y=0):
    return x+y, x-y, x*y 


print(arithmetic(2,5))
x,y,z=arithmetic(2,3)

print(x,y,z)

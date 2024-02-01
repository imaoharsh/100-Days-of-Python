class Person:
    def __init__(self,name,age):                               #Init is just like Constructor in C/C++.
        
        self.name=name
        self.age=age
        
    def run(self):
       print(self.name)
       print(self.age,'\n')
    
    def Sum(self,x,y):
        return (x+y)


p1=Person("Harshit",22)

p1.run()

p2=Person("Mohan",23)

p2.run()

p3=Person("Harsh",24)

p3.run()



#Inheritance

class car:
    def __init__(self,tyre,bodycolor) :
        self.tyre=tyre
        self.bodycolor=bodycolor
    
    def drive():
        print("Car is running")
    
    def running(self):
        print(self.tyre)
        
    def info(self):
        print(self.tyre)
        print(self.bodycolor)
        
print('-'*40)
c1=car(200,"green")
c1.tyre=50

c1.info()

print('-'*40)
class Mahindra(car):
    def electronics():
        print("car having ADAS");

c2=Mahindra(500,"red")

c2.info()
        

    
    


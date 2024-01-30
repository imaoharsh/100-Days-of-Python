print('-'*15,"For Loop",'-'*15)
for i in range(5):              # range from  0 to n-1
    print(i,end=',')
print('\n','-'*30)
for i in range(1,12,2):          #from 1 till 12 with a gap of 2
    print(i)

print('-'*30)
    
n=int(input("Enter the number:"))

print('-'*30)

for i in range(n,(n*10)+1,n):
    print(i)
    
print('-'*15,'While Loop','-'*15)

n=30
i=1
sum=1
while(n>sum):
    print(sum)
    i=i+1
    sum=sum+i

print("Reverese a Number ")
n=1234

while(n>0):
    print(n%10,end='')
    n=int(n/10)

print('-'*30) 
fruits = ["apple", "banana", "cherry"]

# Using enumerate to iterate over both index and value
'''
The enumerate() function in Python is a built-in function that is used to add a counter to an iterable object (e.g., a list, tuple, or string). 
It returns an enumerate object, which contains pairs of index and element values. 

'''
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")
    
    


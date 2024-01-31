#Multi Dimensional List
'''
you can store a list as a value inside a dictionary in Python
 

'''
dct={
    1:{'name':"Harshit","age":22},
    2:{'name':"Mohan","age":20}
}
print(dct)

#Accessing the Elements
print(dct[1]["name"])

#Adding,Deleting,Updating Values.
dct[4]={'name':"manan","age":21}     #Adding
print(dct)

dct[4]["name"]="fiskel"              #Updating
print(dct)

del(dct[4])                           #Deleting
print(dct)
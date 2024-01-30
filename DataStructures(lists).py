'''
Python provides several built-in data structures that can be used to store and manipulate data efficiently. Some commonly used data structures in Python include:

(Imp)Lists: Lists are ordered, mutable collections of elements. They can store elements of different data types and allow duplicate values.

Tuples: Tuples are ordered, immutable collections of elements. They are similar to lists but cannot be modified once created.

Sets: Sets are unordered collections of unique elements. They do not allow duplicate values and provide operations like union, intersection, and difference.

(Imp) Dictionaries: Dictionaries are unordered collections of key-value pairs. They provide fast access to values based on their keys.

Strings: Strings are sequences of characters. They are immutable and provide various methods for string manipulation.

These data structures can be used to solve a wide range of problems and are fundamental to Python programming.

'''
list_ds=[1.4,"Dev","dopa","arin","harshit"]
print(type(list_ds))

#Accesing the value of list
print(list_ds[4])

list_ds[4]="mohan"   #list mutable
print(list_ds[4])

print('-'*20)

#Slicing in List
# The general syntax for slicing is start:stop:step

print(list_ds[1:4])
print(list_ds[:1:-1])

print('-'*20)

#Appending
list_ds.append("raghav")
print(list_ds)

#Removing
list_ds.remove("dopa")
print(list_ds)

list2=[3,2,4,9,5,6]
print(sorted(list2))

print('-'*20)

#Finding element
print(list_ds.index("mohan"))

print('-'*20)

#Counting value in list
list3=["harshit","harshit","mohan","dopa"]
print("Number of times harshit repeated in list:",list3.count("harshit"))


#Extending 
#it help us to multiple element at a same time while in append we only add one element at one time.

list_ds.extend(["kk","lk"])
print(list_ds)

print('-'*20)

#Iterating the list

for i in list_ds:
    print(i,end=' ')
    

print('\n','-'*20)
    
#Iterating the list using indexing
for i in range(len(list_ds)):
      print(list_ds[i],end=',')

print('\n','-'*2,"Reversing a List ",'-'*20)
for i in range(len(list_ds)-1,-1,-1): 
      print(list_ds[i],end=',')
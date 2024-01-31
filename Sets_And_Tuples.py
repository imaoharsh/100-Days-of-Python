'''
Sets:
sets are mutable.
{}
no dulicacy i.e unique values
unordered
if we key value than its a dictionary if we take only value than its a set.

Tuple:
immutable
()
duplicacy
ordered


'''

#Set:

my_set={1,2,3,4,5,6}
print(my_set)
print(type(my_set))


print('-'*20)

#Adding Value to the set
print(my_set)
my_set.add(7)
print(my_set)


#Pop: pop function remove element from the front.
my_set.pop()
print(my_set)


#discard: you can choose which element you want to remove.

my_set.discard(4)
print(my_set)

#Set Operation

set1={1,2,3}
set2={4,5,3}

print('union :', set1 | set2)

print('intersection :',set1.intersection(set2))

print('intersection :',set1&set2)

print("Difference :",set1-set2)

print('Symmetric Difference :',set1 ^ set2)  #removing the common elements from both of the set and union it.

print('-'*30)
#clearing the set
print(set1)
set1.clear()
print(set1)

#Tuple:

tpl=(1,2,3,4)
print(tpl)

#accessing the tuple:
print(tpl[1])

print('-'*30)

#Slicing on tuple:
print(tpl[1:4])

#Concatenate:
tpl1=(1,2,4)
tpl2=(4,5,6)
print(tpl1+tpl2)

print(tpl2*3)   #tuple repeat itself 3 times

tup4=()
tup4[0]=1
print(tup4)


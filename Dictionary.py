'''
In Dictionaries data are in key value pair.
denotes with curly brackets.

key must be unique:
eg:
this 1 and this '1' are different differ by datatype one is integer and one is string.
this "ashish" and this 'Ashish' are different { differ by 'a & 'A'}

'''
dict={
    1:"'Harsh",
    2:"Arin",
    2:"Ankur",                     # this will overwrite the value of key 2.
    3:"Manan",
    "ashish":"you"
}

print(dict["ashish"])
print(dict[1])

print('-'*30)
#Adding New Data

dict[4]="moye"
print(dict)

del(dict[4])   #Deleting the Value.
print(dict)

#clearing whole dictionary
#dict.clear()
print(dict)


print(dict.keys())


for i in dict.keys():
    print(i,dict[i])
    
# OR you can use

print("Dict Itmes: ",dict.items())

for k,v in dict.items():
    print(k,v)

#Checking key is presen in dict.

print(1 in dict)

print(10 in dict)


dict1={1:'A',2:'B'}
dict2={3:'C',4:'D'}

dict1.update(dict2)

# Note: if dict 2 have same keys as dict1 then if we try to update dict1 with dict2 then it will overwrite the value of dict1 according to key value configs.
print(dict1)

dict

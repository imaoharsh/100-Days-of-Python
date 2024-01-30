#In MultiDimensional we are adding list inside a list.

lst=[[1,2,3],[4,5,6],[7,8,9]]
lst2=[["harshit",22,"kota"],["Mohan",20,"Jaipur"],["Arin",2,"Baran"]]     # [Name,age,city]

print(lst)

print('-'*30)

print(lst[0][0])          #O/P:1
print(lst[0][2])          #O/P:3

#printing the value
for i in lst:
    for j in i:
        print(j)

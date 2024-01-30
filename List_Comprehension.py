lst=[1,2,3,4,5,6]
print(lst)

lst=[i**2 for i in lst]  #this is called list comprehension in which we write what operation we have to perform for loop and then as for loop
# iterate we store value inside lst.
print(lst)

#finding first 10 even numbers
lst2=[i for i in range(0,20) if i%2==0]

print(lst2)

'''
pehle yeh 'for i in range(0,20) if i%2==0' chalega phir jo value aayegi voh i mein store hogi.

'''

#Multi-Dimensional Lists.

#print([[i for j in range(8)] for i in range (5)])

#Flatten the Matrix. 

lst=[[1,2,3],[4,5,6],[7,8,9]]

lst2=[j for i in lst for j in i]
print(lst2)

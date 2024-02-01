# Zip.Lambda,Filter,Map

#Zipping
lst1=['A','B','C']
lst2=[1,2,3]

print(list(zip(lst1,lst2)))

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print([list[row] for row in zip(matrix)])

print([list[row] for row in zip(*matrix)])

print('-'*40)

#filters

def even_fun(n):
    if(n%2 == 0):
        return n
    
print(list(filter(even_fun,[1,2,3,4,5,6])))                #stores element in list which even_fun returns


#Lambda (alternative of using function)
add_num=lambda x,y :x*y
print(add_num(5,10))                   
print('-'*40)
num=[1,2,3,4,5,6,7,8,9]
df=filter(lambda x: x%2 ==0,num)

print(list(df))

#Maps

num=[1,2,3,4,5,6,7,8,9]

def sqr(x):
    return x**2

print(list(map(sqr,num)))
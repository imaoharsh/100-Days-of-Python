tup=(1,2,3)

lst=list(tup)
lst=[i*2 for i in lst]
x=len(lst)
print(lst[x-1])



try:
    num=int("abc")
    
except ValueError as e:
    print(f"Error:{e}")
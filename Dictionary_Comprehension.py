


dict={i:i**2 for i in range(1,6)}              #   i:i**2 (here i is key and i**2 is value)
print(dict)

#storing squared value inside dict if it is even 

dict2={i:i**2 for i in range(1,11) if (i%2 == 0)}
print(dict2)


#Converting List into Dict.

lst=["Apple","Banana","Grapes"]

dct_Fruits={item:len(item) for item in lst}

print(dct_Fruits)

#Special Keys

dict3={'num_'+str(i):i for i in range(1,10)}
print(dict3)


#Shortlisting Based on value
dct4={k:v for k,v in dict3.items() if v%3 ==0}
print(dct4)


#String Concatenation
print("Master"+"Harshit")

#String Replication
print('H'*6)
print('-'*20)

#String Lenght
name="HARSHIT"
print(len(name))

#String Slicing
 #The general syntax for slicing is start:stop:step
print('Harshit'[-1])
print('Harshit'[0:5])  #last index not be include if you want to include whole string then add one to last index.
print('Harshit'[3:])
print('Harshit'[:5])
print('Harshit'[-3:8 ])

#String Case Conversion

print('Harshit'.upper())
print('Harshit'.lower())
#String Stripping
print("     Harshit    ".strip())
print("   Harshit     Kapoor     ".strip() ) #Remove the whitespaces from the beginning and the end of the string not works if unnecessary soaces are between two strings.

#String Replacing

print('harshit'.replace('h','p')) #replaicng with h with p.

#String Count
print('PPappa'.lower().count('p')) #converting PPappa into lower then count 'p' in the new string.

#String Checker

print("harshit".isalpha())
print('harshit'.isnumeric())
print('1234'.isnumeric())
print('harshit'.islower())
print('HARSHIT'.isupper())

print('-'*30)

#String Capitaliaion
print('harshit kapoor'.capitalize())
print('harshit kapoor'.title())

print('-'*30)

#startswith and endswith

print('harshit'.startswith('har'))
print('harshit'.endswith('it'))

#align
print('harshit'.center(20,'-'))
print('harshit'.ljust(20,'*')) #remaing will filled with *
print('harshit'.rjust(20,'&'))
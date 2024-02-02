try:
    x=10
    print("working")
    print(x/0)                      #till error is not detected it will work. Once error detects from that line exception block works.
    print("I'm here")


except:
    print("ZeroDivsionError")
    
print('-'*40)

#Exception with specific error:

try:
    x=10
    print(x/0);
except ZeroDivisionError:                             #works for specific error similarly you define multiple exception.
    print("Divide it by any number except zero")
except:
    print("Default error handling")
    
print('-'*40)

try:
    num1,num2=10,0
    print(num1/num2)
except ZeroDivisionError as zde:
    print(zde)
except Exception as e:
    print(e)
else:                                 #if Try works fine than only else block work
    print("try block works fine")
finally:                              #it works for block try as well as except.
    print("Program End")
    
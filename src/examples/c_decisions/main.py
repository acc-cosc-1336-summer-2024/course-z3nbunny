import decisions

value1 = input("Enter a number: ")#read from keyboard, Python brings in values as a string variable

result = decisions.is_number_not_in_range(int(value1), 1, 10) #convert value to integer number with int function

if(result == True):
    print(value1, " not in range")
else:
    print(value1, " in range")
    
print(result)

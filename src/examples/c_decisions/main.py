import decisions

value1 = input("Enter a number: ")#read from keyboard, Python brings in values as a string variable

result = decisions.is_number_in_range(int(value1), 1, 10) #convert value to integer number with int function
print(result)
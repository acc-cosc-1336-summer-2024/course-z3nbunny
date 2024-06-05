import devprocess

value1 = input("Enter a number: ") #Python treats numbers as character from input
value2 = input("Enter a number: ")

result = devprocess.add_numbers(int(value1), int(value2)) #convert value to integer using int function

print(result)

value1 = input("Enter a number: ") #Python treats numbers as character from input
value2 = input("Enter a number: ")

result = devprocess.subtract_numbers(float(value1), float(value2))
print(result)
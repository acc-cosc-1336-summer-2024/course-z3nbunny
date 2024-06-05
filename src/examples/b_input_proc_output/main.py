import input_process_output #references input_process_output.py

value = input("Enter and number: ") #capture keyboard data

integer = input_process_output.echo_number(value) #echo_number function is in the input_process_output.py file
print(integer)

value = input("Enter a decimal number: ")

float = input_process_output.echo_decimal_number(value) #echo_decimal function is in the input_process_output.py file
print(float)

value = input("Enter a sequence of chars: ")

string = input_process_output.echo_string(value)#echo_string function is in the input_process_output file

print(string) #print is built in
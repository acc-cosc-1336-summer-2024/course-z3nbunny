#
def get_factorial(num):

    factorial = 1

    for val in range(1, num + 1):
         factorial *= val

    return factorial



def sum_odd_numbers(num):
     
    sum = 0
    i = 1
    while i <= num:
        if i % 2 != 0: #checks for odd number
            sum += i
        i += 1
    return sum
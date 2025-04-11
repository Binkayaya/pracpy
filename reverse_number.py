# Reverse a number without any conversion to strings

def reverse_number(n):
    number = n
    reversed_number = 0
    while number > 0:
        single_digit = number % 10
        reversed_number = reversed_number * 10 + single_digit
        number = number // 10
    print('The reversed number is: ', reversed_number)

reverse_number(100148)

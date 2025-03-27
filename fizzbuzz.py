# This is the FizzBuzz problem. 
# We print numbers 1 to 100
# If a number is divisible by 3, we print fizz
# If divisible by 5 we print buzz
# If divisible by both, we print fizzbuzz
# If prime, we print prime.                      |

user_input = 101
user_range = range(1,user_input)

def prime_func(r):
    mod_list = []
    target = range(2, r+1)
    check = [2,3,4,5,6,7,8,9]
    for number in target:
        for divisor in check:
            if number % divisor == 0 and number != divisor:
                mod_list.append(number)

    prime = list(set(target) - set(mod_list) )
    return(prime)

prime_number = prime_func(user_input)

for num in user_range:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} is Fizz")
    elif num % 5 == 0:
        print(f"{num} is Buzz")
    elif num in prime_number:
        print(f"{num} is Prime")




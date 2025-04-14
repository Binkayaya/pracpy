# This is the FizzBuzz problem. 
# We print numbers 1 to 100
# If a number is divisible by 3, we print fizz
# If divisible by 5 we print buzz
# If divisible by both, we print fizzbuzz
# If prime, we print prime.                      |

user_input = int(input('What should be the maximum number? '))
numbers_to_check = range(1,user_input)

def prime_func(n):
    primes = []
    for num in range(2,n+1):
        is_prime = True
        for divisor in range(2, int(num**0.5)+1):
            if num%divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

prime_number = prime_func(user_input)

for num in numbers_to_check:
    if num in prime_number:
        print(f"{num} is Prime")
    elif num % 3 == 0 and num % 5 == 0:
        print(f"{num} is FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} is Fizz")
    elif num % 5 == 0:
        print(f"{num} is Buzz")

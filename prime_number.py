def check_prime(n):
    primes = []
    
    for num in range(2,n+1):
        is_prime = True
        for divisor in range(2, int((num)**0.5)+1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
        
n = int(input('Input a number: '))
primes = check_prime(n)
print(primes)
print(f'There are {len(primes)} prime numbers lower than {n}')

# Using the Sieve of Eratosthenes Algorithm. Just uncomment it and run.
'''def sieve(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for multiples in range(i*i, n+1, i):
                primes[multiples] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]

n = int(input('Input a number: '))
primes = sieve(n)
print(primes)
print(f'There are {len(primes)} prime numbers lower than {n}')
'''

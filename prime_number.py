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
print(f'There are {len(primes)} prime numbers between lower than {n}')


# in this excercise, we will print out all prime numbers between 1 and 100
 
# i think that every number between 1 and 100 that isnt divisible by any number between 1 and 9 is a prime number.
# So we get a list of numbers between 1 and 9, and we use a loop to go through to divide the targets which
# will also be a loop from 1 to hundred.

mod_list = []
target = range(2, 101)
check = [2,3,4,5,6,7,8,9]
for number in target:
    for divisor in check:
        if number % divisor == 0 and number != divisor:
            mod_list.append(number)

prime = list(set(target) - set(mod_list) )
print(f'there are {len(prime)} prime numbers between 1 and 100. They are given below: ')
print(prime)

       


    
    
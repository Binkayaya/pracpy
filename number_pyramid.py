# We need to write a code that prints numbers from 1 to n with increamenting the number of numbers each time.
# something like this
# 1
# 1 2
# 1 2 3 
# 1 2 3 4


max_layer = int(input('How many layers should your pyramid have?'))


for layer in range(1, max_layer + 1):
    for number in range(1, layer +1):
        print(number, end=' ')
    print()
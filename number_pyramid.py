# We need to write a code that prints numbers from 1 to n with increamenting the number of numbers each time.
# something like this
# 1
# 1 2
# 1 2 3 
# 1 2 3 4


user_input = int(input('How many layers should your pyramid have?'))

def new_line(num):
    print(num)

for num <= user_input:
    print(layer(num))
# We need to write a code that prints numbers from 1 to n with increamenting the number of numbers each time.
# something like this
# 1
# 1 2
# 1 2 3 
# 1 2 3 4


user_in = int(input('How many layers should your pyramid have?'))

num = list(range(1,user_in+1))

for i in range(len(num)):
    print((num[0:i+1]))
num_layers = int(input('How many layers should your tree have? '))

num = num_layers * 2
j = 1
for i in range(num):
    if i % 2 == 1:
        print(' '*int((num/2)-j) + '*'*i + ' '*int((num/2)-j))
        j +=1  
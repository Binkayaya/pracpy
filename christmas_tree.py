num_layers = int(input('How many layers should your tree have? '))

num = num_layers * 2

for i in range(1, num, 2):
        print(' '*int(num-i//2) + '*'*i)
      
        

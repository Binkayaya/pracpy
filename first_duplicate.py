# Given a list of numbers, find the first duplicate number. If there’s no duplicate, print "No duplicates found".

init_list = [5, 7, 8, 2, 9, 6, 7, 9, 5]
newlist = []
for i in init_list:
    for j in range(0, len(init_list)):
        if i/init_list[j] == 1 and init_list.index(i) != j:
            newlist.append(i)
            init_list.remove(i)
            break
if len(newlist) > 0:
    print(newlist)
else:
    print('No duplicates found')

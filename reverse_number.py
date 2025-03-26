#reverse number

number = 37892
newlist = []
while number % 10 != 0:
    newlist.append(number % 10)
    number = number // 10
    
listing = []

for i in newlist:
    digit = i*10**(len(newlist)-(newlist.index(i)+1))
    listing.append(digit)

outputnum = sum(listing)
print(outputnum)

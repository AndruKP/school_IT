n = int(input())

if n%10==1:
    print(n,'rik')
elif n%10 in [0,5,6,7,8,9]:
    print(n,'rokiv')
else:
    print(n,'roky')

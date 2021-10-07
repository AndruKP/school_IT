n = int(input())
l = list(map(int,input().split()))
l.sort()
min_1,min_2 = l[0],l[1]

max_1,max_2,max_3 = l[-1],l[-2],l[-3]

print(max(max_1*max_2*max_3,min_1*min_2*max_1))
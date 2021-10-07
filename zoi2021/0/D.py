T = input()
s = set()

for i in range(len(T)):
    for j in range(i+1,len(T)+1):
        _ = T[i:j]
        s.add(_)
print(len(s))

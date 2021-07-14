# Compress the given strings as given below

# INPUT

# aaabbb

# OUTPUT

# a3b3

a=input()
v=a[0]
c=0
l=[]
for i in range(len(a)):
    if a[i]==v:
        c+=1
    else:
        l.append(a[i-1])
        l.append(str(c))
        c=1
        v=a[i]
l.append(a[i])
l.append(str(c))
print(''.join(l))


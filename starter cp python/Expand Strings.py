# Write a program to expand strings as given below:

# Assume only a and b are the only two letters and numbers will not exceed 100



# INPUT

# a2b3

# OUTPUT

# aabbb



# INPUT

# a5b10

# aaaaabbbbbbbbbb

a=input()
l=[]
for i in range(len(a)):
    if a[i].isnumeric():
        for j in range(int(a[i])-1):
            l.append(a[i-1])
    else:
        l.append(a[i])
print(''.join(l))

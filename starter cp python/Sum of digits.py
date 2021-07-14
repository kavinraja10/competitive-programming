# Write a program to find the sum of digits till the sum is a single digit number



# Input:

# 12345

# Output:

# 6

# NOTE: 1+2+3+4+5 = 15 but that is not a single digit number. So you again add that 1 + 5 = 6

a=list(map(int,list(input())))
b=sum(a)
while(1):
    if len(str(b))==1:
        print(b)
        break
    else:
        b=sum(list(map(int,list(str(b)))))


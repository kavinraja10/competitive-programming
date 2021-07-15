# Write a program to find the given input is binary or not
# Input:

# 110111

# Output:

# Binary



# Input:

# 1098988232

# Output:

# Not Binary
a=input()
for i in a:
    if int(i)==1 or int(i)==0:
        pass
    else:
        print('Not Binary')
        break
else:
    print('Binary')

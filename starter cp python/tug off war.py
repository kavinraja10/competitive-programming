# Two teams are playing tug off war. The number of people on both the sides is given as inputs.
# After that the weight of each person in first team and the weight of each person in second team is given. 
# If the number of people in each team is not equal print two teams are not equal. 
# If the number of people in each team is equal and the weight of each person in first team matches
# with the weight of each person in the second team then print that the teams are equal.



# If 3rd person in first team has a weight 65, the third person on second team also should have a weight 65



# Explanation:
# 3
# 3
# 10
# 20
# 30
# 10
# 20
# 30


# First 3 is the number of people on team 1
# Second 3 is the number of people on team 2


a=int(input())
b=int(input())

if a!=b:
    print('Not Equal')
else:
    l=[]
    k=[]
    for i in range(a):
        l.append(int(input()))
    for i in range(a):
        k.append(int(input()))

    if sum(l)==sum(k):
        print("Equal")
    else:
        print("Not Equal")

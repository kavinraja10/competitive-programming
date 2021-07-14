# You have a strange crypt text sentence that you have received. Objective is to decode the scroll using the following rules

# The sentence has to be split to words separated by spaces
# The last letter in each word has to be taken. They have to be combined to form a PRE-SCROLL word
# The first two characters of the PRE-SCROLL word should be swapped (1st pair), second and third characters of the PRE-SCROLL word should be swapped (2nd pair) and so on..
# If it is an ODD number of characters in the PRE-SCROLL word, the last character should not be swapped
# If there is any pre-scroll pair that has a number (between 0 to 9) then the pair should not be swapped. Even if one of the letters in a pair is a number the number should not be swapped


# Read the INPUT and OUTPUT to understand the combinations



# INPUT:

# India is a beautiful country



# OUTPUT:

# salay

# Explanation:

# The last letter of each word was taken and the PRE-SCROLL word was formed - asaly

# Now "as" was swapped and "sa"

# "al" was swapped and "la"

# last letter y is left as is since it is odd number of characters

# So output is salay



# INPUT:

# Golden Eye 007 here

# OUTPUT:

# en7e



# Explanation:

# The PRE-SCROLL word GE7e is formed

# the first two characters are swapped to get EG and then the 3rd is a number so it is left as is without swapping.

a=input().split()
l=[]
for i in a:
    l.append(i[-1])
a=[]
for i in range(0,len(l)-1,2):
    if l[i].isnumeric() or l[i+1].isnumeric():
        a.append(l[i])
        a.append(l[i+1])
    else:
        a.append(l[i+1])
        a.append(l[i])
if len(l)%2==0:
    print(''.join(a))
else:
    print(''.join(a+list(l[-1])))

def alternatingCharacters(s):
    # Write your code here
    i=0
    s=list(s)
    count=0
    v=s[0]
    for i in range(1,len(s)):
        if s[i]==v:
            #s.pop(i)
            count+=1
        else:
            v=s[i]
            

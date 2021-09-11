def jumpingOnClouds(c):
    # Write your code here
  
    i=0
    j=0
    while i<=len(c): 
                if i+2<len(c) and c[i+2]==0:
                    j+=1
                    i=i+2
                elif  i+1<len(c) and c[i+1]==0:
                    j+=1
                    i+=1
                else:
                    i+=1
    return j

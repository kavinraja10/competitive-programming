def sockMerchant(n, ar):
    c={}
    count = 0
    for i in ar:
        if i in c:
            
            c[i] += 1
            if c[i] == 2:
                print(c)
                count+=1
                c[i] = 0
        else:
            
            c[i] = 1
    return (count)

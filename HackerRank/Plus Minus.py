def plusMinus(arr):
    n,z,p=0,0,0
    l=len(arr)
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    print("%.6f"%(p/l))
    print("%.6f"%(n/l))
    print("%.6f"%(z/l))

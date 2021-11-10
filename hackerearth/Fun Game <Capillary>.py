def funGame (arr):
    arr1=arr[::-1]
    l=[]
    while 1:
        if len(arr1)==0 or len(arr)==0:
            break
        a=arr1[-1]
        b=arr[-1]
        if a>b:
            l.append(1)
            arr.pop()
        elif a<b:
            l.append(2)
            arr1.pop()
        else:
            l.append(0)
            arr1.pop()
            arr.pop()
    return l

def divide_by_2(n):
    if n==1:
        return True
    if n%2 != 0 :
        return False
    if n == 2:
        return True
        
    elif n<2 :
        return False
    return(divide_by_2(n/2))
return divide_by_2(n)

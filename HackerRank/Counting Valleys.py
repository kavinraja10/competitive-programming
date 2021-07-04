def countingValleys(steps, path):
    level = 0 
    valley = 0
    count = 0
    for i in path:
        if i == "U":
            level += 1
        else:
            level -= 1
        
        if level < 0:
            valley = 1
        if valley == 1 and level == 0:
            count+=1
            valley = 0 
    # Write your code here
    return count    

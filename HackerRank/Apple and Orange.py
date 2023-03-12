def countApplesAndOranges(s, t, a, b, apples, oranges):
        apples=list(map(lambda i:i+a,apples))
        oranges=list(map(lambda i:i+b,oranges))
        ac=0
        oc=0
        ac=len([i for i in apples if i>=s and i<=t])
        oc=len([i for i in oranges if i>=s and i<=t])            
        print(ac)
        print(oc)

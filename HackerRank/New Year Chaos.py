def minimumBribes(q):
    count=0
    for i in reversed(range(len(q))):
        m=max(q[:i+1])
        #print(q[:i+1])
        mv=q[i]
        if i-q.index(m)>2:
            print('Too chaotic')
            return
        if m>mv:
            count+=i-q.index(m)
            #print( q[q.index(m)],q[i])
            q.pop(q.index(m))
            q.append(m)
    print(count)
        

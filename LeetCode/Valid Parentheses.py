    def isValid(self, s: str) -> bool:
        d={')':'(',']':'[','}':'{'}
        l=[]
        if len(s)%2 != 0:
            print(45614)
            return False
        elif s[0] in d:
            return False
        else:
            for i in s:
                if i in d:
                    if  len(l)==0 or l.pop() != d[i]:
                        print(1010)
                        return False
                else:
                    l.append(i)
        if len(l)==0:
            return True
        else:
            return False
                        
                        
        
        

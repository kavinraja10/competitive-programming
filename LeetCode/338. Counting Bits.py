def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            l.append(bin(i).count('1'))
        return l

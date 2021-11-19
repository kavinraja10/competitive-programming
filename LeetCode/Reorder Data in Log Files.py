class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let,dig=[],[]
        for i in logs:
            cur=i.split(' ',1)
            #print(i[1])
            if i[-1].isalpha():
                let.append((cur[1],cur[0]))
            else:
                dig.append(i)
        f=[]
        # print(let)
        let.sort()
        for i in let:
            f.append(i[1]+' '+i[0])
        return f+dig

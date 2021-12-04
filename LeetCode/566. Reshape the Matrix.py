class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        l=[]
        for i in mat:
            for j in range(len(i)):
                l.append(i[j])
        f=[]
        k=0
        print(l)
        for i in range(r):
            v=[]
            for j in range(c):
                v.append(l[k])
                k+=1
            f.append(v)
        return f

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        r=0
        c=0
        while  r<len(matrix):
            if matrix[r][c]==0:
                row.append(r)
                col.append(c)
            if c==len(matrix[0])-1:
                r+=1
                c=0
            else:
                c+=1
        #print(row,col)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    #print(i,j)
                    matrix[i][j]=0
        print(matrix)

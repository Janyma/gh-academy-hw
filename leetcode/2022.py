def construct2DArray(original, m, n):
    a=[[0]*n for _ in range(m)]
    b=0
    if (len(original)> m*n or len(original)<m*n):
        return []
    else:
        for i in range(m):
            for j in range(n):
                a[i][j]=original[b]
                b+=1
    print(a)
print(construct2DArray([2,4,3,2], 2, 2))



        
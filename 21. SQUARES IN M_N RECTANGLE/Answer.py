def countSquares(m, n):
     
    # If n is smaller, swap m and n
    if(n < m):
        temp = m
        m = n
        n = temp
         
    for r in range(1,m+1):
        print((n-(r-1))*(m-(r-1)))

 
# Driver Code
if __name__=='__main__':
    m = int(input())
    n = int(input())
    countSquares(m, n)

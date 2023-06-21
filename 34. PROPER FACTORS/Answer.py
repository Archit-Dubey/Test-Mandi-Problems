def printDivisors(n) :
    i = 2
    sum=0
    while i <= n/2 :
        if (n % i==0) :
            sum=sum+i
            
        i = i + 1
    print (sum)
# Driver method

printDivisors(int(input()))


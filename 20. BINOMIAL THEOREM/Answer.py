''' (a*x + b*y)^n = '''

import math
sum=0
a=int(input())
b=int(input())
n=int(input())
temp=n
for x in range(0,n+1):
    sum= sum + math.comb(n,x) * (a**(x+temp)) * (b**x)
    temp=temp-2
print(sum)


def factorial(num):
	factorial = 1
	for i in range(1,num + 1):
	    factorial = factorial*i
	return factorial
def combinations(a,b):
	return (factorial(a)/factorial(b))
    
m = int(input())
n = int(input())
x = int(input())
y = int(input())

probW = m / (m+n)
probB = n / (m+n)
answer=0
for z in range(x,y-1,-1):
	temp=combinations(x,z)
	answer+=temp*((probW)**z)*((probB)**(x-z))
print(round(answer, 4))

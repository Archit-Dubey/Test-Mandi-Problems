n=int(input())
ans=0
root1=(19-3*33**0.5)**(1/3)
root2=(19+3*33**0.5)**(1/3)
root3=(586+102*(33)**0.5)

for x in range(n-2,n-5,-1):
    numerator=3*((1/3*root2 + 1/3*root1 +1/3)**x)*root3**(1/3)
    denominator=root3**(2/3) + 4 -2*(root3)**(1/3)
    sum=numerator/denominator
    ans=ans+sum
print(int(round((ans),0))%107)
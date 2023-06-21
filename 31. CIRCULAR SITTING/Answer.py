
arr=list(map(int,input().split()))
f=0
for x in range(0,len(arr)):
    if(arr[x-1]<arr[x]<arr[x-(len(arr)-1)]):
        f=f+1
        print(x+1)
if(f==0):
    print("None")




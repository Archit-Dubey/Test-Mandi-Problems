n=int(input())
arr=list(map(int,input().split()))

def findQuadruplets(arr, n):
 
    found = False
 
    # sort array elements
    arr.sort()
 
    for i in range(0, n-1):
     
        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l + 1 < r):
         
            if (x + arr[l] + arr[l+1] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[l+1], arr[r])
                l+=1
                r-=1
                found = True
             
 
            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l+=1
 
            # if sum is greater than zero than
            # decrement in right side
            else:
                r-=1
         
    if (found == False):
        print("No Quadruplets Found")
        
findQuadruplets(arr,n)
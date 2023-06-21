def maximumTip(arr1, arr2, n, x, y):
 
    # Base Condition
    if n == 0:
        return 0
 
    # If both have non-zero count then
    # return max element from both array
    if x != 0 and y != 0:
        return max(
            arr1[n-1] + maximumTip(arr1, arr2, n - 1, x-1, y),
            arr2[n-1] + maximumTip(arr1, arr2, n-1, x, y-1)
            )
 
    # Traverse first array, as y
    # count has become 0
    if y == 0:
        return arr1[n-1] + maximumTip(arr1, arr2, n-1, x-1, y)
 
    # Traverse 2nd array, as x
    # count has become 0
    else:
        return arr2[n - 1] + maximumTip(arr1, arr2, n-1, x, y-1)
 
 
# Drive Code
N = int(input())
X = int(input())
Y = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
 
# Function Call
print(maximumTip(A, B, N, X, Y))

'''
5
3
3
5 4 3 2 1
1 2 3 4 5
'''
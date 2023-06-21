def LBS(nums):
 
    n = len(nums)
 
    if n == 0:
        return

    I = [[] for _ in range(n)]
    I[0].append(nums[0])
 
    for i in range(1, n):
        for j in range(i):
            if len(I[i]) < len(I[j]) and nums[i] > nums[j]:
                I[i] = I[j].copy()
        I[i].append(nums[i])
 
    D = [[] for _ in range(n)]
    D[n - 1].insert(0, nums[n - 1])
 
    for i in reversed(range(n - 1)):
        for j in reversed(range(i + 1, n)):
            if len(D[i]) < len(D[j]) and nums[i] > nums[j]:
                D[i] = D[j].copy()
        D[i].insert(0, nums[i])
 
    peak = 0
    for i in range(1, n):
        if len(I[i]) + len(D[i]) > len(I[peak]) + len(D[peak]):
            peak = i
    
    D[peak].pop(0)
    print(len(I[peak]+D[peak]))
    print(I[peak]+D[peak])
    
arr =  list(map(int,input().split()))
'''
0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
7
'''
LBS(arr)
from sys import maxsize

def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
    
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
            
         
    return max_so_far
 
def maxSubArraySize(a,size):
 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,size):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
 
    return (end - start + 1)
    
    
a = list(map(int,input().split()))
print(maxSubArraySum(a,len(a)))
print(maxSubArraySize(a,len(a)))

'''
-1 -2 1
1
1
'''
def waysToPaint(n):
 
    # Count of ways to pain a
    # row with same colored ends
    same = 6
 
    # Count of ways to pain a row
    # with different colored ends
    diff = 6
 
    # Traverse up to (N - 1)th row
    for _ in range(n - 1):
 
        # Calculate the count of ways
        # to paint the current row
 
        # For same colored ends
        sameTmp = 3 * same + 2 * diff
 
        # For different colored ends
        diffTmp = 2 * same + 2 * diff
 
        same = sameTmp
        diff = diffTmp
        
    print(same)
    print(diff)
    # Print the total number of ways
    print(same + diff)
 
 
# Driver Code
 
N = int(input())
waysToPaint(N)


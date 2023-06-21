from bisect import bisect_left
def maximumLen(nums):

        list = []
        for num in nums:
            pos = bisect_left(list, num )
            if pos == len(list):
                list.append( num )
            else:
                list[ pos ] = num
                
        print(len(list)-1)

def maxBoxes(boxes):
        
        sortedBoxes = sorted( boxes, key=lambda coord: (coord[0],coord[1],-coord[2]) )
        maximumLen( z for x,y,z in sortedBoxes )
 
 
n=int(input())

boxes=[]

for x in range(0,n):
    boxes.append(list([int(item) for item in input().split()]))
maxBoxes(boxes)



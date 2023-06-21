
import math
import os
import random
import re
import sys

def twoPluses(grid):
    empty = []    
    count = 0    
    for i in range(1, n - 1, 1):
        for j in range(1,len(grid[i]) - 1 , 1):
            if grid[i][j] == 'N':
                for inl in range(min(m - j - 1, n - i - 1, i , j)):
                    ls = []
                    count = 0
                    for k in range(-min(m - j - 1, n - i - 1, i , j) + inl, min(m - j - 1, n - i - 1, i , j)+1 - inl , 1):
                        if (grid[i + k][j] == "N"):
                            ls.append([i + k,j])
                            count = count + 1
                        if (grid[i][j + k] == "N") & (k != 0):
                            ls.append([i,j + k])                        
                            count = count + 1
                    if (count+1) == len(range(-min(m - j - 1, n - i - 1, i , j) + inl, min(m - j - 1, n - i - 1, i , j)+1 - inl , 1))*2:
                        empty.append(ls)
        max_area = 1
    check = empty    
    if len(empty) > 2:
        for arr in range(len(check)):
            for nex in range(arr, len(check),1):
                if arr != nex:
                    cnt = 0
                    for x in check[arr]:
                        for y in check[nex]:
#                            print(x,y)                            
                            if (x[0] == y [0]) & (x[1] == y[1]):
                                cnt = cnt + 1
#                                print(cnt)
                                break
                    if (cnt == 0) & (max_area < (len(check[arr])*len(check[nex]))):
                        
                        max_area = len(check[arr])*len(check[nex])
    elif len(empty) == 2:
        for arr in range(len(check)):
            for nex in range(arr, len(check),1):
                if arr != nex:
                    cnt = 0
                    for x in check[arr]:
                        for y in check[nex]:         
                            if (x[0] == y [0]) & (x[1] == y[1]):
                                cnt = cnt + 1
                            break
            if cnt == 1:
                max_area = max((len(check[arr]),len(check[nex])))
            else:
                max_area = (len(check[arr])*len(check[nex]))
    elif len(check) == 1:
        max_area = len(check[0])
    else:
        max_area = max_area
    return max_area    
 
 
if __name__ == '__main__':
 
    nm = input().split()
 
    n = int(nm[0])
 
    m = int(nm[1])
 
    grid = []
 
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
        
    bol=False
    for x in range(0,n):
        for y in range(0,m):
            if(grid[x][y]=="N"):
                bol=True
    if(bol==True):
        result = twoPluses(grid)
        print(str(result) + '\n')
    else:
        print(0)

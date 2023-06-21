
str=(input())
res = [str[i: j] for i in range(len(str))
          for j in range(i + 1, len(str) + 1)]
big=0    
for x in res:
    if(len(x)==int(x,2)):
        if(len(x)>big):
            big=len(x)
print(big)

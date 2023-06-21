import sys
import bisect
 
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
 
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
 
scores = list(sorted(set(scores)))
 
 
for x in alice:
    j=0
    rank=1
    scores.append(x)
    scores=sorted(scores,reverse=True)
    if(x>scores[0]):
        print(1)
    else:
        while(x<scores[j] and scores[j]!=scores[j-1]):
            j=j+1
            rank=rank+1
        print(rank)
 

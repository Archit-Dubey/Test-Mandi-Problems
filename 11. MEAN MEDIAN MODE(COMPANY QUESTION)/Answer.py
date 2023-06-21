import statistics
from collections import Counter
n=int(input())
unionList=[]
for _ in range(n):
    unionList=unionList+(list(map(int, input().replace("[", "").replace("]", "").split(","))))
unionList = sorted(unionList)
print(round(float(statistics.mean(unionList)),4))
print((round(float(statistics.median(unionList)),4)))
 
def most_frequent(List):
    occurence_count = Counter(List)
    if(occurence_count.most_common(2)[0][1]!=occurence_count.most_common(2)[1][1]):
        print(occurence_count.most_common(2)[0][0])

most_frequent(unionList)

from statistics import geometric_mean,harmonic_mean
from collections import Counter
def most_frequent(List):
    occurence_count = Counter(List)
    if(occurence_count.most_common(2)[0][1]!=occurence_count.most_common(2)[1][1]):
        print(occurence_count.most_common(2)[0][0])
unionList=[]
unionList=(list(map(int, input().replace("[", "").replace("]", "").split(","))))
unionList = sorted(unionList)
most_frequent(unionList)
print(round(geometric_mean(unionList),4))
print(round(harmonic_mean(unionList),4))

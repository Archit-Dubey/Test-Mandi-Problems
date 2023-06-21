from collections import OrderedDict 
a="".join(OrderedDict.fromkeys(input()))
b="".join(OrderedDict.fromkeys(input()))
stuff=(list(sorted(set(a)&set(b))))
ans=[]
for x in stuff:
    ans1=a.split(x)
    ans2=b.split(x)
    ans.append(ans1[0]+x+ans2[1])
    ans.append(ans2[0]+x+ans1[1])
print("\n".join(sorted(ans)))
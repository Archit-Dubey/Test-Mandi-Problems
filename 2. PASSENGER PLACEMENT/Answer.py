n=int(input()) # Number of Compartments

bookedArr=list([int(item) for item in input().split()]) # Booked Seats

total=[]
comp=[]
leftArr=[]
rightArr=[]
uArr=[]
mArr=[]
lArr=[]

for x in range(0,n):
    arr=[]
    for y in range((x*8 + 1),((x*8+1) + 8)):
        arr.append(y)
        if(y in range((x*8 + 1),((x*8+1) + 6))):
            leftArr.append(y)
        if(y in range((x*8 + 7),((x*8+1) + 8))):
            rightArr.append(y)
        if(y == (x*8 + 1) or y == (x*8 + 4) or y == (x*8 + 7)):
            uArr.append(y)
        elif(y == (x*8 + 2) or y == (x*8 + 5)):
            mArr.append(y)
        elif(y == (x*8 + 3) or y == (x*8 + 6) or y == (x*8 + 8)):
            lArr.append(y)
        total.append(y)
    comp.append(arr)

unbookedArr=list(set(total)-set(bookedArr))

choice=input().split()

def calcTemp(arr1,arr2):
    return [value for value in arr1 if value in arr2]
temp1=[]
if(choice[1] == "L"):
    if(choice[2]=="U"):
        temp1 = calcTemp(leftArr,uArr)
        
    if(choice[2]=="M"):
        temp1 = calcTemp(leftArr,mArr)
        
    if(choice[2]=="L"):
        temp1 = calcTemp(leftArr,lArr)
        
    if(choice[2]=="N"):
        temp1.extend(calcTemp(leftArr,uArr))
        temp1.extend(calcTemp(leftArr,mArr))
        temp1.extend(calcTemp(leftArr,lArr))

 
if(choice[1] == "R"):
    if(choice[2]=="U"):
        temp1 = calcTemp(rightArr,uArr)
        
    if(choice[2]=="M"):
        temp1 = calcTemp(rightArr,mArr)
        
    if(choice[2]=="L"):
        temp1 = calcTemp(rightArr,lArr)
        
    if(choice[2]=="N"):
        temp1.extend(calcTemp(rightArr,uArr))
        temp1.extend(calcTemp(rightArr,mArr))
        temp1.extend(calcTemp(rightArr,lArr))

if(choice[1] == "N"):
    if(choice[2]=="U"):
        temp1.extend(calcTemp(leftArr,uArr))
        temp1.extend(calcTemp(rightArr,uArr))
    if(choice[2]=="M"):
        temp1.extend(calcTemp(leftArr,mArr))
        temp1.extend(calcTemp(rightArr,mArr))
    if(choice[2]=="L"):
        temp1.extend(calcTemp(leftArr,lArr))
        temp1.extend(calcTemp(rightArr,lArr))
        
    if(choice[2]=="N"):
        temp1.extend(calcTemp(leftArr,uArr))
        temp1.extend(calcTemp(rightArr,uArr))
        temp1.extend(calcTemp(leftArr,mArr))
        temp1.extend(calcTemp(rightArr,mArr))
        temp1.extend(calcTemp(leftArr,lArr))
        temp1.extend(calcTemp(rightArr,lArr))

temp2=[]

if(choice[0]!="N"):
    index=comp[int(choice[0]) - 1]
    temp2 = [value for value in temp1 if value in index]

elif(choice[0]=="N"):
    for index in comp:
        temp2.extend([value for value in temp1 if value in index])
    
final= [value for value in temp2 if value in unbookedArr]

print(final)
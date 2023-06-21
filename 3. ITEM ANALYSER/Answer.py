itemQty=int(input())
arr=[]
for x in range(0,itemQty):
    arr.append(input().split())

#[Item Number, Item Name, Price, Stock]

itemNum = input()
qty = input()
bool1=any(c.isalpha() for c in str(itemNum))
bool2=any(c.isalpha() for c in str(qty))

if(bool1==False and bool2==False):
    
    if(int(itemNum)<101 or int(itemNum)>199):
        print("INVALID INPUT")
    
    else:
        itemNum=int(itemNum)-101
       
            
 
        try:
            if(int(qty)<=int(arr[int(itemNum)][3])):
                print(int(qty)*int(arr[int(itemNum)][2]))
                print(int(arr[int(itemNum)][3]) - int(qty))
            elif(int(qty)>int(arr[int(itemNum)][3])):
                print("NOT ENOUGH STOCK")

        except IndexError:
            print("INVALID INPUT")

else:
    print("INVALID INPUT")

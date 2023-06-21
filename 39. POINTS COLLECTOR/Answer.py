class Solution:
    def maxBalls(self, N, M, a, b):
        # code here

        i=0
        j=0
        temp1=0
        temp2=0
        result=0
        current1, current2=-1,-1
        while i<N and j<M:
            if a[i]>b[j]:
                temp2+=b[j]
                j+=1
            elif a[i]<b[j]:
                temp1+=a[i]
                i+=1
            else:
                temp1+=a[i]
                temp2+=b[j]
                i+=1
                j+=1
                while i<N and a[i]==a[i-1]:
                    temp1+=a[i]
                    i+=1
                while j<M and b[j]==b[j-1]:
                    temp2+=b[j]
                    j+=1
                current1=i
                current2=j
                if temp1>=temp2:
                    result+=temp1
                else:
                    result+=temp2
                temp1=0
                temp2=0
        while j<M:
            temp2+=b[j]
            j+=1
        while i<N:
            temp1+=a[i]
            i+=1
        if temp1>=temp2:
            result+=temp1
        else:
            result+=temp2
        
        return result   

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

        N, M = [int(x) for x in input().split()]
        a = input().split()
        b = input().split()
        for i in range(N):
            a[i] = int(a[i])
        for i in range(M):
            b[i] = int(b[i])
        
        ob = Solution()
        print(ob.maxBalls(N, M, a, b))

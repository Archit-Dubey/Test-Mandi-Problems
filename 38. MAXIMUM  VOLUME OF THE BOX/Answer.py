def maxVol(P, A):
 
    l = (P - (P * P - 24 * A)**0.5) / 12
    V = l * (A / 2.0 - l * (P / 4.0 - l))
    return V
 
 

if __name__ == '__main__':
    P = float(input())
    A = float(input())
    print(format(maxVol(P, A),".4f"))
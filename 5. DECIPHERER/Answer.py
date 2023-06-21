
import math

def decrypt(k, text):

    numC = math.ceil(len(text) / k)

    numR = k

    numS = (numC * numR) - len(text)

    answer = [''] * numC

    col = 0
    row = 0

    for symbol in text:
        answer[col] += symbol
        col += 1

        if (col == numC) or (col == numC - 1 and row >= numR - numS):
            col = 0
            row += 1

    return ''.join(answer)

myMessage =input()
myKey = int(input())
answer = decrypt(myKey, myMessage)
print(answer)
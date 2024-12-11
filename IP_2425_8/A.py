import sys

def readArray():
    try:
        a = input().split(" ")
    except:
        sys.exit(0)
    for i in range(0, len(a)):
        a[i] = int(a[i])
    return a;

def obterPosicaoEquilibrio(a):
    leftSums = [0]
    rightSums = [0]
    currentSum = 0
    for i in range(0, len(a) - 1):
        currentSum += a[i]
        leftSums.append(currentSum)
    
    currentSum = 0
    for i in range(len(a) - 1, 0, -1):
        currentSum += a[i]
        rightSums.append(currentSum)
    
    rightSums = rightSums[::-1]
    
    print(leftSums, rightSums)
    for i in range(0, len(a)):
        if (leftSums[i] == rightSums[i]):
            return i
    return -1
        
def main():
    a = readArray()
    posicaoEquilibrio = obterPosicaoEquilibrio(a)
    print(posicaoEquilibrio)

if __name__ == "__main__":
    main()
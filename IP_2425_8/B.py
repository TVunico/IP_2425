import sys

def readArray():
    try:
        a = input().split(" ")
    except:
        sys.exit(0)
    for i in range(0, len(a)):
        a[i] = int(a[i])
    return a;

def getSleepOverTotalMadeInMonth(rendimentoAnual, dormidasPorMes, start, end):
    totalSleepOvers = 0
    for i in range(start, end):
        totalSleepOvers += dormidasPorMes[i]
    
    sleepOverPrice = rendimentoAnual / totalSleepOvers
    
    totalMadePerMonth = []
    for i in dormidasPorMes:
        totalMadePerMonth.append(sleepOverPrice * i)
    
    return totalMadePerMonth
    
def main():
    rendimentosAnuais = readArray()
    dormidasPorMes = readArray()
    if (len(dormidasPorMes) != len(rendimentosAnuais) * 12):
        sys.exit(0)
    result = []
    for i in range(0, len(rendimentosAnuais)):
        temp = getSleepOverTotalMadeInMonth(rendimentosAnuais[i], dormidasPorMes, 0 + i * 12, 12 + i * 12)
        print(temp)
        result.extend(temp)
    print(result)

if __name__ == "__main__":
    main()
    
# 321432 43456
# 30 20 10 15 20 34 23 12 23 34 30 15 32 23 15 17 22 31 25 12 23 32 30 16
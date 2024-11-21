import sys

def floats_get():
    a = []
    try:
        line = input().split()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)
    if line:
        for i in line:
            a.append( float(i))
    return a

def getListGoals():
    try:
        lenGroups = int(input())
        hatTricks = floats_get()
        if len(hatTricks) == 0:
            return (lenGroups, hatTricks)
    except:
        sys.exit(0)
    
    return (lenGroups, hatTricks)

def getHatTricksPerGroupd(lenGroups, hatTricks):
    if not hatTricks:
        return []
    hatTrickslen = len(hatTricks)
    hatTricksPerGroup = []
    externalCounter = 0
    for i in range(0, hatTrickslen - lenGroups, lenGroups):
        hatTrickCounter = 0
        for j in range(i , i + lenGroups):
            if (hatTricks[j] >= 3):
                hatTrickCounter += 1
        hatTricksPerGroup.append(hatTrickCounter)
        externalCounter += lenGroups
    hatTrickCounter2 = 0
    for i in range(externalCounter + 1, hatTrickslen):
        if (hatTricks[i] >= 3):
                hatTrickCounter2 += 1
    hatTricksPerGroup.append(hatTrickCounter2)
    return hatTricksPerGroup

def int_println_bracket(a):
	print("[", end='')
	if (len(a) > 0):
		print("%d" % a[0], end='')
		for i in range(1, len(a) ):
			print(" %d" % a[i], end='')
	print("]")
          
def main():
    lenGroups, hatTricks = getListGoals()
    hatTricksPerGroup = getHatTricksPerGroupd(lenGroups, hatTricks)
    int_println_bracket(hatTricksPerGroup)
    
if __name__ == "__main__":
    main()
    
    
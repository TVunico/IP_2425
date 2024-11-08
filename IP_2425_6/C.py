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


def floats_println_bracket(a):
	print("[", end='')
	if (len(a) > 0):
		print("%g" % a[0], end='')
		for i in range(1, len(a) ):
			print(" %g" % a[i], end='')
	print("]")
 
 
def floats_take(a, x, b):
    for index in range(0, x):
        b.append(a[index])
    return b

def floats_drop(a, x, b):
    for index in range(x, len(a)):
        b.append(a[index])
    return b
    

 
def main():
    try:
        x = int(input())
        a = floats_get()
    except:
        sys.exit(0)
    
    if (x > len(a)): x = len(a)
    b = []
    floats_take(a, x, b)
    floats_println_bracket(b)
    b =[]
    floats_drop(a, x, b)
    floats_println_bracket(b)
    

if __name__ == "__main__":
    main()
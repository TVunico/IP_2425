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
 
 
def floats_append(a, b, c):
    for num in a:
        c.append(num)
    for num in b:
        c.append(num)
    return len(c)
 
 
def main():
    a = floats_get()
    b = floats_get()
    c = []
    floats_append(a, b, c)
    floats_println_bracket(c)
    
    
    
    
if __name__ == "__main__":
    main()
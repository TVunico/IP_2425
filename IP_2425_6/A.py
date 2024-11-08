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
 
def floats_large(a, n, b):
    for num in a:
        if num > n:
            b.append(num)
    
def floats_small(a, n, b):
    for num in a:
        if num < n:
            b.append(num)
                        
def floats_equal(a, n, b):
    for num in a:
        if num == n:
            b.append(num)
    
def main():
    b = []
    n = int(input())
    array = floats_get()
    floats_large(array, n, b)
    floats_println_bracket(b)
    b = []
    floats_small(array, n, b)
    floats_println_bracket(b)
    b = []
    floats_equal(array, n, b)
    floats_println_bracket(b)
    
    
    
if __name__ == "__main__":
    main()
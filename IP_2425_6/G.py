import sys


def floats_find_triple(a):
    for i in range(0, len(a) - 2):
        if (a[i] == a[i + 1] == a[i + 2]):
            return i
    return -1

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


def main():
    try:
        a = floats_get()
    except:
        sys.exit(0)
    print (floats_find_triple(a))



if __name__ == "__main__":
    main()
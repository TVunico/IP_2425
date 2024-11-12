import sys


def floats_accumulate(a, b):
    if (len(a) == 0): 
        return
    soma = 0
    for num in a:
        soma = num + soma
        b.append(soma)
    return len(b)


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
        b = [0]
        a = floats_get()
    except:
        sys.exit(0)
    floats_accumulate(a,b)
    floats_println_bracket(b)
        




if __name__ == "__main__":
    main()
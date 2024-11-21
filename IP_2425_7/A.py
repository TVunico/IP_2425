import sys


def floats_get():
    a = []
    try:
        line = input().split()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)
    if line:
        for i in line:
            try:
                a.append( float(i))
            except ValueError:
                sys.exit(0)
    return a


def floats_println_bracket(a):
	print("[", end='')
	if (len(a) > 0):
		print("%g" % a[0], end='')
		for i in range(1, len(a) ):
			print(" %g" % a[i], end='')
	print("]")




def gasolina_baixou(a):
    d = 0
    for i in range(1 , len(a)):
        if a[-i] < a[-i -1]:
            d += 1
    return d




def verificar(a):
    if a > 0:
        print (a)
    else:
        print ("void")
    
                
    
def main():
    try:
        a = floats_get()
        for num in a:
            if num <= 0:
                sys.exit(0)
    except:
        sys.exit(0)
    if len(a) > 0 and len(a) <= 1000:
        count = gasolina_baixou(a)
        verificar(count)


if __name__ == "__main__":
    main()
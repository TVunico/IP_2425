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

def main():

    def read_prices():
        try:
            prices = list(map(float, input().strip().split()))
            return prices
        except EOFError:
            return []

    prices = read_prices()

    if len(prices) < 2:
        print("void")
        return

    last_increase_day = -1
    first_decrease_day = -1 


    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            last_increase_day = i
            first_decrease_day = -1 
        elif prices[i] < prices[i - 1]:
            if last_increase_day != -1 and first_decrease_day == -1:
                first_decrease_day = i
    if first_decrease_day == -1 or last_increase_day == -1:
        print("void")
    else:
        days_since_decrease = len(prices) - first_decrease_day
        print(days_since_decrease)

if __name__ == "__main__":
    main()     



def gasolina_baixou(a):
    maior = a[0]
    c = 0
    for i in range(1, len(a)):
        if  a[i] >= maior:
            c = 0
            maior = a[i]
        elif c == 0:
            c = i
        
    return len(a)-i
    
        




def verificar(a):
    if a > 0:
        print (a)
    else:
        print ("void")
    
                
    
def main2():
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
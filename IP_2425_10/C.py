import sys
"""Funcao para ler um array de um array de float, necessita especificar qual o numero de linhas a intuduzir (valor n)"""
def list_get(n):
	a = []
	try:
		for i in range(0,n):
			a.append( list( float(x) for x in input().split() ) )
	except (EOFError, KeyboardInterrupt):
		sys.exit(0)
	return a

def list_println_bracket(a):
	print("[", end='')
	if (len(a) > 0):
		for i in range(0, len(a) ):
			print(" [", end='')
			if len(a[i])>0:
				print("%g" % a[i][0], end='')
			for j in range(1,len(a[i])):
				print(" %g" % a[i][j], end='')
			print("]", end='')
	print(" ]")
 
def getBestSellers(lista):
    productCount = {}
    for i in lista:
        if i[2] not in productCount:
            productCount[i[2]] = 1
        else:
            productCount[i[2]] += 1
    
    bestSellers = [[key, value] for key, value in productCount.items()]
    bestSellers.sort(key = lambda x: (-x[1], -x[0]))
    
    
    list_println_bracket(bestSellers[:5])
    
    

def main():
    n = int(input())
    lista = list_get(n)
    getBestSellers(lista)

if __name__ == "__main__":
    main()

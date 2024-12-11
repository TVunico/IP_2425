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






QUALITY = [1.1,1.1]

def distanceBetween2Points(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def checkQuality(qualities):
    for quality in qualities:
        if distanceBetween2Points(quality, QUALITY) < 1:
            print(True)
        else:
            print(False)

      
def main():
    n = int(input())
    lista = list_get(n)
    checkQuality(lista)
    
if __name__ == "__main__":
    main()
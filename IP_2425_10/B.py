import sys
import math
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

def calculateContainer(lista):
    for dia in lista:
        containers = 0
        for quantidadeModelo in dia:
            containers = containers + math.ceil(quantidadeModelo / 4)
        print(containers)
    
def main():
    n = int(input())
    lista = list_get(n)
    calculateContainer(lista)

if __name__ == "__main__":
    main()
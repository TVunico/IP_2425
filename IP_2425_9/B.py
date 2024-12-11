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



"""Funcao que serve para printar arrays de arrays"""
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
 
def media(n):
    temperaturas = []
    for i in range(len(n)):
        media = (n[i][0] + n[i][1]) / 2
        if media >= 25:
            temp = [n[i][0], n[i][1], media]
            temperaturas.append(temp)
    temperaturas.sort(key = lambda x: x[2], reverse=True)
    list_println_bracket(temperaturas[:5])
    
def main(): 
    n = int(input())
    lista = list_get(n)
    media(lista)
    

if __name__ == "__main__":
    main()
    
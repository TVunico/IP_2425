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



"""Funcao que recebe os dados de entrada"""
def test_list():
	n = input()
	a = list_get(int(n))
	list_println_bracket(a)



"""realiza a soma da precipitacao total da posicao de cada coluna"""
def precipitacao(n):
    limite = 0
    soma0 = 0
    soma1 = 0
    max0 = 0
    max1 = 0
    dias0 = 0
    dias1 = 0
    maxcount0 = 0
    maxcount1 = 0
    current0 = 0
    current1 = 0
    while n > limite:
        line = input().split(" ")
        n0 = float(line[0])
        n1 = float(line[1])
        if (n0 > max0):
            max0 = n0
        if (n1 > max1):
            max1 = n1
        if (n0 > 0):
            dias0 += 1
        if (n1 > 0):
            dias1 += 1
        if (n0 > 0):
            current0 += 1
        else:
            current0 = 0
        if (n1 > 0):
            current1 += 1
        else:
            current1 = 0
        soma0 = soma0 + n0
        soma1 = soma1 + n1
        limite += 1
        maxcount0 = max(current0, maxcount0)
        maxcount1 = max(current1, maxcount1)
    print ("%.1f" % soma0, "%.1f" % soma1)
    print(max0, max1)
    print(dias0, dias1)
    print(maxcount0, maxcount1)
    
    	
     

def main(): 
    n = int(input())
    precipitacao(n)


if __name__ == "__main__":
    main()
    
    
    
    
"""

10
0.0 4.6
0.0 0.0
4.9 5.0
3.5 2.8
0.1 0.0
0.0 0.2
0.0 0.0
0.8 0.0
0.0 1.2
4.8 5.8

"""

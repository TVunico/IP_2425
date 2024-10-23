import sys


def sum_inverses(n):
    resultado = 0
    for i in range (1, n + 1):
        resultado = resultado + 1/i;
    return resultado


def sum_inverse_squares(n):
    resultado = 0;
    for i in range(1, n+1):
        resultado = resultado + 1 / (i*i)
    return resultado
        
def test_two_sequences():
	for line in sys.stdin:
		n = line
		z1 = sum_inverses(int(n))
		print("%f" % z1)
		z2 = sum_inverse_squares(int(n))
		print("%f" % z2)

def main():
    test_two_sequences()
            
if __name__ == "__main__":
    main()
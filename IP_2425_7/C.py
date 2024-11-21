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
    
    
def trimester(a):
    medias = []
    media = 0
    for i in range (0 , len(a)-2, 3):
        media = (a[i] + a [i+1]+ a[i+2]) / 3
        medias.append(media)
    return medias

def maximo(a):
    max = a[0]
    ano = 2022
    max_trimestre = 4
    max_ano = 2022
    trimestre = 4 
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
            max_trimestre = trimestre
            max_ano = ano
        trimestre -= 1
        if trimestre == 0:
            trimestre = 4
            ano -=1
    return [max_trimestre,max_ano]
   # return max(a)
            
        
        
        
            
        
            
            
    
    
    
def main():
    try:
        a = floats_get()
        for num in a:
            if num <= 0:
                sys.exit(0)
    except:
        sys.exit(0)
    medias = trimester(a)
    resultado = maximo (medias)
    print(resultado[1], resultado[0])
        
        
if __name__ == "__main__":
    main()
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
 
 
def hat_tricks(grupos_jogos , golos_jogo):
    c = 0
    n = 0
    golos_grupo = []
    for i in range (0 , len(golos_jogo)):
        if golos_jogo[i] >= 3:
            n += 1
        c += 1
        if c >= grupos_jogos:
            golos_grupo.append(n)
            c = 0
            n = 0
    if c > 0:
        golos_grupo.append(n)
    return golos_grupo
        
        
            
            
 
def main():
    try:
        grupos_jogos = int(input())
        golos_jogo = floats_get()
    except:
        sys.exit(0)
    resultado = hat_tricks(grupos_jogos,golos_jogo)
    floats_println_bracket(resultado)
    
    

 
 
 
if __name__ == "__main__":
    main()
    
    
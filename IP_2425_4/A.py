import sys
TAXA_MINIMA=2.5
TAXA_BASE=1.1

def uber(t,d):
    custo_t = 0.11 * t
    custo_d = 0.82 * d
    return TAXA_BASE + custo_t + custo_d

def test_uber():
    for line in sys.stdin:
        line = line.split(" ")
        try:
            t = int(line[0])
            d = float(line[1])
        except: sys.exit(0)
        
        if t < 0 or d < 0: sys.exit(0)
        preco = uber(t,d)
        if preco < TAXA_MINIMA:
            preco = TAXA_MINIMA
        print("%.2f" % preco)

def main():
    test_uber()
    
    
if __name__ == "__main__":
    main()
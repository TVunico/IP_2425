import sys
import math

CONV_POLEGADAS = 2.54
CONV_PES = 30.48

def nbanba(pes,pol):
    pes_cm = pes * CONV_PES
    pol_cm = pol * CONV_POLEGADAS
    metros = (pes_cm + pol_cm) / 100
    return round(metros,2)


def test_nbanba():
    for line in sys.stdin:
        line = line.split()
        try:
            pes = int(line[0])
            pol = int(line[1])
        except: sys.exit(0)
        
        if pes < 0 or pol < 0:
            sys.exit(0)
        print("%.6f" %  nbanba(pes,pol))
        
def main():
    test_nbanba()
        
        



if __name__ == "__main__":
    main()
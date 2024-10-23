import sys
def get_retire_age(ano, mes):
    if (ano < 26 or (ano == 26 and mes <= 7)):
        return (66, 7)
    else:
        idade_reforma = ano + 40
        if (idade_reforma > 70):
            return (70, 0)
        return (idade_reforma, mes)

def test_retire_age():
    for line in sys.stdin:
        line_split = line.split(" ")
        if len(line_split) != 2: sys.exit(0)
        try:
            ano = int(line_split[0])
            mes = int(line_split[1])
        except Exception:
            sys.exit(0)
        
        # Valores invalidos para o mes e ano.
        if ano < 0 or mes < 0 or mes > 12 or ano > 70:
            sys.exit(0)
        
        
        idade_reforma = get_retire_age(ano, mes)
        print(idade_reforma[0], idade_reforma[1])

def main():
    test_retire_age()
    
    
if __name__ == "__main__":
    main()
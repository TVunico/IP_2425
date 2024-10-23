import sys


def sum_squares_i(n):
    result = 0
    for i in range(1, n):   
        result = result + i * i
    return result

def main():
    while True:
        try:
            line = input().split()
        except Exception:
            sys.exit(0)
        if line:
            n = line[0]
            try:
                z = sum_squares_i(int(n))
            except:
                sys.exit(0)
                
            print("%.6f" % z)
            
if __name__ == "__main__":
    main()
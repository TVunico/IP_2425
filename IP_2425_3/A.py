import sys


def sum_arithmetic(x0, r, n):
    return x0 + sum_arithmetic(x0 + r, r, n-1) if n else 0


def main():
    while True:
        try:
            line = input().split()
        except Exception:
            sys.exit(0)
        if line:
            x0, r, n = line
            try:
                z = sum_arithmetic(float(x0), float(r), int(n))
            except:
                sys.exit(0)
            print("%.6f" % z)
            
if __name__ == "__main__":
    main()
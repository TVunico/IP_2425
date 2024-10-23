def sum_progression(x0,r,n,):
    return x0 + (n - 1) * r


def main():
    x0 = int(input())
    r = int(input())
    n = int(input())
    sum_final = ((x0 + sum_progression(x0,r,n)) * n) / 2
    print(sum_final)

if __name__ == "__main__":
    main()
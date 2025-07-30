def simple_interest(p: float, n: float, r: float) -> tuple[float, float]:
    i = (p * n * r) / 100
    a = p + i
    return i, a


def main():
    p = float(input("Enter Principal in INR : "))
    n = float(input("Enter number of Years : "))
    r = float(input("Enter Rate of interest in %.p.a. : "))
    i, a = simple_interest(p, n, r)
    print(f"Simple Interest : {i:.2f} INR")
    print(f"Amount : {a:.2f} INR")


if __name__ == "__main__":
    main()

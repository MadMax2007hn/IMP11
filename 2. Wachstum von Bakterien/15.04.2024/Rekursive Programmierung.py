def amount(n):
    print(n)
    if n == 0:
        return 1
    else:
        return amount(n-1) * 2

print(amount(991))
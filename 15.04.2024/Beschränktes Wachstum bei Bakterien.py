

def amount(n):
    if n == 0:
        return 1
    else:
        return amount(n + (1/59) * (60-(n-1))


print(amount(10))
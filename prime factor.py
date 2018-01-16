#Program will prompt user to input a number, then give them the result.


num = int(input("Enter a number to see its prime factorization:  "));

def Prime(num):
    factors = []
    if num == 1 or 0:
        return ("No factors")
    while True:
        if num // 9 == 0:
            num = num / 9
            factors.append(9)
        else:
            break
    while True:
        if num // 7 == 0:
            num = num / 7
            factors.append(7)
        else:
            break
    while True:
        if num // 5 == 0:
            num = num / 5
            factors.append(5)
        else:
            break
    while True:
        if num // 3 == 0:
            num = num / 3
            factors.append(3)
        else:
            break
    while True:
        if (num / 2).is_integer():
            num = num / 2
            factors.append(2)
        else:
            break
    if num != 1:
        factors.append(int(num));
    return (factors)

print (Prime(num))

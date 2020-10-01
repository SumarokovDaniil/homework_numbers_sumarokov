def ft_straight_code(a):
    if a > 0:
        b = ''
        while a > 0:
            c = str(a % 2)
            b = c + b
            a = int(a / 2)
        while len(b) != 8:
            b = '0' + b
        return b
    else:
        a = a * -1
        b = ''
        while a > 0:
            c = str(a % 2)
            b = c + b
            a = int(a / 2)
        while len(b) != 7:
            b = '0' + b
        b = '1' + b
        return b

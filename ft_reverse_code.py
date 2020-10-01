def ft_reverse_code(a):
    x = a
    if a > 0:
        b = ''
        while a > 0:
            c = str(a % 2)
            b = c + b
            a = int(a / 2)
        while len(b) != 8:
            b = '0' + b
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
    a = '1'
    if x > 0:
        return b
    else:
        for i in b[1:]:
            if i == '0':
                a = a + '1'
            else:
                a = a + '0'
        return a

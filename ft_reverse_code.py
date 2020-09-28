def ft_reverse_code(g):
    s = g
    if g > 0:
        f = ''
        while g > 0:
            n = str(g % 2)
            f = n + f
            g = int(g / 2)
        while len(f) != 8:
            f = '0' + f
    else:
        g = g * -1
        f = ''
        while g > 0:
            n = str(g % 2)
            f = n + f
            g = int(g / 2)
        while len(f) != 7:
            f = '0' + f
        f = '1' + f
    a = '1'
    if s > 0:
        return f
    else:
        for i in f[1:]:
            if i == '0':
                a = a + '1'
            else:
                a = a + '0'
        return a

def ft_additional_code(r):
    b = ""
    if r >= 0:
        while r:
            b = r % 2
            if b == 0:
                b = b + 0
            else:
                b = b + 1
        r = r // 2
        while len(b) < 8:
            b = b + 0
        print(b)
    else:
        r = r * (-1)
        while r:
            v = r % 2
            if v == 0:
                b = b + 1
            else:
                b = b + 0
            r = r // 2
        while len(b) < 8:
            b = 1 + b
        print(b)

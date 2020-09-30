def ft_bin_num(number):
    p = 1
    d = 0
    while number > 0:
        d += number % 2 * p
        p *= 10
        number //= 2
    return d

def ft_straight_code(number):
    if number > 0:
        b = ''
        while number > 0:
            c = str(number % 2)
            b = c + b
            number = number // 2
        while len(b) != 8:
            b = '0' + b
        return b
    else:
        number = number * -1
        n = ''
        while number > 0:
            c = str(number % 2)
            b = c + b
            number = number // 2
        while ft_len(b) != 7:
            b = '0' + b
        b = '1' + b
        return b

def ft_reverse_code(number):
    return ft_straight_code(number)[::-1]

def ft_pow(number, s):
    previous = number
    if s > 0:
        for i in range(s - 1):
            number *= previous
        return number
    elif s == 0:
        return 1
    for i in range(number):
        number /= previous
    return number


def ft_rev_bin_num(number):
    temp = number
    bin_number = 0
    count_digits = 0
    while temp > 0:
        temp //= 10
        count_digits += 1
    for digit in range(count_digits):
        bin_number += number % 10 * ft_pow(2, digit)
        number //= 10
    return bin_number

def ft_additional_code(number):
    q = str(rev.ft_reverse_code(number))
    w = int(r) % 10000000
    r = q[0]
    return r + str(ft_bin_num(ft_rev_bin_num(w) + 1))

def ft_len(string):
    count = 0
    for i in string:
        count += 1

    return count

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

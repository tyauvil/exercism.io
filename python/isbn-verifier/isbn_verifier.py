def verify(isbn):
    if len(isbn) == 0:
        return False
    
    result = []
    
    for n in isbn:
        if n.isnumeric():
            result.append(n)

    if isbn[-1] == 'X':
        result.append(10)

    if len(result) != 10:
        return False
    else:
        r = 0
        x = 10
        for i in range(10):
            r += (int(result[i])*x)
            x -= 1
    
    return r%11 == 0

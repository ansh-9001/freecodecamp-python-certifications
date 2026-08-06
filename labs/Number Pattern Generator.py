def number_pattern(n):
    pattern = []
    if type(n) == int:
        if n > 0:
            for n in range(1,n+1):
                pattern.append(str(n))
            return ' '.join(pattern)
        else:
            return 'Argument must be an integer greater than 0.'
    else:
        return 'Argument must be an integer value.'

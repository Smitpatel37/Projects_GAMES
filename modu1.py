def search(li, n):
    a = 0
    b = len(li) - 1
    while b - a > 1:
        new_limit = (a + b)//2
        if n == li[new_limit] or n == li[b]:
            return True
        elif n > li[new_limit]:
            a = new_limit
        else:
            b = new_limit
    return False

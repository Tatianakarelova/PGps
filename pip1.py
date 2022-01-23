def leapyr(x):
    if x % 400 == 0:
        return True
    if x % 100 == 0:
        return False
    if x % 4 == 0:
        return True
    else:
        return False
print ( leapyr(2020))
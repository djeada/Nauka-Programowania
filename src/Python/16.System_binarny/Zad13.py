def findMinV1(x, y):
    return y ^ ((x ^ y) & -(1 if (x < y) else 0))

def findMinV2(x, y):
    return y + ((x - y) & ((x - y) >> 31))

def findMaxV1(x, y):
    return x ^ ((x ^ y) & -(1 if (x < y) else 0))

def findMaxV2(x, y):
    return x - ((x - y) & ((x - y) >> 31))

if __name__ == '__main__':

    x, y = 2, 4

    print(f"min({x}, {y}) is", findMinV1(x, y))
    print(f"max({x}, {y}) is", findMaxV1(x, y))


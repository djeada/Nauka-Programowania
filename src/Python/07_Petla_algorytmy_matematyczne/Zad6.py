"""
Napisz funkcję, która dla otrzymanych dwóch liczb 
zwróci ich najmniejszą wspólną wielokrotność.
"""

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return a * b // nwd(a, b)

def test_nww():
    assert nww(12, 15) == 60
    assert nww(12, 16) == 48
    assert nww(12, 18) == 36

if __name__ == "__main__":
    
    test_nww() 
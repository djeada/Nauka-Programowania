"""
Dla pobranych czterech liczb, znajdz najwieksza liczbe. 
"""

if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    maks_ab = a if a > b else b

    maks_cd = c if c > d else d

    maks = maks_ab if maks_ab > maks_cd else maks_cd

    print(maks)

"""
Pobierz od użytkownika trzy długości boków i sprawdź, czy można z nich zbudować trójkąt.
"""

if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())

    if a + b > c and b + c > a and a + c > b:
        print("z podanych bokow mozna zbudowac trojkat")

    else:
        print("z podanych bokow nie mozna zbudowac trojkata")

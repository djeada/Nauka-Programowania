"""
Napisz funkcję, która dla otrzymanej liczby n, poprosi użytkownika 
o podanie n liczb i zwróci ich średnią arytmetyczną.
"""

def srednia_arytmetyczna(n):
    suma = 0
    for i in range(n):
        liczba = int(input('Podaj liczbę: '))
        suma += liczba
    return suma / n

if __name__ == "__main__":
    
    n = int(input('Podaj liczbę: '))
    print(srednia_arytmetyczna(n))


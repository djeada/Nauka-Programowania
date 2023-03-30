"""
Tytul: Suma elementow ciagu.
Tresc: Dla otrzymanej liczby naturalnej n, wypisz sume n pierwszych elementow ciagu danego wzorem:
$$a_n = n^2 + n + 1$$
$$a_n = n^2 + 5n$$
$$a_n = n + 2n$$
Wynik powinien zostac zaokraglony do najblizszej liczby naturalnej.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
* Dla otrzymanej liczby 2, w podpunkcie a) powinna zostac wypisana liczba 1.
* Dla otrzymanej liczby 2, w podpunkcie b) powinna zostac wypisana liczba 17.
* Dla otrzymanej liczby 2, w podpunkcie c) powinna zostac wypisana liczba 6.

"""

if __name__ == "__main__":

    print("Podaj liczbe n: ")
    n = int(input())

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = n/(n + 1) wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += i / (i + 1)

    print(suma)

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = (n^2 + 5)/n wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += (i ** 2 + 5) / i

    print(suma)

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = n + 2^n wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += i + 2 ** i

    print(suma)


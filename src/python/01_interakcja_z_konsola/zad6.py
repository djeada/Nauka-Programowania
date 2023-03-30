"""
Tytuł: Obliczanie wyników operacji arytmetycznych.
Treść zadania: Napisz program, który pobierze od użytkownika dwie liczby naturalne i wypisze wyniki następujących operacji arytmetycznych:
a) suma tych liczb
b) różnica pierwszej i drugiej liczby
c) iloczyn tych liczb
d) iloraz pierwszej liczby przez drugą
e) reszta z dzielenia pierwszej liczby przez drugą
f) pierwsza liczba podniesiona do potęgi równej drugiej liczbie
Dane wejściowe: Dwie liczby naturalne dla wszystkich podpunktów.
Dane wyjściowe: Liczba naturalna dla wszystkich podpunktów.
Przykład:
* Jeśli użytkownik poda liczby 9 oraz 1, program powinien wypisać liczby: 10, 1, 9, 9, 0, 9.
* Jeśli użytkownik poda liczby 3 oraz 2, program powinien wypisać liczby: 5, 1, 6, 1, 1, 9.

"""

if __name__ == "__main__":

    print("podaj wielkosc w kilogramach:")

    kilogramy = int(input())
    gramy = kilogramy * 1000

    print(kilogramy, " kg to ", gramy, " g")

    print("podaj wielkosc w calach:")

    cal = int(input())
    cm = cal / 2.54

    print(cal, " cali to", cm, " cm")

    print("podaj ilosc sekund:")

    sekundy = int(input())
    godziny = sekundy / 3600

    print(sekundy, " sekund to ", godziny, " godzin")

    print("podaj liczbe w euro:")

    euro = input()
    zloty = euro * 4.40

    print(euro, " euro to ", zloty, " zlotych")

    print("podaj miare kata w stopniach:")

    kat_stopnie = int(input())
    kat_rad = kat_stopnie * 0.0174532

    print(kat_stopnie, " stopni to ", kat_rad, " radianow")

    print("podaj temperature w Fahrenheitach:")

    temp_f = int(input())
    temp_c = (temp_f - 32) * 5 / 9
    temp_k = temp_c - 273

    print(temp_f, " F to ", temp_c, " C", " i ", temp_k, " K")

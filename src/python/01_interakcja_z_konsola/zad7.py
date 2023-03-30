"""
Tytuł: Konwersja jednostek.
Treść zadania: Napisz program, który będzie konwertować jednostki zgodnie z następującymi instrukcjami:
a) Pobierz wielkość w kilogramach i wypisz, ile gramów odpowiada.
b) Pobierz wielkość w calach i wypisz, ile centymetrów odpowiada.
c) Pobierz liczbę sekund i przelicz na godziny.
d) Pobierz liczbę w euro i wypisz, ile złotówek odpowiada.
e) Pobierz miarę kąta w stopniach i wypisz, ile radianów odpowiada.
f) Pobierz temperaturę w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.
Dane wejściowe: Liczba naturalna we wszystkich podpunktach.
Dane wyjściowe:
* Liczba naturalna dla podpunktów 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostałych podpunktów.
Przykład:
a) Dla pobranej liczby: 2, powinna zostać wypisana liczba: 2000.
b) Dla pobranej liczby: 12, powinna zostać wypisana liczba: 4.724.
c) Dla pobranej liczby: 3600, powinna zostać wypisana liczba: 1.
d) Dla pobranej liczby: 4, powinna zostać wypisana liczba: 17.6.
e) Dla pobranej liczby: 120, powinna zostać wypisana liczba:  2.094.
f) Dla pobranej liczby: 100, powinny zostać wypisane liczby: 37.777 i -235.222.

"""

if __name__ == "__main__":

    print("podaj podstawe i wysokosc trojkata:")
    a = int(input())
    h = int(input())
    print(
        "pole trojkata o podstawie ", a, " i wysokosci ", h, " jest rowne ", a * h / 2
    )

    print("podaj dlogosci bokow prostokata:")
    a = int(input())
    b = int(input())
    print("pole prostokata o bokach ", a, " i ", b, " jest rowne ", a * b)

    print("podaj dlugosc przekatnych rombu:")
    a = int(input())
    b = int(input())
    print("pole rombu o przekatnych ", a, " i ", b, " jest rowne ", a * b / 2)

    print("podaj promien kuli:")
    r = int(input())
    print("objetosc kuli o promieniu ", r, " jest rowna ", 4 / 3 * 3.14 * r ** 3)

    print("podaj promien podstawy i wysokosc stozka:")
    r = int(input())
    h = int(input())
    print(
        "objetosc stozka o podstawie ",
        r,
        " i wysokosci ",
        h,
        " jest rowna ",
        1 / 3 * 3.14 * r ** 2 * h,
    )

    print("podaj dlugosc, szerokosc i wysokosc graniastoslupa:")
    a = int(input())
    b = int(input())
    h = int(input())
    print(
        "objetosc graniastoslupa o dlugosci ",
        a,
        " i szerokosci ",
        b,
        " i wysokosci ",
        h,
        " jest rowna ",
        a * b * h,
    )

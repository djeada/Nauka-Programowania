"""
Tytul: Konwersja jednostek.
Tresc zadania: Napisz program, ktory bedzie konwertowac jednostki zgodnie z nastepujacymi instrukcjami:
a) Pobierz wielkosc w kilogramach i wypisz, ile gramow odpowiada.
b) Pobierz wielkosc w calach i wypisz, ile centymetrow odpowiada.
c) Pobierz liczbe sekund i przelicz na godziny.
d) Pobierz liczbe w euro i wypisz, ile zlotowek odpowiada.
e) Pobierz miare kata w stopniach i wypisz, ile radianow odpowiada.
f) Pobierz temperature w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.
Dane wejsciowe: Liczba naturalna we wszystkich podpunktach.
Dane wyjsciowe:
* Liczba naturalna dla podpunktow 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostalych podpunktow.
Przyklad:
a) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 2000.
b) Dla pobranej liczby: 12, powinna zostac wypisana liczba: 4.724.
c) Dla pobranej liczby: 3600, powinna zostac wypisana liczba: 1.
d) Dla pobranej liczby: 4, powinna zostac wypisana liczba: 17.6.
e) Dla pobranej liczby: 120, powinna zostac wypisana liczba:  2.094.
f) Dla pobranej liczby: 100, powinny zostac wypisane liczby: 37.777 i -235.222.

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

"""
Zamien jednostki:

a) Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.
b) Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.
c) Pobierz liczbe sekund i przelicz na godziny.
d) Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 
e) Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.
f) Pobierz temperature w stopniach Fahrenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 
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

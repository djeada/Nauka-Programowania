"""
Zamień jednostki:

a) Pobierz wielkość w kilogramach i wypisz ilu gramom odpowiada.
b) Pobierz wielkość w calach i wypisz ilu centymetrom odpowiada.
c) Pobierz liczbę sekund i przelicz na godziny.
d) Pobierz liczbę w euro i wypisz ilu złotówkom odpowiada. 
e) Pobierz miarę kąta w stopniach i wypisz ilu radianom odpowiada.
f) Pobierz temperaturę w stopniach Fahrenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 
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

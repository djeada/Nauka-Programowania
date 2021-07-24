if __name__ == "__main__":

    """
    Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.
    """

    print("podaj wielkosc w kilogramach:")

    kilogramy = int(input())
    gramy = kilogramy * 1000

    print(kilogramy, " kg to ", gramy, " g")

    """
	Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.
	"""

    print("podaj wielkosc w calach:")

    cal = int(input())
    cm = cal / 2.54

    print(cal, " cali to", cm, " cm")

    """
	Pobierz ilosc sekund i przelicz na godziny.
	"""

    print("podaj ilosc sekund:")

    sekundy = int(input())
    godziny = sekundy / 3600

    print(sekundy, " sekund to ", godziny, " godzin")

    """
	Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 
	"""

    print("podaj liczbe w euro:")

    euro = input()
    zloty = euro * 4.40

    print(euro, " euro to ", zloty, " zlotych")

    """
	Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada. 
	"""

    print("podaj miare kata w stopniach:")

    kat_stopnie = int(input())
    kat_rad = kat_stopnie * 0.0174532

    print(kat_stopnie, " stopni to ", kat_rad, " radianow")

    """
	Pobierz temperature w stopniach Farenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 
	"""

    print("podaj temperature w Farenheitach:")

    temp_f = int(input())
    temp_c = (temp_f - 32) * 5 / 9
    temp_k = temp_c - 273

    print(temp_f, " F to ", temp_c, " C", " i ", temp_k, " K")

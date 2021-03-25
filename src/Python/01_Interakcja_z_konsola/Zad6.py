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

    katStopnie = int(input())
    katRad = katStopnie * 0.0174532

    print(katStopnie, " stopni to ", katRad, " radianow")

    """
	Pobierz temperature w stopniach Farenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 
	"""

    print("podaj temperature w Farenheitach:")

    tempF = int(input())
    tempC = (tempF - 32) * 5 / 9
    tempK = tempC - 273

    print(tempF, " F to ", tempC, " C", " i ", tempK, " K")

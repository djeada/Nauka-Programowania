if __name__ == '__main__':

	'''
	Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.
	'''

	print("podaj kg")

	kilogramy = int(input())
	gramy = kilogramy * 1000

	print(kilogramy, "kg to " , gramy, "g") 

	'''
	Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.
	'''

	print("podaj cale")

	cal = int(input())
	cm = cal / 2.54

	print(cal, "cali to" , cm, "cm") 
	 
	'''
	Pobierz ilosc sekund i przelicz na godziny.
	'''

	print("podaj ilosc sekund")

	s = int(input())
	h = s / 3600

	print(s, "sekund to " , h, "godzin")

	'''
	Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 
	'''

	print("podaj liczbe w euro")

	euro = input()
	zloty = euro * 4,40

	print(euro, "euro to " , zloty, "zlotych")

	'''
	Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada. 
	'''
	
	print("podaj miare kata w stopniach") 

	kat = int(input())
	rad = kat * 0.0174532

	print(kat, " stopni to " , rad, "radianow")

	'''
	Pobierz temperature w stopniach Farenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 
	'''

	print("podaj temperature w Farenheitach") 

	F = int(input())
	C = (F -32) * 5 / 9
	K = C - 273

	print(F, "Farenheitow to " , C, "C" , " i " ,K ,"K")



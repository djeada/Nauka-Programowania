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

print(s, "sekund to" , h, "godzin")

'''
Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 
'''

print("podaj ilosc euro")

euro = input()
zloty = euro * 4,40

print(euro, "euro to" , zloty, "zlotych")

'''
Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada. 
'''
print("podaj ilosc katow") 

kat = int(input())
rad = kat * 0.0174532

print(kat, "kat to" , rad, "radow")

'''
Pobierz temperature w stopniach Farenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 
'''

print("podaj ilosc Farenheit") 

F = int(input())
C = (F -32) * 5 / 9
K = C - 273

print(F, "Farenheitow to" , C, "C" , "i" ,K ,"K")



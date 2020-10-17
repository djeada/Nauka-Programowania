'''
Otrzymujesz cene oraz wymiary pojedynczej plytki. Oblicz ile bedzie wynosila cena
za podloge o podanych wymiarach. Podloga jest prostokatem, a plytka kwadratem
'''

print("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi")

cena = int(input())
a = int(input())
b = int(input())
c = int(input()) 

_b = b + a - b % a 
_c = c + a - c % a

print( "jesli cena to" , cena , "a bok plytki to" , a , "a wymiary pokoju to" , b , c , "to calkowita cena wynosi" , cena * (_b * _c) / (a *a))

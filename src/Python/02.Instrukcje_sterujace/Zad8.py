'''

Pobierz od uzytkownika trzy dlugosci bokow i sprawdz, czy mozna z nich zbudowac trojkat.

'''

a = int(input())
b = int(input())
c = int(input()) 

if a + b > c and b + c > a and a + c > b:
	print("z podanych bokow mozna zbudowac trojkat") 
else:
	print("z podanych bokow nie mozna zbudowac trojkat") 

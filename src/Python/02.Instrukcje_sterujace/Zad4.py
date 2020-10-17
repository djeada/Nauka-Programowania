'''
Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.
'''
print("podaj dwie liczby")

a = int(input())
b = int(input())  

if a<b: 
	print(b,a)
	print(" druga liczba jest wieksza od pierwszej")
else:
	print(a,b)
	print("pierwsza liczba jest wieksza od drugiej") 

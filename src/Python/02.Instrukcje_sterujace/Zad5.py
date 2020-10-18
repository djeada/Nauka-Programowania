'''
Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.
'''
print("podaj trzy liczby") 

a = int(input())
b = int(input())
c = int(input())

if a>b>c:
	print(a,b,c)
	print("1 liczba jest najwieksza, 2 mniejsza i 3 najmniejsza")

else:
	print(c,b,a)
	print("liczby sa odwrotnie rosnace")
	
	 


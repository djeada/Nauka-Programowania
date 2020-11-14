'''

Dla pobranych czterech liczb, znajdz najwieksza liczbe. 

'''

a = int(input())
b = int(input())
c = int(input())
d = int(input()) 


maksAB = a if a > b else b
  
maksCD = c if c > d else d 

maks = maksAB if maksAB > maksCD else maksCD

print(maks)

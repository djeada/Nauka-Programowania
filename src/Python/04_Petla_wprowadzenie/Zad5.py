"""
Znajdz liczby podzielne przez x na przedziale [a, b].	
"""

print("Podaj liczby a, b oraz x: ")
a = int(input())
b = int(input())
x = int(input())

print("Liczby podzielne przez x na przedziale [a, b]: ")

# Wersja 1
for i in range(a, b + 1):
    if i % x == 0:
        print(i)

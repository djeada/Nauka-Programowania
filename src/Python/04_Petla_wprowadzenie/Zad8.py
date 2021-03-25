"""
Na farmie mamy a glow i b nog, znajdz liczbe kur oraz owieczek.
"""

# Wersja 1
a = 40
b = 100

for i in range(a):
    owieczki = a - i
    if 2 * i + 4 * owieczki == b:
        print("Na farmie mamy: ", i, "kur oraz ", owieczki, " owieczek.")
        break

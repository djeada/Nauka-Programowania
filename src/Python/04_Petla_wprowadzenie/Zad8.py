"""
Na farmie mamy a glow i b nog, znajdz liczbe kur oraz liczbe owieczek.
"""

if __name__ == "__main__":

    glowy = int(input("Podaj liczbe glow: "))
    nogi = int(input("Podaj liczbe nog: "))

    kury = 0
    owieczki = 0

    for i in range(glowy):
        owieczki = glowy - i
        if 2 * i + 4 * owieczki == nogi:
            print("Liczba kur: ", i)
            print("Liczba owieczek: ", owieczki)
            break

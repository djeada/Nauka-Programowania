"""
Na farmie mamy a głów i b nóg, znajdź liczbę kur oraz liczbę owieczek.
"""

if __name__ == "__main__":

    glowy = int(input("Podaj liczbę głów: "))
    nogi = int(input("Podaj liczbę nóg: "))

    kury = 0
    owieczki = 0

    for i in range(glowy):
        owieczki = glowy - i
        if 2 * i + 4 * owieczki == nogi:
            print("Liczba kur: ", i)
            print("Liczba owieczek: ", owieczki)
            break

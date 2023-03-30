"""
Tytul: Zaprojektuj klase Macierz.
Tresc: Napisz klase Macierz, ktora bedzie reprezentowala macierz. Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje jako argument liste list liczb calkowitych. Pobrana lista reprezentuje macierz. Domyslna wartosc argumentu to pusta lista.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie) oraz odwracanie macierzy. Jesli jest to mozliwe, nalezy przeciazyc operatory: +, -, *.
3. Funkcje, ktora wypisuje informacje o macierzy na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Macierz. Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.
Napisz program, ktory przetestuje twoja klase. Stworz macierze: A ([[1, 3], [4, 2]]) oraz B ([[5, 0], [1, 3]]). Wypisz na standardowe wyjscie informacje o utworzonych macierzach oraz ich sume, roznice pierwszej i drugiej oraz iloczyn macierzy.

"""

class Macierz:
    def __init__(self, macierz=[[]]):
        self.macierz = macierz

    def __add__(self, other):
        if len(self.macierz) == len(other.macierz):
            if len(self.macierz[0]) == len(other.macierz[0]):
                suma = []
                for i in range(len(self.macierz)):
                    suma.append([])
                    for j in range(len(self.macierz[0])):
                        suma[i].append(self.macierz[i][j] + other.macierz[i][j])
                return Macierz(suma)
            else:
                raise ValueError("Macierze maja rozne wymiary")
        else:
            raise ValueError("Macierze maja rozne wymiary")

    def __sub__(self, other):
        if len(self.macierz) == len(other.macierz):
            if len(self.macierz[0]) == len(other.macierz[0]):
                roznica = []
                for i in range(len(self.macierz)):
                    roznica.append([])
                    for j in range(len(self.macierz[0])):
                        roznica[i].append(self.macierz[i][j] - other.macierz[i][j])
                return Macierz(roznica)
            else:
                raise ValueError("Macierze maja rozne wymiary")
        else:
            raise ValueError("Macierze maja rozne wymiary")

    def __mul__(self, other):
        if len(self.macierz[0]) == len(other.macierz):
            iloczyn = []
            for i in range(len(self.macierz)):
                iloczyn.append([])
                for j in range(len(other.macierz[0])):
                    iloczyn[i].append(0)
                    for k in range(len(other.macierz)):
                        iloczyn[i][j] += self.macierz[i][k] * other.macierz[k][j]
            return Macierz(iloczyn)

        else:
            raise ValueError("Macierze maja rozne wymiary")

    def __str__(self):
        return f"{self.macierz}"

    def __eq__(self, other):
        if len(self.macierz) == len(other.macierz):
            if len(self.macierz[0]) == len(other.macierz[0]):
                for i in range(len(self.macierz)):
                    for j in range(len(self.macierz[0])):
                        if self.macierz[i][j] != other.macierz[i][j]:
                            return False
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if len(self.macierz) == len(other.macierz):
            if len(self.macierz[0]) == len(other.macierz[0]):
                for i in range(len(self.macierz)):
                    for j in range(len(self.macierz[0])):
                        if self.macierz[i][j] != other.macierz[i][j]:
                            return True
                return False
            else:
                return True
        else:
            return True

    def transponuj(self):
        transponowana = []
        for i in range(len(self.macierz[0])):
            transponowana.append([])
            for j in range(len(self.macierz)):
                transponowana[i].append(self.macierz[j][i])
        return Macierz(transponowana)

if __name__ == "__main__":
    macierz_a = Macierz([[1, 3], [4, 2]])
    macierz_b = Macierz([[5, 0], [1, 3]])

    print(f"Macierz A: {macierz_a.macierz}")
    print(f"Macierz B: {macierz_b.macierz}")
    print(f"Suma: {macierz_a + macierz_b}")
    print(f"Roznica: {macierz_a - macierz_b}")
    print(f"Iloczyn: {macierz_a * macierz_b}")
    print(f"Transponowana macierz A: {macierz_a.transponuj()}")
    print(f"Macierz A == Macierz B: {macierz_a == macierz_b}")
    print(f"Macierz A != Macierz B: {macierz_a != macierz_b}")
    print(f"Macierz A == Macierz A: {macierz_a == macierz_a}")
    print(f"Macierz A != Macierz A: {macierz_a != macierz_a}")


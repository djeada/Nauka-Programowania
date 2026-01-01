"""
ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

* A = [[1, 3], [4, 2]]
* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

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

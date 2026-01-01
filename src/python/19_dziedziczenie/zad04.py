"""
ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `konstruktory`, `super`

### Treść

Zaprojektuj hierarchię klas:

1. **Człowiek** — pola:

   * imię
   * nazwisko
   * miejsce urodzenia
   * zawód

2. **Student** (dziedziczy po `Człowiek`) — dodatkowo:

   * numer albumu
   * kierunek studiów

3. **StudentFizyki** (dziedziczy po `Student`) — dodatkowo:

   * średnia z laboratoriów
   * średnia z wykładów

Program:

* wczytuje dane dla trzech obiektów (Człowiek, Student, StudentFizyki),
* tworzy obiekty,
* wypisuje je w formacie jak w przykładzie.

**Uwaga do wejścia:** wszystko w osobnych liniach, w podanej kolejności.

### Wejście

**Dane dla Człowiek:**

1. imię
2. nazwisko
3. miejsce urodzenia
4. zawód

**Dane dla Student:**
5. imię
6. nazwisko
7. miejsce urodzenia
8. zawód
9. numer albumu (int)
10. kierunek studiów

**Dane dla StudentFizyki:**
11. imię
12. nazwisko
13. miejsce urodzenia
14. zawód
15. numer albumu (int)
16. kierunek studiów
17. średnia z laboratoriów (float)
18. średnia z wykładów (float)

### Wyjście

Trzy bloki jak w przykładzie, oddzielone pustą linią.

### Przykład

**Wejście:**

```
Jan
Kowalski
Kraków
Inżynier
Anna
Nowak
Warszawa
Student
12345
Informatyka
Piotr
Wiśniewski
Gdańsk
Student
54321
Fizyka
4.5
4.0
```

**Wyjście:**

```
Człowiek:
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Kraków
Zawód: Inżynier

Student:
Imię: Anna
Nazwisko: Nowak
Miejsce urodzenia: Warszawa
Zawód: Student
Numer albumu: 12345
Kierunek studiów: Informatyka

Student Fizyki:
Imię: Piotr
Nazwisko: Wiśniewski
Miejsce urodzenia: Gdańsk
Zawód: Student
Numer albumu: 54321
Kierunek studiów: Fizyka
Średnia z laboratoriów: 4.5
Średnia z wykładów: 4.0
```

"""


class Czlowiek:
    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_urodzenia = miejsce_urodzenia
        self.zawod = zawod

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.miejsce_urodzenia} {self.zawod}"

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.miejsce_urodzenia} {self.zawod}"

    def __eq__(self, other):
        return (
            self.imie == other.imie
            and self.nazwisko == other.nazwisko
            and self.miejsce_urodzenia == other.miejsce_urodzenia
            and self.zawod == other.zawod
        )

    def __ne__(self, other):
        return not self.__eq__(other)


class Student(Czlowiek):
    def __init__(
        self, imie, nazwisko, miejsce_urodzenia, numer_albumu, kierunek_studiow
    ):
        super().__init__(imie, nazwisko, miejsce_urodzenia, "student")
        self.numer_albumu = numer_albumu
        self.kierunek_studiow = kierunek_studiow

    def __str__(self):
        return f"{super().__str__()} {self.numer_albumu} {self.kierunek_studiow}"

    def __repr__(self):
        return f"{super().__repr__()} {self.numer_albumu} {self.kierunek_studiow}"

    def __eq__(self, other):
        return (
            super().__eq__(other)
            and self.numer_albumu == other.numer_albumu
            and self.kierunek_studiow == other.kierunek_studiow
        )

    def __ne__(self, other):
        return not self.__eq__(other)


class StudentFizyki(Student):
    def __init__(
        self,
        imie,
        nazwisko,
        miejsce_urodzenia,
        numer_albumu,
        srednia_z_lab,
        srednia_z_wykl,
    ):
        super().__init__(imie, nazwisko, miejsce_urodzenia, numer_albumu, "Fizyka")
        self.srednia_z_lab = srednia_z_lab
        self.srednia_z_wykl = srednia_z_wykl

    def __str__(self):
        return f"{super().__str__()} {self.srednia_z_lab} {self.srednia_z_wykl}"

    def __repr__(self):
        return f"{super().__repr__()} {self.srednia_z_lab} {self.srednia_z_wykl}"

    def __eq__(self, other):
        return (
            super().__eq__(other)
            and self.srednia_z_lab == other.srednia_z_lab
            and self.srednia_z_wykl == other.srednia_z_wykl
        )

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == "__main__":

    czlowiek = Czlowiek("Jan", "Kowalski", "Warszawa", "programista")
    student = Student("Jan", "Kowalski", "Warszawa", "123456789", "Informatyka")
    student_fizyki = StudentFizyki("Jan", "Kowalski", "Warszawa", "123456789", 4.5, 5.0)

    print(czlowiek)
    print(student)
    print(student_fizyki)

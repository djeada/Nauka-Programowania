"""
Tytul: Dziedziczenie wielopoziomowe
Tresc: Napisz klase Czlowiek oraz klasy pochodne Student i StudentFizyki. Czlowiek powinien zawierac informacje o imieniu, nazwisku, miejscu urodzenia i zawodzie. Student powinien dodawac pola numeru albumu oraz kierunku studiow. StudentFizyki powinien dodawac pola sredniej z laboratoriow oraz sredniej z wykladow. Napisz program testujacy te klasy.

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


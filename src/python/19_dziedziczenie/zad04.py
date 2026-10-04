r"""
ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `konstruktory`, `super`

### Treść

Zaprojektuj hierarchię klas:

1. `Czlowiek` — atrybuty: imię, nazwisko, miejsce urodzenia, zawód.
2. `Student` (dziedziczy po `Czlowiek`) — dodatkowo: numer albumu, kierunek studiów.
3. `StudentFizyki` (dziedziczy po `Student`) — dodatkowo: średnia z laboratoriów, średnia z wykładów.

Każda klasa ma:

* konstruktor, który atrybuty odziedziczone przekazuje do konstruktora klasy bazowej przez `super().__init__(…)`, a sam zapisuje tylko nowe atrybuty,
* metodę `opis()`, która zwraca **listę linii** z danymi obiektu. Klasa potomna wywołuje `super().opis()` i dopisuje do wyniku linie ze swoimi nowymi atrybutami,
* nagłówek: `Człowiek`, `Student` albo `Student Fizyki`.

Metoda `wypisz()` (zdefiniowana tylko w klasie `Czlowiek`) wypisuje nagłówek z dwukropkiem, a pod nim kolejne linie z `opis()`.

Program wczytuje dane kilku osób, tworzy odpowiednie obiekty i wypisuje je w kolejności z wejścia.

### Wejście

* 1. linia: liczba osób $n$
* następnie dane kolejnych osób; każda wartość w osobnej linii:
  1. rodzaj: `czlowiek`, `student` albo `student_fizyki`
  2. imię
  3. nazwisko
  4. miejsce urodzenia
  5. zawód
  6. numer albumu (liczba całkowita) — tylko dla `student` i `student_fizyki`
  7. kierunek studiów — tylko dla `student` i `student_fizyki`
  8. średnia z laboratoriów (liczba rzeczywista) — tylko dla `student_fizyki`
  9. średnia z wykładów (liczba rzeczywista) — tylko dla `student_fizyki`

Wartości tekstowe mogą zawierać spacje (np. `Zielona Góra`).

### Wyjście

Dla każdej osoby blok linii, bloki oddzielone pustą linią. Blok ma postać (linie z nawiasu kwadratowego występują tylko w odpowiednich klasach):

```
<Nagłówek>:
Imię: <imię>
Nazwisko: <nazwisko>
Miejsce urodzenia: <miejsce>
Zawód: <zawód>
[Numer albumu: <numer>]
[Kierunek studiów: <kierunek>]
[Średnia z laboratoriów: <średnia>]
[Średnia z wykładów: <średnia>]
```

Średnie wypisz z dokładnością do 2 miejsc po przecinku.

### Ograniczenia

* $1 \le n \le 10$

### Przykład

**Wejście:**

```
3
czlowiek
Jan
Kowalski
Kraków
Inżynier
student
Anna
Nowak
Warszawa
Student
12345
Informatyka
student_fizyki
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
Średnia z laboratoriów: 4.50
Średnia z wykładów: 4.00
```

### Uwagi

* Nagłówek wygodnie zapisać jako atrybut klasy, np. `naglowek = "Student"` — klasa potomna nadpisuje go własną wartością, a `wypisz()` odczytuje `self.naglowek`.

### Kod startowy

```python
class Czlowiek:
    naglowek = "Człowiek"

    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod):
        pass

    def opis(self):
        pass

    def wypisz(self):
        print(f"{self.naglowek}:")
        for linia in self.opis():
            print(linia)


class Student(Czlowiek):
    naglowek = "Student"

    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek):
        pass

    def opis(self):
        pass


class StudentFizyki(Student):
    naglowek = "Student Fizyki"

    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek,
                 srednia_lab, srednia_wyklad):
        pass

    def opis(self):
        pass


n = int(input())
osoby = []
for _ in range(n):
    rodzaj = input()
    imie = input()
    nazwisko = input()
    miejsce = input()
    zawod = input()
    if rodzaj == "czlowiek":
        osoby.append(Czlowiek(imie, nazwisko, miejsce, zawod))
        continue
    numer = int(input())
    kierunek = input()
    if rodzaj == "student":
        osoby.append(Student(imie, nazwisko, miejsce, zawod, numer, kierunek))
    else:
        lab = float(input())
        wyklad = float(input())
        osoby.append(StudentFizyki(imie, nazwisko, miejsce, zawod, numer, kierunek, lab, wyklad))

for i, osoba in enumerate(osoby):
    if i > 0:
        print()
    osoba.wypisz()
```

"""


class Czlowiek:
    naglowek = "Człowiek"

    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_urodzenia = miejsce_urodzenia
        self.zawod = zawod

    def opis(self):
        return [
            f"Imię: {self.imie}",
            f"Nazwisko: {self.nazwisko}",
            f"Miejsce urodzenia: {self.miejsce_urodzenia}",
            f"Zawód: {self.zawod}",
        ]

    def wypisz(self):
        print(f"{self.naglowek}:")
        for linia in self.opis():
            print(linia)


class Student(Czlowiek):
    naglowek = "Student"

    def __init__(
        self, imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek
    ):
        super().__init__(imie, nazwisko, miejsce_urodzenia, zawod)
        self.numer_albumu = numer_albumu
        self.kierunek = kierunek

    def opis(self):
        return super().opis() + [
            f"Numer albumu: {self.numer_albumu}",
            f"Kierunek studiów: {self.kierunek}",
        ]


class StudentFizyki(Student):
    naglowek = "Student Fizyki"

    def __init__(
        self,
        imie,
        nazwisko,
        miejsce_urodzenia,
        zawod,
        numer_albumu,
        kierunek,
        srednia_lab,
        srednia_wyklad,
    ):
        super().__init__(
            imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek
        )
        self.srednia_lab = srednia_lab
        self.srednia_wyklad = srednia_wyklad

    def opis(self):
        return super().opis() + [
            f"Średnia z laboratoriów: {self.srednia_lab:.2f}",
            f"Średnia z wykładów: {self.srednia_wyklad:.2f}",
        ]


def wczytaj_osobe():
    rodzaj = input()
    imie = input()
    nazwisko = input()
    miejsce = input()
    zawod = input()
    if rodzaj == "czlowiek":
        return Czlowiek(imie, nazwisko, miejsce, zawod)
    numer = int(input())
    kierunek = input()
    if rodzaj == "student":
        return Student(imie, nazwisko, miejsce, zawod, numer, kierunek)
    lab = float(input())
    wyklad = float(input())
    return StudentFizyki(imie, nazwisko, miejsce, zawod, numer, kierunek, lab, wyklad)


if __name__ == "__main__":
    n = int(input())
    osoby = [wczytaj_osobe() for _ in range(n)]
    for i, osoba in enumerate(osoby):
        if i > 0:
            print()
        osoba.wypisz()

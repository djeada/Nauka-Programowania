# Rozdział 19: Dziedziczenie

Zadania w tym rozdziale uczą **dziedziczenia**: klasa potomna przejmuje atrybuty i metody klasy bazowej, może je **nadpisać** (override) albo rozszerzyć, wywołując wersję z klasy bazowej przez `super()`. Dzięki **polimorfizmowi** ten sam kod (np. pętla po liście obiektów) wywołuje metodę odpowiednią dla konkretnej klasy obiektu. Dziedziczenie przydaje się też przy wyjątkach: własne wyjątki to klasy dziedziczące po `Exception`, które można układać w hierarchie.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* W każdym zadaniu dostajesz **kod startowy** ze szkieletami klas i gotowym wczytywaniem danych. Twoim zadaniem jest uzupełnienie klas — wynik programu zależy od tego, jak działają Twoje klasy.
* Nazwy klas i metod podane w treści są obowiązkowe (kod startowy z nich korzysta). Nazwy w kodzie piszemy bez polskich znaków, np. `Kolo`, `Czlowiek`.
* „Z dokładnością do 2 miejsc po przecinku” oznacza dokładnie dwie cyfry po kropce, np. `f"{x:.2f}"` (`3.00`, `4.50`).
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

**Poziom:** ★☆☆
**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. `Bazowa` — konstruktor `__init__(self, nazwa)` zapamiętuje nazwę obiektu, a metoda `przedstaw_sie()` wypisuje linię
   `Jestem klasą bazową. Nazywam się <nazwa>.`
2. `Potomna` — dziedziczy po `Bazowa` i **nadpisuje** metodę `przedstaw_sie()`. Nowa wersja:
   * najpierw **wywołuje** wersję metody z klasy bazowej (przez `super()`),
   * potem wypisuje linię `A ja jestem klasą potomną.`

Klasa `Potomna` nie potrzebuje własnego konstruktora — dziedziczy go po `Bazowa`.

Program wczytuje opis kilku obiektów, tworzy je, a następnie dla każdego z nich (w kolejności z wejścia) wywołuje metodę `przedstaw_sie()`.

### Wejście

* 1. linia: liczba obiektów $n$
* kolejne $n$ linii: rodzaj obiektu (`bazowa` albo `potomna`) i jego nazwa (jedno słowo), oddzielone spacją

### Wyjście

Komunikaty wypisane przez kolejne wywołania `przedstaw_sie()`: jedna linia dla obiektu klasy `Bazowa` i dwie linie dla obiektu klasy `Potomna`.

### Ograniczenia

* $1 \le n \le 20$

### Przykład

**Wejście:**

```
3
bazowa Ala
potomna Ola
bazowa Jan
```

**Wyjście:**

```
Jestem klasą bazową. Nazywam się Ala.
Jestem klasą bazową. Nazywam się Ola.
A ja jestem klasą potomną.
Jestem klasą bazową. Nazywam się Jan.
```

### Kod startowy

```python
class Bazowa:
    def __init__(self, nazwa):
        # Uzupełnij: zapamiętaj nazwę.
        pass

    def przedstaw_sie(self):
        # Uzupełnij.
        pass


class Potomna(Bazowa):
    def przedstaw_sie(self):
        # Uzupełnij: wywołaj wersję z klasy bazowej, a potem dopisz własny komunikat.
        pass


n = int(input())
obiekty = []
for _ in range(n):
    rodzaj, nazwa = input().split()
    if rodzaj == "bazowa":
        obiekty.append(Bazowa(nazwa))
    else:
        obiekty.append(Potomna(nazwa))

for obiekt in obiekty:
    obiekt.przedstaw_sie()
```

---

## ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

* `Ksztalt` — klasa bazowa dla wszystkich kształtów. Ma metodę `wypisz()`, która wypisuje informacje o kształcie w trzech liniach:

  ```
  Kształt: <nazwa>
  <parametr>
  Pole powierzchni: <pole>
  ```

  Metoda `wypisz()` jest napisana **tylko raz**, w klasie `Ksztalt` — korzysta z metod `nazwa()`, `parametr()` i `pole()`, które nadpisują klasy potomne.
* `Kolo(r)` — dziedziczy po `Ksztalt`. Metoda `nazwa()` zwraca `Koło`, `parametr()` zwraca napis `Promień: <r>`, a `pole()` zwraca $\pi r^2$.
* `Kwadrat(a)` — dziedziczy po `Ksztalt`. Metoda `nazwa()` zwraca `Kwadrat`, `parametr()` zwraca napis `Długość boku: <a>`, a `pole()` zwraca $a^2$.

Program wczytuje listę kształtów, wypisuje informacje o każdym z nich (bloki oddzielone pustą linią), a na końcu — po pustej linii — sumę pól wszystkich kształtów.

### Wejście

* 1. linia: liczba kształtów $n$
* kolejne $n$ linii: `kolo r` albo `kwadrat a`, gdzie $r$ i $a$ są dodatnimi liczbami rzeczywistymi

### Wyjście

* Dla każdego kształtu blok trzech linii opisany w treści; po każdym bloku pusta linia.
* Ostatnia linia: `Suma pól: <suma>`.

Wszystkie liczby (promień, bok, pola i suma) wypisz z dokładnością do 2 miejsc po przecinku.

### Ograniczenia

* $1 \le n \le 20$
* $0 < r, a \le 1000$

### Przykład

**Wejście:**

```
2
kolo 5
kwadrat 4
```

**Wyjście:**

```
Kształt: Koło
Promień: 5.00
Pole powierzchni: 78.54

Kształt: Kwadrat
Długość boku: 4.00
Pole powierzchni: 16.00

Suma pól: 94.54
```

### Uwagi

* Metody `nazwa()`, `parametr()` i `pole()` w klasie `Ksztalt` mogą zgłaszać wyjątek `NotImplementedError` — w ten sposób zaznaczamy, że każda klasa potomna musi je nadpisać.

### Kod startowy

```python
import math


class Ksztalt:
    def nazwa(self):
        raise NotImplementedError

    def parametr(self):
        raise NotImplementedError

    def pole(self):
        raise NotImplementedError

    def wypisz(self):
        # Uzupełnij: wypisz trzy linie, korzystając z nazwa(), parametr() i pole().
        pass


class Kolo(Ksztalt):
    def __init__(self, r):
        # Uzupełnij.
        pass

    # Uzupełnij: nadpisz metody nazwa(), parametr() i pole().


class Kwadrat(Ksztalt):
    def __init__(self, a):
        # Uzupełnij.
        pass

    # Uzupełnij: nadpisz metody nazwa(), parametr() i pole().


n = int(input())
ksztalty = []
for _ in range(n):
    rodzaj, wartosc = input().split()
    if rodzaj == "kolo":
        ksztalty.append(Kolo(float(wartosc)))
    else:
        ksztalty.append(Kwadrat(float(wartosc)))

suma = 0
for ksztalt in ksztalty:
    ksztalt.wypisz()
    print()
    suma += ksztalt.pole()
print(f"Suma pól: {suma:.2f}")
```

---

## ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

* `Zwierz` — konstruktor `__init__(self, imie)` zapamiętuje imię zwierzęcia. Metoda `odglos()` zwraca napis `...` (ogólny, nieokreślony dźwięk). Metoda `przedstaw_sie()` wypisuje linię:

  ```
  <NazwaKlasy> <imię> wydaje odgłos: <odgłos>
  ```

  gdzie `<NazwaKlasy>` to nazwa klasy obiektu (`Zwierz`, `Pies` albo `Kot`), a `<odgłos>` to wynik metody `odglos()`.
* `Pies` — dziedziczy po `Zwierz` i nadpisuje `odglos()`, która zwraca `Hau!`.
* `Kot` — dziedziczy po `Zwierz` i nadpisuje `odglos()`, która zwraca `Miau!`.

Klasy `Pies` i `Kot` **nie** definiują własnej metody `przedstaw_sie()` — korzystają z odziedziczonej. Dzięki polimorfizmowi wywołanie `self.odglos()` wewnątrz `przedstaw_sie()` uruchomi wersję metody właściwą dla klasy obiektu.

Program wczytuje listę zwierząt, umieszcza je w jednej liście i dla każdego (w kolejności z wejścia) wywołuje `przedstaw_sie()`.

### Wejście

* 1. linia: liczba zwierząt $n$
* kolejne $n$ linii: rodzaj zwierzęcia (`zwierz`, `pies` albo `kot`) i jego imię (jedno słowo), oddzielone spacją

### Wyjście

$n$ linii — po jednej dla każdego zwierzęcia, w formacie podanym w treści.

### Ograniczenia

* $1 \le n \le 20$

### Przykład

**Wejście:**

```
3
zwierz Gucio
pies Burek
kot Mruczek
```

**Wyjście:**

```
Zwierz Gucio wydaje odgłos: ...
Pies Burek wydaje odgłos: Hau!
Kot Mruczek wydaje odgłos: Miau!
```

### Uwagi

* Nazwę klasy obiektu można odczytać wyrażeniem `type(self).__name__`.

### Kod startowy

```python
class Zwierz:
    def __init__(self, imie):
        # Uzupełnij.
        pass

    def odglos(self):
        # Uzupełnij.
        pass

    def przedstaw_sie(self):
        # Uzupełnij: wypisz linię z nazwą klasy, imieniem i odgłosem.
        pass


class Pies(Zwierz):
    # Uzupełnij: nadpisz metodę odglos().
    pass


class Kot(Zwierz):
    # Uzupełnij: nadpisz metodę odglos().
    pass


n = int(input())
zwierzeta = []
for _ in range(n):
    rodzaj, imie = input().split()
    if rodzaj == "pies":
        zwierzeta.append(Pies(imie))
    elif rodzaj == "kot":
        zwierzeta.append(Kot(imie))
    else:
        zwierzeta.append(Zwierz(imie))

for zwierze in zwierzeta:
    zwierze.przedstaw_sie()
```

---

## ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki

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
        # Uzupełnij.
        pass

    def opis(self):
        # Uzupełnij: zwróć listę linii, np. ["Imię: Jan", "Nazwisko: Kowalski", ...].
        pass

    def wypisz(self):
        print(f"{self.naglowek}:")
        for linia in self.opis():
            print(linia)


class Student(Czlowiek):
    naglowek = "Student"

    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek):
        # Uzupełnij: wywołaj super().__init__(...) i zapamiętaj nowe atrybuty.
        pass

    def opis(self):
        # Uzupełnij: rozszerz wynik super().opis().
        pass


class StudentFizyki(Student):
    naglowek = "Student Fizyki"

    def __init__(self, imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek,
                 srednia_lab, srednia_wyklad):
        # Uzupełnij.
        pass

    def opis(self):
        # Uzupełnij.
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

---

## ZAD-05 — Dziedziczenie wielokrotne: Ptak

**Poziom:** ★★☆
**Tagi:** `multiple inheritance`, `dziedziczenie`, `metody`

### Treść

Zaprojektuj klasy:

* `Zwierz` — konstruktor `__init__(self, imie)` zapamiętuje imię. Metody:
  * `jedz()` → wypisuje `<imię> je.`
  * `spij()` → wypisuje `<imię> śpi.`
  * `wydaj_dzwiek()` → wypisuje `<imię> wydaje dźwięk.`
* `ObiektLatajacy` — konstruktor `__init__(self, imie)` zapamiętuje imię i ustawia stan „na ziemi” (np. atrybut `w_powietrzu = False`). Metody:
  * `lec()` → jeśli obiekt jest na ziemi, wypisuje `<imię> leci.` i przechodzi w stan „w powietrzu”; jeśli już jest w powietrzu, wypisuje `<imię> już leci.`
  * `wyladuj()` → jeśli obiekt jest w powietrzu, wypisuje `<imię> ląduje.` i przechodzi w stan „na ziemi”; jeśli już jest na ziemi, wypisuje `<imię> jest już na ziemi.`
* `Ptak` — dziedziczy **jednocześnie** po `Zwierz` i `ObiektLatajacy`. Jego konstruktor wywołuje konstruktory obu klas bazowych. `Ptak` nie definiuje żadnych innych metod — wszystkie dziedziczy.

Program wczytuje imię ptaka, tworzy obiekt `Ptak` (na początku jest na ziemi), a następnie wykonuje kolejne polecenia — każde polecenie to nazwa metody do wywołania.

### Wejście

* 1. linia: imię ptaka (może zawierać spacje)
* 2. linia: liczba poleceń $n$
* kolejne $n$ linii: polecenie — jedno z: `jedz`, `spij`, `wydaj_dzwiek`, `lec`, `wyladuj`

### Wyjście

$n$ linii — komunikaty wypisane przez kolejno wywołane metody.

### Ograniczenia

* $1 \le n \le 50$

### Przykład

**Wejście:**

```
Ptak
5
jedz
spij
wydaj_dzwiek
lec
wyladuj
```

**Wyjście:**

```
Ptak je.
Ptak śpi.
Ptak wydaje dźwięk.
Ptak leci.
Ptak ląduje.
```

### Uwagi

* Przy dziedziczeniu wielokrotnym najprościej wywołać konstruktory klas bazowych jawnie: `Zwierz.__init__(self, imie)` oraz `ObiektLatajacy.__init__(self, imie)`.

### Kod startowy

```python
class Zwierz:
    def __init__(self, imie):
        # Uzupełnij.
        pass

    def jedz(self):
        # Uzupełnij.
        pass

    def spij(self):
        # Uzupełnij.
        pass

    def wydaj_dzwiek(self):
        # Uzupełnij.
        pass


class ObiektLatajacy:
    def __init__(self, imie):
        # Uzupełnij: zapamiętaj imię i ustaw stan "na ziemi".
        pass

    def lec(self):
        # Uzupełnij.
        pass

    def wyladuj(self):
        # Uzupełnij.
        pass


class Ptak(Zwierz, ObiektLatajacy):
    def __init__(self, imie):
        # Uzupełnij: wywołaj konstruktory obu klas bazowych.
        pass


imie = input()
ptak = Ptak(imie)
n = int(input())
for _ in range(n):
    polecenie = input()
    if polecenie == "jedz":
        ptak.jedz()
    elif polecenie == "spij":
        ptak.spij()
    elif polecenie == "wydaj_dzwiek":
        ptak.wydaj_dzwiek()
    elif polecenie == "lec":
        ptak.lec()
    elif polecenie == "wyladuj":
        ptak.wyladuj()
```

---

## ZAD-06 — Wypłaty pracowników

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `fabryka`

### Treść

Zaprojektuj hierarchię klas pracowników:

* `Pracownik` — klasa bazowa. Konstruktor `__init__(self, imie)` zapamiętuje imię. Metoda `wyplata()` zgłasza wyjątek `NotImplementedError` (każda klasa potomna musi ją nadpisać). Metoda `opis()` zwraca napis
  `<imię> (<rodzaj>): <wypłata>`, gdzie `<rodzaj>` to atrybut klasy `rodzaj`, a wypłata jest wypisana z dokładnością do 2 miejsc po przecinku. Metoda `opis()` jest zdefiniowana **tylko** w klasie `Pracownik`.
* `Etatowy(imie, pensja)` — `rodzaj = "etatowy"`; wypłata to stała miesięczna pensja.
* `Godzinowy(imie, stawka, godziny)` — `rodzaj = "godzinowy"`; za pierwsze 160 godzin płacimy zwykłą stawkę, a za każdą godzinę powyżej 160 (nadgodziny) — stawkę 1,5 razy wyższą:
  $w = s \cdot g$ dla $g \le 160$ oraz $w = 160 s + 1.5 s (g - 160)$ dla $g > 160$.
* `Stazysta(imie)` — `rodzaj = "stażysta"`; wypłata to stałe stypendium 1500 zł, takie samo dla każdego stażysty.

Napisz też funkcję-fabrykę `utworz_pracownika(linia)`, która na podstawie jednej linii wejścia tworzy i zwraca obiekt odpowiedniej klasy.

Program wczytuje listę pracowników, wypisuje opis każdego z nich (w kolejności z wejścia) i sumę wszystkich wypłat.

### Wejście

* 1. linia: liczba pracowników $n$
* kolejne $n$ linii, każda w jednej z postaci:
  * `etatowy IMIĘ PENSJA`
  * `godzinowy IMIĘ STAWKA GODZINY`
  * `stazysta IMIĘ`

Imię to jedno słowo, pensja i stawka to liczby rzeczywiste, a liczba godzin to liczba całkowita $\ge 0$.

### Wyjście

* $n$ linii — wynik metody `opis()` dla kolejnych pracowników,
* ostatnia linia: `Suma wypłat: <suma>` (z dokładnością do 2 miejsc po przecinku).

### Ograniczenia

* $1 \le n \le 50$
* $0 \le pensja \le 100000$, $0 \le stawka \le 1000$, $0 \le godziny \le 400$

### Przykład

**Wejście:**

```
4
etatowy Anna 5200
godzinowy Bartek 40 170
stazysta Celina
godzinowy Darek 35.5 100
```

**Wyjście:**

```
Anna (etatowy): 5200.00
Bartek (godzinowy): 7000.00
Celina (stażysta): 1500.00
Darek (godzinowy): 3550.00
Suma wypłat: 17250.00
```

Bartek przepracował 10 nadgodzin: $160 \cdot 40 + 10 \cdot 1.5 \cdot 40 = 6400 + 600 = 7000$.

### Uwagi

* **Funkcja-fabryka** ukrywa przed resztą programu, jak powstają obiekty: program tylko woła `utworz_pracownika(linia)` i dostaje gotowy obiekt, a dalej korzysta wyłącznie z metod wspólnych dla wszystkich pracowników (`opis()`, `wyplata()`). Dodanie nowego rodzaju pracownika wymaga wtedy zmian tylko w nowej klasie i w fabryce.
* `raise NotImplementedError` w klasie bazowej to umowny sposób zapisania: „ta metoda musi zostać nadpisana w klasie potomnej”.

### Kod startowy

```python
class Pracownik:
    rodzaj = "pracownik"

    def __init__(self, imie):
        self.imie = imie

    def wyplata(self):
        raise NotImplementedError

    def opis(self):
        # Uzupełnij: zwróć napis "<imię> (<rodzaj>): <wypłata>".
        pass


class Etatowy(Pracownik):
    rodzaj = "etatowy"
    # Uzupełnij: konstruktor i metoda wyplata().


class Godzinowy(Pracownik):
    rodzaj = "godzinowy"
    # Uzupełnij: konstruktor i metoda wyplata().


class Stazysta(Pracownik):
    rodzaj = "stażysta"
    # Uzupełnij: metoda wyplata().


def utworz_pracownika(linia):
    # Uzupełnij: utwórz i zwróć obiekt klasy wskazanej w pierwszym słowie linii.
    pass


n = int(input())
pracownicy = []
for _ in range(n):
    pracownicy.append(utworz_pracownika(input()))

suma = 0
for pracownik in pracownicy:
    print(pracownik.opis())
    suma += pracownik.wyplata()
print(f"Suma wypłat: {suma:.2f}")
```

---

## ZAD-07 — Hierarchia własnych wyjątków

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `wyjątki`, `try-except`

### Treść

Zdefiniuj własne wyjątki tworzące hierarchię:

* `BladDanych` — dziedziczy po wbudowanej klasie `Exception`; ogólny błąd danych wejściowych,
* `BladFormatu` — dziedziczy po `BladDanych`; dane mają zły format,
* `BladZakresu` — dziedziczy po `BladDanych`; format jest dobry, ale wartość jest spoza dozwolonego zakresu.

Napisz funkcję `parsuj_godzine(tekst)`, która zamienia godzinę zapisaną w postaci `GG:MM` na liczbę minut od północy ($60 \cdot GG + MM$). Funkcja sprawdza dane w tej kolejności:

1. Jeśli `tekst` nie ma dokładnie 5 znaków, na pozycji 2 nie ma dwukropka albo znaki na pozycjach 0, 1, 3, 4 nie są cyframi — zgłasza `BladFormatu("oczekiwano formatu GG:MM")`.
2. Jeśli godzina jest większa od 23 — zgłasza `BladZakresu("godzina spoza zakresu 0-23")`.
3. Jeśli minuty są większe od 59 — zgłasza `BladZakresu("minuty spoza zakresu 0-59")`.

Program dla każdej wczytanej linii wywołuje `parsuj_godzine` i wypisuje wynik albo informację o błędzie. Oba rodzaje błędów przechwytuje **jedną** klauzulą `except BladDanych as e` — łapie ona wyjątki klasy `BladDanych` i wszystkich klas, które po niej dziedziczą.

### Wejście

* 1. linia: liczba napisów $n$
* kolejne $n$ linii: napis do sprawdzenia (bez spacji)

### Wyjście

Dla każdego napisu jedna linia:

* `<napis> -> <minuty>` — jeśli napis jest poprawny,
* `<napis> -> <NazwaKlasyWyjątku>: <komunikat>` — jeśli funkcja zgłosiła wyjątek, np. `24:00 -> BladZakresu: godzina spoza zakresu 0-23`.

### Ograniczenia

* $1 \le n \le 50$
* Każdy napis ma od 1 do 20 znaków.

### Przykład

**Wejście:**

```
5
07:30
23:59
24:00
7:30
12:60
```

**Wyjście:**

```
07:30 -> 450
23:59 -> 1439
24:00 -> BladZakresu: godzina spoza zakresu 0-23
7:30 -> BladFormatu: oczekiwano formatu GG:MM
12:60 -> BladZakresu: minuty spoza zakresu 0-59
```

### Uwagi

* Własny wyjątek to zwykła klasa dziedzicząca po `Exception` — zwykle nie potrzebuje żadnego kodu: `class BladDanych(Exception): pass`. Komunikat przekazuje się przy zgłaszaniu: `raise BladFormatu("…")`.
* Nazwę klasy przechwyconego wyjątku odczytasz wyrażeniem `type(e).__name__`.
* Gdy błędy różnych klas trzeba obsłużyć **różnie**, piszemy kilka klauzul `except`. Python sprawdza je **po kolei** i wybiera pierwszą pasującą, dlatego klasy potomne muszą stać **przed** klasą bazową:

  ```python
  try:
      minuty = parsuj_godzine(tekst)
  except BladFormatu:
      ...   # tylko błędy formatu
  except BladDanych:
      ...   # wszystkie pozostałe błędy danych (np. BladZakresu)
  ```

  Gdyby `except BladDanych` stało pierwsze, przechwyciłoby także `BladFormatu`, a druga klauzula nigdy by się nie wykonała.
* `"07".isdigit()` sprawdza, czy napis składa się z samych cyfr.

### Kod startowy

```python
# Uzupełnij: zdefiniuj wyjątki BladDanych (dziedziczy po Exception)
# oraz BladFormatu i BladZakresu (dziedziczą po BladDanych).


def parsuj_godzine(tekst):
    # Uzupełnij: zwróć liczbę minut od północy albo zgłoś BladFormatu / BladZakresu.
    pass


n = int(input())
for _ in range(n):
    tekst = input()
    # Uzupełnij: wywołaj parsuj_godzine(tekst) w bloku try
    # i obsłuż błędy klauzulą except BladDanych as e.
```

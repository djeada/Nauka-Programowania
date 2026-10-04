r"""
ZAD-05 — Dziedziczenie wielokrotne: Ptak

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
        pass

    def jedz(self):
        pass

    def spij(self):
        pass

    def wydaj_dzwiek(self):
        pass


class ObiektLatajacy:
    def __init__(self, imie):
        pass

    def lec(self):
        pass

    def wyladuj(self):
        pass


class Ptak(Zwierz, ObiektLatajacy):
    def __init__(self, imie):
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

"""


class Zwierz:
    def __init__(self, imie):
        self.imie = imie

    def jedz(self):
        print(f"{self.imie} je.")

    def spij(self):
        print(f"{self.imie} śpi.")

    def wydaj_dzwiek(self):
        print(f"{self.imie} wydaje dźwięk.")


class ObiektLatajacy:
    def __init__(self, imie):
        self.imie = imie
        self.w_powietrzu = False

    def lec(self):
        if self.w_powietrzu:
            print(f"{self.imie} już leci.")
        else:
            print(f"{self.imie} leci.")
            self.w_powietrzu = True

    def wyladuj(self):
        if self.w_powietrzu:
            print(f"{self.imie} ląduje.")
            self.w_powietrzu = False
        else:
            print(f"{self.imie} jest już na ziemi.")


class Ptak(Zwierz, ObiektLatajacy):
    def __init__(self, imie):
        Zwierz.__init__(self, imie)
        ObiektLatajacy.__init__(self, imie)


if __name__ == "__main__":
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

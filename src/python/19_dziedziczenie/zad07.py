r"""
ZAD-07 — Hierarchia własnych wyjątków

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


def parsuj_godzine(tekst):
    pass


n = int(input())
for _ in range(n):
    tekst = input()
```

"""


class BladDanych(Exception):
    pass


class BladFormatu(BladDanych):
    pass


class BladZakresu(BladDanych):
    pass


def parsuj_godzine(tekst):
    if len(tekst) != 5 or tekst[2] != ":" or not (tekst[:2] + tekst[3:]).isdigit():
        raise BladFormatu("oczekiwano formatu GG:MM")
    godziny = int(tekst[:2])
    minuty = int(tekst[3:])
    if godziny > 23:
        raise BladZakresu("godzina spoza zakresu 0-23")
    if minuty > 59:
        raise BladZakresu("minuty spoza zakresu 0-59")
    return 60 * godziny + minuty


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        tekst = input()
        try:
            print(f"{tekst} -> {parsuj_godzine(tekst)}")
        except BladDanych as e:
            print(f"{tekst} -> {type(e).__name__}: {e}")

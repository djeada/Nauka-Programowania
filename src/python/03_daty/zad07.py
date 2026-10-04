r"""
ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)

**Poziom:** ★★☆
**Tagi:** `sumowanie`, `tablice`, `przestępny`

### Treść

Wczytaj datę `d`, `m`, `y` i oblicz numer dnia w roku, tzn. ile dni minęło od 1 stycznia do tej daty **włącznie** (1 stycznia to dzień 1, 31 grudnia to dzień 365 albo 366 w roku przestępnym).

### Wejście

3 liczby całkowite, każda w osobnej linii: `d`, `m`, `y`.

### Wyjście

Jedna liczba całkowita: numer dnia w roku.

### Ograniczenia

* Podana data jest poprawna (nie musisz jej sprawdzać).
* $1 \le y \le 9999$

### Przykład

**Wejście:**

```
14
2
1482
```

**Wyjście:**

```
45
```

31 dni stycznia + 14 dni lutego = 45.

### Uwagi

* Wygodnie jest skorzystać z łańcucha `if`/`elif`, w którym dla każdego miesiąca zapisujesz, ile dni roku nieprzestępnego upłynęło **przed** jego początkiem: styczeń 0, luty 31, marzec 59, kwiecień 90, maj 120, czerwiec 151, lipiec 181, sierpień 212, wrzesień 243, październik 273, listopad 304, grudzień 334. Do tej liczby dodaj `d`.
* W roku przestępnym luty ma 29 dni, więc dla dat od 1 marca dodaj jeszcze 1.
* Po rozdziale o pętlach możesz te sumy obliczać w pętli, dodając długości kolejnych miesięcy.

"""


def czy_przestepny(rok):
    return rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0)


def dni_przed_miesiacem(miesiac):
    """Liczba dni roku nieprzestępnego, które upłynęły przed początkiem miesiąca."""
    if miesiac == 1:
        return 0
    elif miesiac == 2:
        return 31
    elif miesiac == 3:
        return 59
    elif miesiac == 4:
        return 90
    elif miesiac == 5:
        return 120
    elif miesiac == 6:
        return 151
    elif miesiac == 7:
        return 181
    elif miesiac == 8:
        return 212
    elif miesiac == 9:
        return 243
    elif miesiac == 10:
        return 273
    elif miesiac == 11:
        return 304
    else:
        return 334


def dzien_roku(dzien, miesiac, rok):
    numer = dni_przed_miesiacem(miesiac) + dzien
    if miesiac > 2 and czy_przestepny(rok):
        numer += 1
    return numer


if __name__ == "__main__":
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())
    print(dzien_roku(dzien, miesiac, rok))

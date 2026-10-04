# Rozdział 3: Daty (warunki + kalendarz)

Zadania w tym rozdziale dotyczą walidacji i obliczeń na datach w kalendarzu gregoriańskim.

**Konwencje wspólne:**

* Każde zadanie to **osobny program**: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Liczby wczytuj z osobnych linii, w kolejności z opisu. Data jest zawsze podawana jako trzy liczby: dzień, miesiąc, rok.
* Komunikaty wypisuj **dokładnie** jak w treści (kropki, polskie znaki, wielkość liter, spacje).
* Jeśli zadanie mówi „nie wypisuj nic” — program kończy się bez żadnego wyjścia.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* We wszystkich zadaniach obowiązuje kalendarz gregoriański (także dla lat sprzed 1582 roku). Rok jest **przestępny**, gdy jest podzielny przez 4 i nie jest podzielny przez 100, albo gdy jest podzielny przez 400 (np. 2024 i 2000 są przestępne, a 2023 i 1900 — nie). Luty ma w roku przestępnym 29 dni, a w nieprzestępnym 28.

---

## ZAD-01 — Numer dnia tygodnia lub miesiąca

**Poziom:** ★☆☆
**Tagi:** `if`, `zakresy`, `I/O`

### Treść

Wczytaj liczbę całkowitą `n` i sprawdź, czy może być numerem dnia tygodnia (1–7) i czy może być numerem miesiąca (1–12). Wypisz:

* `Liczba jest numerem dnia tygodnia i numerem miesiąca.` — gdy $1 \le n \le 7$,
* `Liczba jest tylko numerem miesiąca.` — gdy $8 \le n \le 12$,
* `Liczba nie jest numerem dnia tygodnia ani miesiąca.` — w pozostałych przypadkach.

### Wejście

* 1 linia: `n` — liczba całkowita, $-1000 \le n \le 1000$

### Wyjście

Jedna linia — dokładnie jeden z trzech komunikatów.

### Przykład 1

**Wejście:**

```
5
```

**Wyjście:**

```
Liczba jest numerem dnia tygodnia i numerem miesiąca.
```

### Przykład 2

**Wejście:**

```
15
```

**Wyjście:**

```
Liczba nie jest numerem dnia tygodnia ani miesiąca.
```

---

## ZAD-02 — Pełnoletność (18 lat)

**Poziom:** ★☆☆
**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiejszą” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty dzisiejszej.

Pełnoletność osiąga się **w dniu 18. urodzin**. Osoba jest więc pełnoletnia wtedy, gdy data (`d1`, `m1`, `y1 + 18`) jest **nie późniejsza** niż data dzisiejsza (`d2`, `m2`, `y2`). Daty porównuj najpierw po roku, przy równych latach po miesiącu, a przy równych miesiącach po dniu.

Wypisz:

* `Osoba jest pełnoletnia.` — jeśli ma ukończone 18 lat,
* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych, każda w osobnej linii:

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — dzisiejszy dzień
5. `m2` — dzisiejszy miesiąc
6. `y2` — dzisiejszy rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia

* Obie daty są poprawne (nie musisz ich sprawdzać), $1 \le y1, y2 \le 9999$.
* Data urodzenia nie jest późniejsza niż data dzisiejsza.

### Przykład

**Wejście:**

```
5
12
1999
20
11
2020
```

**Wyjście:**

```
Osoba jest pełnoletnia.
```

Osiemnaste urodziny wypadły 5.12.2017, a więc przed 20.11.2020.

### Uwagi

* Porównujesz same liczby, więc data (`d1`, `m1`, `y1 + 18`) nie musi istnieć w kalendarzu. Osoba urodzona 29 lutego obchodzi 18. urodziny w roku nieprzestępnym (np. urodzona 29.02.2004 — w 2022 roku), więc zgodnie z regułą 28 lutego jest jeszcze niepełnoletnia, a pełnoletnia staje się 1 marca.

---

## ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

Wypisz:

* `Rok jest przestępny.` — jeśli rok jest przestępny,
* `Rok nie jest przestępny.` — w przeciwnym razie.

### Wejście

* 1 linia: `y` — liczba całkowita, $1 \le y \le 9999$

### Wyjście

Jedna linia — odpowiedni komunikat.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

Rok 2100 jest podzielny przez 4 i przez 100, ale nie przez 400.

---

## ZAD-04 — Dzień tygodnia z numeru

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `mapowanie`, `string`

### Treść

Wczytaj liczbę `n`. Jeśli `n` jest w zakresie 1–7, wypisz nazwę dnia tygodnia:

1. `Poniedziałek`
2. `Wtorek`
3. `Środa`
4. `Czwartek`
5. `Piątek`
6. `Sobota`
7. `Niedziela`

W przeciwnym razie wypisz:
`Niepoprawny numer dnia tygodnia.`

### Wejście

* 1 linia: `n` — liczba całkowita, $0 \le n \le 1000$

### Wyjście

Jedna linia: nazwa dnia (wielką literą, z polskimi znakami) lub komunikat o błędzie.

### Przykład 1

**Wejście:**

```
5
```

**Wyjście:**

```
Piątek
```

### Przykład 2

**Wejście:**

```
8
```

**Wyjście:**

```
Niepoprawny numer dnia tygodnia.
```

---

## ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu:

* 31 dni: styczeń (1), marzec (3), maj (5), lipiec (7), sierpień (8), październik (10), grudzień (12),
* 30 dni: kwiecień (4), czerwiec (6), wrzesień (9), listopad (11),
* 28 dni: luty (2).

Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` — liczba całkowita, $0 \le m \le 1000$

### Wyjście

Jedna linia: liczba dni **albo** komunikat o błędzie.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
28
```

---

## ZAD-06 — Sprawdzanie poprawności daty

**Poziom:** ★★☆
**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d`, `m`, `y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Data jest poprawna, gdy:

1. miesiąc `m` jest w zakresie 1–12,
2. dzień `d` jest w zakresie od 1 do liczby dni w miesiącu `m`:
   * 31 dni: miesiące 1, 3, 5, 7, 8, 10, 12,
   * 30 dni: miesiące 4, 6, 9, 11,
   * luty (2): 29 dni w roku przestępnym, 28 w nieprzestępnym (zob. konwencje rozdziału).

Wypisz:

* `Data jest poprawna.`
* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite, każda w osobnej linii:

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia

* $-100 \le d, m \le 100$ (dzień i miesiąc mogą być spoza poprawnego zakresu, także zerowe lub ujemne)
* $1 \le y \le 9999$ (rok zawsze jest poprawny)

### Przykład 1

**Wejście:**

```
31
4
2021
```

**Wyjście:**

```
Data jest niepoprawna.
```

Kwiecień ma tylko 30 dni.

### Przykład 2

**Wejście:**

```
29
2
2024
```

**Wyjście:**

```
Data jest poprawna.
```

Rok 2024 jest przestępny, więc luty ma 29 dni.

---

## ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)

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

---

## ZAD-08 — Dzień tygodnia dla daty (Zeller)

**Poziom:** ★★☆
**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d`, `m`, `y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli $m \le 2$, potraktuj styczeń i luty jako 13. i 14. miesiąc poprzedniego roku: $m = m + 12$, $y = y - 1$.
2. Oblicz:
   * $K = y \bmod 100$ (rok w stuleciu),
   * $J = \lfloor y / 100 \rfloor$ (stulecie),
   * $h = \left(d + \left\lfloor \frac{13(m+1)}{5} \right\rfloor + K + \left\lfloor \frac{K}{4} \right\rfloor + \left\lfloor \frac{J}{4} \right\rfloor + 5J\right) \bmod 7$.
3. Zamień `h` na dzień tygodnia:
   * 0 → `Sobota`
   * 1 → `Niedziela`
   * 2 → `Poniedziałek`
   * 3 → `Wtorek`
   * 4 → `Środa`
   * 5 → `Czwartek`
   * 6 → `Piątek`

### Wejście

3 liczby całkowite, każda w osobnej linii: `d`, `m`, `y`.

### Wyjście

Jedna linia: nazwa dnia tygodnia — dokładnie jedna z: `Poniedziałek`, `Wtorek`, `Środa`, `Czwartek`, `Piątek`, `Sobota`, `Niedziela`.

### Ograniczenia

* Podana data jest poprawna (nie musisz jej sprawdzać).
* $1 \le y \le 9999$

### Przykład

**Wejście:**

```
9
10
2020
```

**Wyjście:**

```
Piątek
```

$m = 10$, $y = 2020$, więc $K = 20$, $J = 20$, $h = (9 + 28 + 20 + 5 + 5 + 100) \bmod 7 = 167 \bmod 7 = 6$, czyli piątek.

### Uwagi

* W Pythonie $\lfloor a / b \rfloor$ to `a // b`, a $a \bmod b$ to `a % b`.

---

## ZAD-09 — Dni między datami (moduł datetime)

**Poziom:** ★★☆
**Tagi:** `datetime`, `daty`, `biblioteka standardowa`

### Treść

Wczytaj dwie daty i za pomocą modułu `datetime` z biblioteki standardowej Pythona oblicz:

1. liczbę dni między tymi datami — jako wartość bezwzględną różnicy, więc kolejność dat nie ma znaczenia,
2. nazwę dnia tygodnia **pierwszej** daty.

### Wejście

6 liczb całkowitych, każda w osobnej linii:

1. `d1` — dzień pierwszej daty
2. `m1` — miesiąc pierwszej daty
3. `y1` — rok pierwszej daty
4. `d2` — dzień drugiej daty
5. `m2` — miesiąc drugiej daty
6. `y2` — rok drugiej daty

### Wyjście

Dwie linie:

1. liczba dni między datami (liczba całkowita, $\ge 0$),
2. nazwa dnia tygodnia pierwszej daty — dokładnie jedna z: `Poniedziałek`, `Wtorek`, `Środa`, `Czwartek`, `Piątek`, `Sobota`, `Niedziela`.

### Ograniczenia

* Obie daty są poprawne (nie musisz ich sprawdzać).
* $1 \le y1, y2 \le 9999$

### Przykład

**Wejście:**

```
9
10
2020
1
1
2021
```

**Wyjście:**

```
84
Piątek
```

Od 9 października 2020 do 1 stycznia 2021 mijają 84 dni: 22 do końca października, 30 w listopadzie, 31 w grudniu i 1 w styczniu.

### Uwagi

* Moduł `datetime` udostępnia typ `date`, który reprezentuje jedną datę. Tworząc ją, podaj kolejno **rok, miesiąc, dzień**:

  ```python
  from datetime import date

  pierwsza = date(2020, 10, 9)
  druga = date(2021, 1, 1)
  print((druga - pierwsza).days)   # 84
  print((pierwsza - druga).days)   # -84
  print(pierwsza.weekday())        # 4
  ```

* Różnica dwóch dat to odcinek czasu (`timedelta`); liczbę dni odczytasz z jego pola `.days`. Może być ujemna, więc użyj `abs(...)`.
* Metoda `weekday()` zwraca 0 dla poniedziałku, 1 dla wtorku, …, 6 dla niedzieli — to inna numeracja niż `h` w kongruencji Zellera z ZAD-08 (tam 0 oznacza sobotę).
* Moduł sam uwzględnia lata przestępne. Porównaj go z ZAD-07 i ZAD-08: `(data - date(rok, 1, 1)).days + 1` to numer dnia w roku, a `weekday()` zastępuje wzór Zellera — dobry sposób na sprawdzenie swoich wcześniejszych rozwiązań.

### Kod startowy

```python
from datetime import date

d1 = int(input())
m1 = int(input())
y1 = int(input())
d2 = int(input())
m2 = int(input())
y2 = int(input())

# Uzupełnij: utwórz obiekty date, oblicz liczbę dni między nimi
# i wypisz nazwę dnia tygodnia pierwszej daty.
```

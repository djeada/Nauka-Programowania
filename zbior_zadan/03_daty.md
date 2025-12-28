# Rozdział: Daty (warunki + kalendarz)

Zadania w tym rozdziale dotyczą walidacji i obliczeń na datach w kalendarzu gregoriańskim.

**Konwencje wspólne:**

* Każde zadanie to **osobny program**.
* Liczby wczytuj z osobnych linii, w kolejności z opisu.
* Komunikaty wypisuj **dokładnie** jak w treści (kropki, polskie znaki, spacje).
* Jeśli zadanie mówi „nie wypisuj nic” — program kończy się bez żadnego wyjścia.

---

## ZAD-01 — Numer dnia tygodnia lub miesiąca

**Poziom:** ★☆☆
**Tagi:** `if`, `zakresy`, `I/O`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz `n` **tylko wtedy**, gdy jest poprawnym numerem:

* dnia tygodnia (1–7) **lub**
* miesiąca (1–12).

W praktyce oznacza to: wypisz `n` tylko wtedy, gdy `1 ≤ n ≤ 12`.

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

* Jeśli `1 ≤ n ≤ 12`: wypisz `n` w osobnej linii
* W przeciwnym razie: brak wyjścia

### Przykłady

**Wejście:**

```
5
```

**Wyjście:**

```
5
```

**Wejście:**

```
15
```

**Wyjście:** *(brak)*

---

## ZAD-02 — Pełnoletność (18 lat)

**Poziom:** ★☆☆
**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiaj” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty aktualnej.

Wypisz:

* `Osoba jest pełnoletnia.` — jeśli ma ≥ 18 lat,
* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych (każda w osobnej linii):

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — aktualny dzień
5. `m2` — aktualny miesiąc
6. `y2` — aktualny rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia / gwarancje

* Obie daty są poprawne (nie musisz walidować).
* Pełnoletność jest osiągana **dokładnie w dniu 18. urodzin**.

### Uwagi (jak to porównać)

Osoba jest pełnoletnia wtedy, gdy data `y1+18, m1, d1` jest **nie późniejsza** niż data aktualna.

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

---

## ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

* `Rok jest przestępny.`
* `Rok nie jest przestępny.`

### Wejście

* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

---

## ZAD-04 — Dzień tygodnia z numeru

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `mapowanie`, `string`

### Treść

Wczytaj liczbę `n`. Jeśli `n` jest w zakresie 1–7, wypisz nazwę dnia tygodnia:

1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek
6. Sobota
7. Niedziela

W przeciwnym razie wypisz:
`Niepoprawny numer dnia tygodnia.`

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

Jedna linia: nazwa dnia lub komunikat o błędzie.

### Przykład

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

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

* liczba dni (jedna linia) **albo**
* komunikat o błędzie (jedna linia)

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

Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Wypisz:

* `Data jest poprawna.`
* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite (w osobnych liniach):

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia / gwarancje

* `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w całym zbiorze)

### Reguły walidacji

1. `m` musi być w zakresie 1–12
2. Ustal liczbę dni w miesiącu:

   * 31: 1,3,5,7,8,10,12
   * 30: 4,6,9,11
   * luty: 28 lub 29 (zależnie od przestępności roku)
3. `d` musi być w zakresie 1–dni_w_miesiącu

### Przykład

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

---

## ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)

**Poziom:** ★★☆
**Tagi:** `sumowanie`, `tablice`, `przestępny`

### Treść

Wczytaj datę `d, m, y` i oblicz numer dnia w roku, tzn. ile dni minęło od 1 stycznia do tej daty **włącznie**.

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna liczba całkowita: numer dnia w roku.

### Ograniczenia / gwarancje

* Podana data jest poprawna (nie musisz jej sprawdzać), **albo** możesz jawnie napisać: „jeśli data jest niepoprawna, zachowanie nieokreślone”.

  * (Najczyściej: dać gwarancję poprawności.)

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

---

## ZAD-08 — Dzień tygodnia dla daty (Zeller)

**Poziom:** ★★☆
**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d, m, y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli `m <= 2`, to:

* `m = m + 12`
* `y = y - 1`

2. Oblicz:

* `K = y % 100`
* `J = y // 100`
* `h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7`

3. Zmapuj `h` na dzień tygodnia:

* 0 → `Sobota`
* 1 → `Niedziela`
* 2 → `Poniedziałek`
* 3 → `Wtorek`
* 4 → `Środa`
* 5 → `Czwartek`
* 6 → `Piątek`

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna linia: nazwa dnia tygodnia (dokładnie jedna z: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela).

### Ograniczenia / gwarancje

* Data wejściowa jest poprawna (zalecane; inaczej dopisz, co robić dla błędnej).
* Kalendarz gregoriański.

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

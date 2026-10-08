/*
ZAD-08 — Liczby doskonałe, obfite i deficytowe

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `dzielniki`

### Treść

**Dzielnik właściwy** liczby naturalnej `n` to jej dzielnik mniejszy od `n` — np. dzielnikami właściwymi liczby `12` są `1`, `2`, `3`, `4` i `6`. Porównując sumę dzielników właściwych z samą liczbą, dzielimy liczby na trzy rodzaje:

* **doskonałe** — suma jest równa `n` (np. $6 = 1 + 2 + 3$),
* **obfite** — suma jest większa od `n` (np. $1 + 2 + 3 + 4 + 6 = 16 > 12$),
* **deficytowe** — suma jest mniejsza od `n` (np. dla `8`: $1 + 2 + 4 = 7 < 8$).

Napisz dwie funkcje:

1. `suma_dzielnikow(n)` — zwraca sumę dzielników właściwych liczby `n`,
2. `rodzaj_liczby(n)` — **wywołuje** funkcję `suma_dzielnikow(n)` i na podstawie jej wyniku zwraca napis `doskonała`, `obfita` albo `deficytowa`.

Program wczytuje `k` liczb i dla każdej wypisuje jej rodzaj.

### Wejście

* 1. linia: `k` — liczba liczb do sprawdzenia
* kolejne `k` linii: liczby naturalne `n` — po jednej w linii

### Wyjście

`k` linii w formacie:

```
<n>: <rodzaj>
```

gdzie `<rodzaj>` to `doskonała`, `obfita` albo `deficytowa` (małymi literami, z polskimi znakami).

### Ograniczenia

* $1 \le k \le 100$
* $1 \le n \le 10000$

### Przykład

**Wejście:**

```
3
6
12
15
```

**Wyjście:**

```
6: doskonała
12: obfita
15: deficytowa
```

Dla `15` suma dzielników właściwych to $1 + 3 + 5 = 9 < 15$.

### Uwagi

* Liczba `1` nie ma dzielników właściwych, więc ich suma wynosi `0` — `1` jest liczbą deficytową.
* Wydzielenie obliczeń do osobnej funkcji sprawia, że `rodzaj_liczby` jest krótka i czytelna, a `suma_dzielnikow` da się sprawdzić i wykorzystać niezależnie.

### Kod startowy

```python
def suma_dzielnikow(n):
    pass


def rodzaj_liczby(n):
    pass


k = int(input())
for _ in range(k):
    n = int(input())
    print(f"{n}: {rodzaj_liczby(n)}")
```

*/
const linie = require("fs").readFileSync(0, "utf8").split("\n");

// Suma dzielników właściwych liczby n (dzielników mniejszych od n)
function sumaDzielnikow(n) {
  let suma = 0;
  for (let d = 1; d <= Math.floor(n / 2); d++) {
    if (n % d === 0) {
      suma += d;
    }
  }
  return suma;
}

// Rodzaj liczby na podstawie sumy jej dzielników właściwych
function rodzajLiczby(n) {
  const suma = sumaDzielnikow(n);
  if (suma === n) {
    return "doskonała";
  }
  if (suma > n) {
    return "obfita";
  }
  return "deficytowa";
}

const k = parseInt(linie[0], 10);
for (let i = 1; i <= k; i++) {
  const n = parseInt(linie[i], 10);
  console.log(`${n}: ${rodzajLiczby(n)}`);
}

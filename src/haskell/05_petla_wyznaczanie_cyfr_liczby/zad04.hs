{-
ZAD-04A — Cyfry parzyste

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie jej cyfry, które są **parzyste**. Każdą cyfrę wypisz w osobnej linii.

Cyfry analizuj od końca (od jedności), czyli w tej samej kolejności, co w zadaniu o wypisywaniu cyfr w odwrotnej kolejności.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Cyfry parzyste liczby `n`, każda w nowej linii (w kolejności od jedności do najwyższej cyfry).
Jeśli nie ma takich cyfr — brak wyjścia.

### Przykład

**Wejście:**

```
932
```

**Wyjście:**

```
2
```

ZAD-04B — Cyfry mniejsze niż 5

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie jej cyfry, które są **mniejsze niż 5**. Każdą cyfrę wypisz w osobnej linii.

Cyfry analizuj od końca (od jedności).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Cyfry < 5, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
1
0
1
```

ZAD-04C — Cyfry różne od zera

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie jej cyfry, które są **różne od zera**. Każdą cyfrę wypisz w osobnej linii.

Cyfry analizuj od końca (od jedności).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Cyfry ≠ 0, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład

**Wejście:**

```
650
```

**Wyjście:**

```
5
6
```

### Uwagi o formatowaniu

* W przykładzie widać kolejność od jedności: najpierw `5`, potem `6`.

-}
main :: IO ()
main = pure ()

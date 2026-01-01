{-
ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Masz klasę `Miasto` z polami:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Otrzymujesz listę miast.

a) Posortuj miasta alfabetycznie po nazwie.
b) Posortuj miasta rosnąco po liczbie mieszkańców.

Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)

### Wyjście

* 1 linia: lista miast po sortowaniu a)
* 2 linia: lista miast po sortowaniu b)

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Uwagi o formatowaniu

* Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.

-}
main :: IO ()
main = pure ()

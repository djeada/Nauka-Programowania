{-
ZAD-06 — Statystyki pliku tekstowego

**Poziom:** ★★☆
**Tagi:** `files`, `stats`, `dict`, `regex`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Oblicz:

a) liczbę wierszy,
b) łączną liczbę słów (słowa = ciągi liter),
c) średnią długość wiersza (w znakach),
d) średnią liczbę słów na wiersz,
e) częstość występowania słów (słownik).

### Wejście

* 1 linia: `file_path`

### Wyjście

5 elementów w tej kolejności:

1. liczba wierszy
2. liczba słów
3. średnia długość wiersza
4. średnia liczba słów na wiersz
5. słownik częstości słów

Każdy element wypisz w osobnej linii.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\tekst.txt
```

**Wyjście:**

```
4
12
17.75
3.0
{'ala': 2, 'ma': 2, 'kota': 1, 'kot': 1, 'na': 1, 'imię': 1, 'filemon': 1, 'filemona': 1, 'lubi': 2, 'mleko': 1}
```

### Uwagi o formatowaniu

* Jeżeli ujednolicisz wielkość liter — w słowniku używaj małych liter (jak w przykładzie).
* Interpunkcję traktuj jako separator (usuń ją przy wyznaczaniu słów).

-}
main :: IO ()
main = pure ()

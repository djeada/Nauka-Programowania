## Instrukcje sterujące

### Zad 1. (★☆☆)

Tytuł: Porównanie ze stałą.

Treść: Pobierz od użytkownika liczbę naturalną. Jeśli ta liczba jest większa niż 5, wypisz ją.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna lub brak danych wyjściowych.

Przykład:

Dla pobranej liczby: 10, powinna zostać wypisana liczba: 10.

### Zad 2. (★☆☆)

Tytuł: Porównanie ze zmienną.

Treść: Pobierz od użytkownika dwie liczby naturalne i sprawdź, czy są one identyczne. Wypisz odpowiedni komunikat.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Komunikat.

Przykład:

Dla pobranych liczb: 7 i 4, powinien zostać wypisany komunikat, że liczby są różne.

### Zad 3. (★☆☆)

Tytuł: Znak liczby.

Treść: Pobierz liczbę naturalną od użytkownika i sprawdź, czy liczba jest ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla pobranej liczby: 2, powinien zostać wypisany komunikat, że liczba jest dodatnia.

### Zad 4. (★☆☆)

Tytuł: Maksimum i minimum z dwóch liczb.

Treść: Pobierz od użytkownika dwie liczby naturalne i wypisz najpierw większą, a potem mniejszą.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Dla pobranych liczb: 1 oraz 4, powinny zostać wypisane liczby: 4 i 1.

### Zad 5. (★★☆)

Tytuł: Posortowanie trzech liczb.

Treść: Pobierz od użytkownika trzy liczby naturalne i wypisz je w kolejności rosnącej.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Trzy liczby naturalne.

Przykład:

Dla pobranych liczb: 2, 1 oraz 4, powinny zostać wypisane liczby: 1, 2 i 4.

### Zad 6. (★☆☆)

Tytuł: Maks z czterech liczb.

Treść: Dla czterech pobranych liczb naturalnych, wypisz największą z nich.

Dane wejściowe: Cztery liczby naturalne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla pobranych liczb: 2, 5, 1 i 4, powinna zostać wypisana liczba: 5.

### Zad 7. (★☆☆)

Tytuł: Dowody praw logicznych.

Treść: Pokaż za pomocą operacji logicznych następujące prawa:

a) Prawo wyłączonego środka.

b) Prawo niesprzeczności.

c) Przemienność koniunkcji.

d) Przemienność alternatywy.

e) Pierwsze prawo de Morgana.

f) Drugie prawo de Morgana.

Dane wejściowe: Brak.

Dane wyjściowe: Komunikat.

a) Prawo wyłączonego środka:
  - Dla p mającego wartość logiczną: `False` wyrażenie p v ~p ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` wyrażenie p v ~p ma wartość logiczną: `True`.

b) Zasada niesprzeczności:
  - Dla p mającego wartość logiczną: `False` wyrażenie ~(p Ʌ ~p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` wyrażenie ~(p Ʌ ~p) ma wartość logiczną: `True`.

c) Przemienność koniunkcji:
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `True` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.

d) Przemienność alternatywy:
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `True` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.

e) Pierwsze prawo de Morgana:
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `True` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.

f) Drugie prawo de Morgana:
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
  - Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczna: `True` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.

### Zad 8. (★☆☆)

Tytuł: Warunek trójkąta.

Treść: Dla trzech pobranych od użytkownika długości boków sprawdź, czy można z nich zbudować trójkąt. Jednostki są umowne.

Dane wejściowe: Trzy liczby naturalne oznaczające długości boków trójkąta.

Dane wyjściowe: Komunikat o możliwości lub niemożliwości zbudowania trójkąta.

Przykład:

Dla pobranych liczb: 1, 2 oraz 3, powinna zostać wypisana informacja, że nie można zbudować trójkąta z podanych boków.

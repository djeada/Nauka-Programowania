## Funkcje — rekurencja

### Zad 1. (★☆☆)

Tytuł: Liczby naturalne mniejsze od N.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji stwórz napis składający się z liczb naturalnych mniejszych od N oddzielonych przecinkami.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Napis.

Przykład:

Dla N = 10, powinien zostać zwrócony napis: "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0".

### Zad 2. (★☆☆)

Tytuł: Suma liczb naturalnych mniejszych od N.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz sumę liczb naturalnych mniejszych od N.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 10, powinna zostać zwrócona liczba: 55.

### Zad 3. (★☆☆)

Tytuł: Potęga.

Treść: Otrzymujesz dwie liczby, a i b. Przy użyciu rekurencji oblicz a podniesione do b.

Dane wejściowe: Dwie liczby naturalne a i b.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla a = 2 i b = 3, powinna zostać zwrócona liczba: 8.

### Zad 4. (★☆☆)

Tytuł: Silnia.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz silnię z tej liczby.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 3, powinna zostać zwrócona liczba: 6.

### Zad 5. (★☆☆)

Tytuł: Liczba Fibonacciego.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz wartość N-tego wyrazu ciągu Fibonacciego.

Podpowiedź: Ciąg Fibonacciego zdefiniowany jest następująco:

* $a_0= 0$,
* $a_1= 1$,
* $a_n= a_{n-1}+a_n-2$.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 7, powinna zostać zwrócona liczba: 13.

### Zad 6. (★☆☆)

Tytuł: N-ty wyraz ciągu danego wzorem rekurencyjnym.

Treść: Otrzymujesz liczbę N. Oblicz wartość N-tego wyrazu ciągu danego wzorem rekurencyjnym:

* $a_1 = 1$
* $a_n = 1+2*a_{n-1}$

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 5, powinna zostać zwrócona liczba: 31.

### Zad 7. (★★☆)

Tytuł: Wyszukiwanie liniowe rekurencyjnie.

Treść: Otrzymujesz listę liczb naturalnych oraz liczbę naturalną klucz. Przy użyciu rekurencji znajdź indeks odpowiadający pierwszemu wystąpieniu klucza w liście. Jeśli klucz nie występuje w liście, zwróć -1.

Dane wejściowe: Lista liczb naturalnych oraz liczba naturalna klucz.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy oraz liczby: [1, 2, 2] i 2, powinna zostać zwrócona liczba: 1.

### Zad 8. (★★☆)

Tytuł: Wieża Hanoi.

Treść: N krążków o różnych średnicach ułożonych jest na jednym z trzech słupków (A, B lub C). Na dole znajduje się krążek o największej średnicy. Każdy następny jest mniejszy od poprzedniego. Znajdź sposób na przełożenie wszystkich krążków na inny słupek. Pamiętaj, że nie wolno kłaść krążka o większej średnicy na krążek o mniejszej średnicy, ani przekładać kilku krążków jednocześnie.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Lista par znaków.

Przykład:

Dla N = 3, powinna zostać zwrócona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]

### Zad 9. (★★☆)

Tytuł: Słowa elfickie.

Treść: Otrzymujesz napis. Przy użyciu rekurencji sprawdź czy otrzymane słowo jest słowem elfickim. Przez słowo elfickie rozumiemy taki napis, w którym co najmniej raz występuje każda z liter słowa elf.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:
Dla otrzymanego napisu: "reflektor", powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 10. (★★☆)

Tytuł: Gra.	

Treść: W grze, w każdym ruchu gracz może zdobyć 3, 5 lub 10 punktów. Oblicz przy użyciu rekurencji, ile sposobów istnieje, aby gracz wygrał grę, gdy ma do dyspozycji N punktów.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:
Dla N = 20, powinna zostać zwrócona liczba: 4.

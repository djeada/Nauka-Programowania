## Sortowanie — praktyka

### Zad 1.  (★☆☆)

Tytuł: Sortowanie znaków w napisie.

Treść: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla napisu "Ala ma kota" powinno zostać zwrócone " Aaaaklmot".

### Zad 2.  (★★☆)

Tytuł: Sortowanie słów w zdaniu.

Treść: Masz dany napis reprezentujący zdanie. Podziel to zdanie na słowa, posortuj je alfabetycznie i zapisz w liście. Znaki interpunkcyjne nie są liczone jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla napisu "Lemur wygina śmiało ciało" powinno zostać zwrócone ["Lemur", "ciało", "śmiało", "wygina"].

### Zad 3.  (★☆☆)

Tytuł: Sortowanie listy par względem jednej z kategorii.

Treść: Masz daną listę par napisów i liczb. Posortuj pary w liście względem:

a) Liczb.
b) Długości napisów.

Dane wejściowe: Lista par napisów i liczb.

Dane wyjściowe: Lista par napisów i liczb.

Przykład:

Dla listy [(“ab”, 3), (“bca”, 1), (“c”, 2)] powinno zostać zwrócone:

a) [(“bca”, 1), (“c”, 2), (“ab”, 3)] lub
b) [(“c”, 2), (“ab”, 3), (“bca”, 1)].

### Zad 4.  (★☆☆)

Tytuł: Sortowanie napisów w liście względem długości.

Treść: Masz daną listę napisów. Posortuj napisy w liście względem długości.

Dane wejściowe: Lista napisów.

Dane wyjściowe: Lista napisów.

Przykład:

Dla listy ["abcd", "ab", "a", "abc"] powinno zostać zwrócone ["a", "ab", "abc", "abcd"].

### Zad 5.  (★☆☆)

Tytuł: Sortowanie listy miast.

Treść: Klasa Miasto ma dwie właściwości: nazwa (napis) oraz liczba_mieszkańców (liczba naturalna). Posortuj listę miast względem nazwy oraz względem liczby mieszkańców.

Dane wejściowe: Lista miast.

Dane wyjściowe: Posortowana lista miast.

Przykład:
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostać zwrócona lista: [Miasto("Berlin", 3800000), Miasto("New York", 8400000), Miasto("Paris", 2150000)].
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostać zwrócona lista: [Miasto("Berlin", 3800000), Miasto("Paris", 2150000), Miasto("New York", 8400000)].

### Zad 6.  (★★☆)

Tytuł: Sortowanie listy binarnej.

Treść: Otrzymujesz listę liczb składających się tylko z zer i jedynek. Posortuj tę listę.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Posortowana lista liczb naturalnych.

Przykład:
Dla listy: [1, 0, 1, 0, 1, 1], powinna zostać zwrócona lista: [0, 0, 1, 1, 1, 1].

### Zad 7.  (★★☆)

Tytuł: Sortowanie listy liczb z zakresu 0-2.

Treść: Otrzymujesz listę liczb składających się tylko z zer, jedynek i dwójek. Posortuj tę listę.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Posortowana lista liczb naturalnych.

Przykład:
Dla listy: [1, 0, 1, 2, 2, 0, 1], powinna zostać zwrócona lista: [0, 0, 1, 1, 1, 2, 2].

### Zad 8.  (★★☆)

Tytuł: Wyszukiwanie indeksu klucza w cyklicznie posortowanej liście.

Treść: Otrzymujesz cyklicznie posortowaną listę oraz klucz. Znajdź indeks pierwszego wystąpienia klucza w liście. Jeśli klucz nie występuje w liście, zwróć -1.

Dane wejściowe: Cyklicznie posortowana lista, klucz.

Dane wyjściowe: Indeks pierwszego wystąpienia klucza lub -1.

Przykład:

Dla cyklicznie posortowanej listy [3, 4, 5, 6, 1, 2] i klucza 4, powinno zostać zwrócone 2.

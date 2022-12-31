## Listy — wprowadzenie

### Zad 1. (★☆☆)

Tytuł: Wczytaj i wypisz.

Treść: Dla podanej liczby naturalnej N, wczytaj N liczb całkowitych do listy, a następnie:

a) Wypisz listę od początku do końca, z każdym elementem w osobnym wierszu.

b) Wypisz listę od końca, z elementami oddzielonymi przecinkami i wypisanymi w jednym wierszu.

Dane wejściowe: N liczb całkowitych.

Dane wyjściowe: N liczb.

Przykład:

Dla N równego 3 oraz pobranych liczb: 8, 12, 7, w drugim podpunkcie powinno zostać wypisane: 7, 12, 8.

### Zad 2. (★☆☆)

Tytuł: Wczytaj, zmodyfikuj i wypisz.

Treść: Wczytaj liczbę całkowitą N oraz N liczb całkowitych i umieść je w liście. Następnie:

a) Dodaj 1 do każdego elementu listy.

b) Pomnóż każdy element przez jego indeks w liście (indeksy zaczynają się od 0).

c) Zastąp wszystkie elementy wartością pierwszego elementu listy.

Dla każdego z powyższych podpunktów wypisz zmodyfikowaną listę. Elementy listy powinny być oddzielone przecinkami i wypisane w jednym wierszu.

Dane wejściowe: N oraz N liczb całkowitych.

Dane wyjściowe: N liczb całkowitych.

Przykład:

Dla N równego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostać wypisana: 4, 10, 8.

### Zad 3. (★☆☆)

Tytuł: Pierwsze wystąpienie klucza.

Treść: Otrzymujesz listę liczb naturalnych oraz liczbę naturalną jako klucz. Znajdź indeks odpowiadający pierwszemu wystąpieniu klucza w liście. Jeśli klucz nie występuje w liście, zwróć -1.

Dane wejściowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.

Dane wyjściowe: Liczba całkowita oznaczająca indeks pierwszego wystąpienia klucza w liście.

Przykład:

Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostać zwrócone 2.

### Zad 4. (★☆☆)

Tytuł: Minimum oraz maksimum.

Treść: Otrzymujesz listę liczb całkowitych. Znajdź największy i najmniejszy element tej listy i zwróć je jako dwie osobne liczby całkowite.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Dwie liczby całkowite oznaczające największy i najmniejszy element z listy.

Przykład:

Dla otrzymanej listy [4, -7, 8, 5, 6, -9, 10, 2, -8] powinny zostać zwrócone liczby 10 oraz -9.

### Zad 5. (★☆☆)

Tytuł: Zmodyfikuj elementy spełniające warunek.

Treść: Otrzymujesz listę liczb całkowitych. W wyniku wykonania poniższych poleceń otrzymasz nową listę:

a) Zwiększ o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynają się od 0).

b) Wyzeruj wszystkie elementy będące wielokrotnościami liczby 3.

c) Podnieś do kwadratu wszystkie elementy mniejsze niż 10.

d) Wstaw sumę wszystkich elementów otrzymanej listy na indeksy będące liczbami pierwszymi.

e) Zamień każdy element na iloczyn wszystkich elementów listy poza nim samym.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy [5, 7, 9, 4, 2]:

a) Wynik: [5, 8, 9, 5, 2]

b) Wynik: [5, 0, 0, 5, 2]

c) Wynik: [25, 0, 0, 25, 4]

d) Wynik: [37, 0, 0, 25, 4]

e) Wynik: [2592, 0, 0, 36, 1080]

### Zad 6. (★☆☆)

Tytuł: Czy średnia elementów znajduje się w liście?

Treść: Dla otrzymanej listy liczb całkowitych oraz liczby całkowitej jako klucza, usuń pierwsze wystąpienie klucza w liście.

Dane wejściowe: Lista liczb całkowitych i liczba całkowita jako klucz.

Dane wyjściowe: Lista liczb całkowitych bez pierwszego wystąpienia klucza.

Przykład:

Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostać zwrócona lista [6, 2, 1, 27].

### Zad 7. (★☆☆)

Tytuł: Liczba mniejsza od największej i większa od wszystkich pozostałych.

Treść: Otrzymujesz listę liczb naturalnych. Znajdź największą i drugą co do wielkości liczbę w liście, a następnie oblicz średnią arytmetyczną tych dwóch liczb i zwróć ją jako liczbę zmiennoprzecinkową.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba zmiennoprzecinkowa oznaczająca średnią arytmetyczną największej i drugiej co do wielkości liczby z listy.

Przykład:

Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostać zwrócona liczba 8.0.

### Zad 8. (★☆☆)

Tytuł: Usuń klucz.

Treść: Dla otrzymanej listy: liczb całkowitych oraz klucza, usuń pierwsze wystąpienie klucza w liście.

Dane wejściowe: Lista liczb całkowitych i liczba całkowita.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [6, 2, 1, 4, 27] oraz 4, powinna zostać zwrócona lista: [6, 2, 1, 27].


### Zad 9. (★☆☆)

Tytuł: Usuń duplikaty.

Treść: Otrzymujesz listę liczb naturalnych. Usuń z niej wszystkie duplikaty, tak aby każda liczba pozostała tylko raz.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista liczb naturalnych.

Przykład:

Dla otrzymanej listy: [3, 2, 1, 3, 2, 2], powinna zostać zwrócona lista: [3, 2, 1].

### Zad 10. (★★☆)

Tytuł: Czy punkty mogą stanowić wierzchołki trójkąta?

Treść: Otrzymujesz dokładnie 6 liczb całkowitych, które odpowiadają współrzędnym punktów A, B, C w kolejności: xA, yA, xB, yB, xC, yC. Sprawdź, czy punkty A, B, C mogą stanowić wierzchołki trójkąta.

Dane wejściowe: Lista liczb całkowitych reprezentująca współrzędne punktów A, B, C.

Dane wyjściowe: Wartość logiczna określająca, czy punkty A, B, C mogą stanowić wierzchołki trójkąta.

Przykład:

Dla otrzymanej listy [-3, -2, -3, 1, -3, 0], powinna zostać zwrócona wartość logiczna: Fałsz.

### Zad 11. (★★☆)

Tytuł: Samochody jadące w przeciwnych kierunkach.

Treść: Otrzymujesz listę złożoną wyłącznie z liter 'A' i 'B', które odpowiadają samochodom jadącym odpowiednio na wschód ('A') i zachód ('B'). Policz, ile razy samochody jadące w przeciwnych kierunkach mijają się.

Dane wejściowe: Lista znaków odpowiadających samochodom jadącym na wschód ('A') i zachód ('B').

Dane wyjściowe: Liczba naturalna oznaczająca liczbę mijających się samochodów.

Przykład:

Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostać zwrócona liczba 5.

### Zad 12. (★★☆)

Tytuł: Rotacja w lewo/prawo.

Treść: Otrzymujesz listę liczb całkowitych, kierunek przesunięcia (1 odpowiada przesunięciu w prawo, a 0 w lewo) oraz liczbę miejsc, o jaką elementy listy mają zostać przesunięte. Na przykład dla przesunięcia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesuń elementy listy w podanym kierunku.

Dane wejściowe: Lista liczb całkowitych oraz dwie liczby naturalne.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostać zwrócona lista: [6, 2, 1, 10, 8, 5, 27].

### Zad 13. (★★☆)

Tytuł: Znalezienie brakującego elementu w liście.

Treść: Dla dostarczonej listy, składającej się z nieuporządkowanych kolejnych (oprócz jednego) elementów ciągu arytmetycznego, znajdź brakujący element.

Dane wejściowe: Lista zawierająca liczby naturalne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [5, 2, 1, 3] zostanie zwrócona liczba: 4.

### Zad 14. (★★☆)

Tytuł: Znalezienie elementu bez pary w liście liczb całkowitych.

Treść: Dla otrzymanej listy liczb całkowitych, składającej się z nieparzystej liczby elementów, znajdź element, który nie ma pary o tej samej wartości.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [1, 3, 1, 7, 3, 1, 1] zostanie zwrócona liczba: 7.

### Zad 15. (★★☆)

Tytuł: Znalezienie elementu dominującego w liście liczb naturalnych.

Treść: Dla dostarczonej listy liczb naturalnych, znajdź element, który występuje w niej więcej niż połowa jej długości. Jeśli taki element nie istnieje, zwróć -1.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrócona liczba: 4.

### Zad 16. (★★☆)

Tytuł: Znalezienie indeksów pierwszej pary elementów listy o sumie równej podanej liczbie.

Treść: Dla otrzymanej listy liczb całkowitych oraz liczby x, znajdź indeksy pierwszej pary elementów listy, których suma jest równa x. Jeśli taka para nie istnieje, zwróć parę (-1, -1).

Dane wejściowe: Lista liczb całkowitych oraz liczba całkowita.

Dane wyjściowe: Para liczb całkowitych.

Przykład:

Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostaną zwrócone indeksy pierwszej pary elementów o sumie równej 5: (0, 2).

### Zad 17. (★★☆)

Tytuł: Znalezienie wszystkich par elementów listy o sumie równej podanej liczbie.

Treść: Dla otrzymanej listy liczb całkowitych oraz liczby x, znajdź wszystkie pary elementów listy, których suma jest równa x.

Dane wejściowe: Lista liczb całkowitych oraz liczba całkowita.

Dane wyjściowe: Lista par liczb całkowitych.

Przykład:

Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5, zostaną zwrócone wszystkie pary elementów o sumie równej 5: [(1, 4), (2, 3)].

### Zad 18. (★★☆)

Tytuł: Znalezienie indeksu najmniejszego elementu w posortowanej i przesuniętej w prawo liście.

Treść: Dla otrzymanej listy liczb całkowitych, znajdź indeks najmniejszego elementu. Lista jest posortowana rosnąco, ale została przesunięta w prawo o określoną liczbę miejsc. Przykładowo dla przesunięcia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.

Dane wejściowe: Lista liczb całkowitych oraz liczba naturalna określająca przesunięcie w prawo.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrócona liczba: 2.

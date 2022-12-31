## Sortowanie — Algorytmy

### Zad 1.  (★☆☆)

Tytuł: Sortowanie bąbelkowe.

Treść: Dla otrzymanej listy liczb całkowitych zaimplementuj sortowanie bąbelkowe:
Dokonuj kolejno porównania dla sąsiadujących liczb z listy.
Zamień miejscami porównywane liczby, jeśli pierwsza jest większa od drugiej.
Operację powtarzaj, aż po przejściu przez całą listę nie wykonasz żadnej zamiany.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład: 

Dla otrzymanej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 2.  (★★☆)

Tytuł: Sortowanie przez wybieranie.

Treść: Dla otrzymanej listy liczb całkowitych zaimplementuj sortowanie przez wybieranie:
Znajdź największy element w liście i zapisz go zmiennej maks.
Zainicjalizuj zmienną i liczbą 0.
Znajdź indeks najmniejszego elementu listy spośród elementów o indeksach od i do końca listy.
Zamień miejscami element o indeksie i, ze znalezionym najmniejszym elementem.
Zwiększ i o 1.
Powtarzaj operacje z punktów 2-4, aż znaleziony najmniejszy element będzie równy zmiennej maks.

Przykład: 

Dla otrzymanej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 3.  (★★☆)
 
Tytuł: Sortowanie przez wstawianie.

Treść: Dla otrzymanej listy liczb całkowitych zaimplementuj sortowanie przez wstawianie:
Stwórz nową listę i zainicjalizuj ją dowolnym elementem z listy sortowanej.
Dostawiaj kolejno elementy sortowanej listy do nowej listy. Przy czym porównuj dostawiany element kolejno z elementami nowej listy, aż znajdziesz liczbę równą, bądź większą od dostawianej liczby. 
Wstaw liczbę na miejsce poprzedzające elementy równy, bądź większy od dostawianej liczby. 
W przypadku dotarcia na koniec posortowanej listy, dostaw liczbę na koniec listy.
Powtarzaj operacje z punktów 2-4, aż przejdziesz przez wszystkie elementy sortowanej listy.

Dane wejściowe: Lista.

Dane wyjściowe: Lista.

Przykład: 

Dla otrzymanej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 4.  (★★☆)

Tytuł: Sortowanie przez scalanie.

Treść: Dla otrzymanej listy liczb całkowitych zaimplementuj sortowanie przez scalanie:
Podziel listę na n jednoelementowych list, gdzie n to długość sortowanej listy.
Łącz kolejno dwie sąsiednie listy w jedną listę składającą się z elementów obu list.
Przy łączeniu list ustawiaj w wynikowej liście elementy łączonych list w porządku rosnącym.
Powtarzaj operacje z punktów 2-3, aż otrzymasz pojedynczą listę.

Dane wejściowe: Lista.

Dane wyjściowe: Lista.

Przykład: 

Dla otrzymanej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 5.  (★★☆)

Tytuł: Sortowanie szybkie.

Treść: Dla otrzymanej listy liczb całkowitych zaimplementuj sortowanie szybkie:
Wybierz jeden element listy. Wybrany element jest elementem rozdzielającym.
Podziel listę na dwie części. Do pierwszej przenieś wszystkie elementy mniejsze od elementu rozdzielającego, a do drugiej wszystkie pozostałe.
Dla każdej z otrzymanych list powtórz operacje z punktów 1-2.
Powtarzaj operacje 1-3, aż otrzymasz  n jednoelementowych list, gdzie n to długość pierwotnej listy.
Połącz wszystkie jednoelementowe listy w jedną posortowaną listę.

Dane wejściowe: Lista.

Dane wyjściowe: Lista.

Przykład: 

Dla otrzymanej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

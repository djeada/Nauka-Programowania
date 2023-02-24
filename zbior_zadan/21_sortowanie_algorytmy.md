## Sortowanie — Algorytmy

### Zad 1.  (★☆☆)

Tytuł: Sortowanie bąbelkowe.

Treść: Napisz program sortujący listę liczb całkowitych metodą sortowania bąbelkowego. Porównaj sąsiednie liczby z listy i zamień je miejscami, jeśli pierwsza jest większa od drugiej. Powtarzaj operację, aż przejdziesz przez całą listę bez dokonywania zmian.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 2.  (★★☆)

Tytuł: Sortowanie przez wybieranie.

Treść: Napisz program sortujący listę liczb całkowitych metodą sortowania przez wybieranie. Znajdź największy element w liście i zapisz go do zmiennej. Następnie znajdź najmniejszy element w pozostałej części listy i zamień go z pierwszym elementem nieposortowanej części. Powtarzaj operację, aż lista będzie posortowana.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 3.  (★★☆)
 
Tytuł: Sortowanie przez wstawianie.

Treść: Napisz program sortujący listę liczb całkowitych metodą sortowania przez wstawianie. Stwórz nową, pustą listę i dodaj do niej pierwszy element listy wejściowej. Dla każdego kolejnego elementu znajdź odpowiednie miejsce w posortowanej już części listy i wstaw go tam.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 4.  (★★☆)

Tytuł: Sortowanie przez scalanie.

Treść: Dla danej listy liczb całkowitych zaimplementuj algorytm sortowania przez scalanie.

1. Jeśli długość listy jest mniejsza niż 2, zwróć listę.
2. Podziel listę na dwie równe (lub prawie równe) części.
3. Wywołaj rekurencyjnie sortowanie przez scalanie dla obu części listy.
4. Scal obie posortowane części listy w jedną posortowaną listę.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla danej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

### Zad 5.  (★★☆)

Tytuł: Sortowanie szybkie.

Treść: Dla danej listy liczb całkowitych zaimplementuj algorytm sortowania szybkiego.

1. Jeśli długość listy jest mniejsza niż 2, zwróć listę.
2. Wybierz element rozdzielający, nazywany pivotem.
3. Podziel listę na trzy części: elementy mniejsze od pivota, pivot oraz elementy większe od pivota.
4. Wywołaj rekurencyjnie sortowanie szybkie dla części z elementami mniejszymi od pivota i większymi od pivota.
5. Scal posortowane części listy w jedną posortowaną listę.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla danej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

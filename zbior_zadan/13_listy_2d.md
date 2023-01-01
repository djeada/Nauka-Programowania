## Listy 2D

### Zad 1. (★☆☆)

Tytuł: Macierz z identycznymi wierszami, składającymi się z liczb od 0 do b.

Treść: Otrzymujesz dwie liczby naturalne, a i b. Stwórz macierz, składającą się z a identycznych wierszy, które składają się z liczb od 0 do b.

Dane wejściowe: Dwie liczby naturalne, a i b.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanych liczb: 3 i 2, powinna zostać zwrócona macierz: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

### Zad 2. (★☆☆)

Tytuł: Macierz kwadratowa, z elementami będącymi iloczynem współrzędnych.

Treść: Dla otrzymanej liczby naturalnej n, stwórz macierz kwadratową o rozmiarze n x n, której każdy element jest iloczynem jego współrzędnych.

Dane wejściowe: Liczba naturalna n.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej liczby 3 powinna zostać zwrócona macierz: [[0, 0, 0], [0, 1, 2], [0, 2, 4]].

### Zad 3. (★☆☆)

Tytuł: Macierz z parami elementów odpowiadających sobie z dwóch list.

Treść: Dla otrzymanych dwóch list, stwórz dwukolumnową macierz, której pierwsza kolumna składa się z elementów pierwszej listy, a druga kolumna z elementów drugiej listy. Jeśli otrzymane listy nie są równej długości, zwróć pustą macierz.

Dane wejściowe: Dwie listy.

Dane wyjściowe: Lista list liczb naturalnych lub pusta macierz (w przypadku nierównych długości list).

Przykład:

Dla otrzymanych dwóch list: [3, 5, 2] oraz [2, 8, 1], powinna zostać zwrócona macierz: [[3, 2], [5, 8], [2, 1]

### Zad 4. (★☆☆)

Tytuł: Dodawanie i odejmowanie macierzy.

Treść: Otrzymujesz dwie macierze o tych samych wymiarach. Zwróć dwie macierze będące:

a) wynikiem dodawania otrzymanych macierzy

b) wynikiem odejmowania drugiej macierzy od pierwszej.

Dane wejściowe: Dwie listy list liczb naturalnych.

Dane wyjściowe: Dwie listy list liczb naturalnych.

Przykład:

Dla otrzymanych dwóch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinny zostać zwrócone następujące macierze:

a) [[6, -1], [-1, 7]] - wynik dodawania

b) [[-4, 5], [-3, -7]] - wynik odejmowania drugiej macierzy od pierwszej.

### Zad 5. (★★☆)

Tytuł: Sprawdzanie czy macierz jest "magiczna".

Treść: Otrzymujesz macierz kwadratową. Sprawdź, czy jest ona kwadratem magicznym.

Podpowiedź: Kwadrat magiczny składa się z powtarzających się dodatnich liczb naturalnych. Suma elementów w każdym wierszu, w każdej kolumnie oraz na każdej przekątnej jest taka sama.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanej macierzy: [[6, 7, 2], [1, 5, 9], [8, 3, 4]], powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 6. (★★☆)

Tytuł: Scalanie przedziałów w liście przedziałów.

Treść: Otrzymujesz listę par liczb. Każda para reprezentuje początek i koniec przedziału. Niektóre przedziały mogą się nachodzić. W takim przypadku połącz je ze sobą i zwróć listę przedziałów, które się nie pokrywają.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej listy: [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11, 12], [42, 45]], powinna zostać zwrócona lista: [[10, 22], [23, 88]].

### Zad 7. (★★☆)

Tytuł: Zerowanie macierzy.

Treść: Otrzymujesz listę list liczb naturalnych reprezentującą macierz. Jeśli element macierzy jest równy zero, zamień wszystkie elementy tej samej kolumny i wiersza na zera.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostać zwrócona macierz: [[1,0,3], [0,0,0], [7,0,9]].

### Zad 8. (★★☆)

Tytuł: Wypisanie elementów macierzy spiralnie.

Treść: Otrzymujesz listę list liczb naturalnych. Zbierz elementy otrzymanej macierzy spiralnie i zapisz je w liście.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostać zwrócona lista: [1, 2, 3, 6, 9, 8, 7, 4, 5].

### Zad 9. (★★☆)

Tytuł: Klepsydra o największej sumie.

Treść: Otrzymasz listę list liczb naturalnych. Znajdź w macierzy klepsydrę o największej sumie. Klepsydra składa się dokładnie z 7 elementów. Pierwsze trzy elementy są kolejnymi elementami dowolnego wiersza macierzy. Czwarty element znajduje się w tej samej kolumnie co drugi element i o jeden wiersz niżej. Ostatnie trzy elementy znajdują się w tych samych kolumnach co trzy pierwsze i o dwa wiersze niżej.

Podpowiedź: Następująca macierz:

      1 2 3
      4 5 6
      7 8 9

ma tylko jedną klepsydrę:

      1 2 3
        5
      7 8 9

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej macierzy: [[7, 4, 2, 0], [4, 8, 10, 8], [3, 6, 7, 6], [3, 9, 19, 14]], powinna zostać zwrócona liczba: 75.

### Zad 10. (★★☆)

Tytuł: Obróć macierz o 90 stopni.

Treść: Otrzymujesz macierz składającą się z liczb naturalnych. Obróć ją o 90 stopni. Tzn. zamień miejscami ostatnią kolumnę z ostatnim wierszem, przedostatnią kolumnę z przedostatnim wierszem itd.

Dane wejściowe: Macierz składająca się z liczb naturalnych.

Dane wyjściowe: Macierz składająca się z liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostać zwrócona macierz: [[7,4,1], [8,5,2], [9,6,3]].

### Zad 11. (★★★)

Tytuł: Gra w statki

Treść: Napisz program implementujący grę w statki.

Stwórz macierz o wymiarach 10x10. Wylosuj położenia statków i zapisz je w macierzy. Do dyspozycji masz następujące statki:

* 1 statek o długości 4
* 2 statki o długości 3
* 3 statki o długości 2
* 5 statków o długości 1

Każde pole może zawierać tylko jeden statek.

Wypisz na standardowe wyjście planszę złożoną z 10x10 kropek i poproś użytkownika o podanie współrzędnych. Jeśli na podanych przez użytkownika współrzędnych znajduje się statek, zamień kropkę na literę o na planszy. W przeciwnym razie, zamień kropkę na literę x.

Powtarzaj krok 2, aż wszystkie pozycje statków zostaną odkryte przez użytkownika lub aż na planszy pojawi się 10 liter x. W obu przypadkach zakończ grę i poinformuj użytkownika o wyniku.

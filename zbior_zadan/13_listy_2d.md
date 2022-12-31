## Listy 2D

### Zad 1. (★☆☆)

Tytuł: Macierz a identycznych wierszy składających się z liczb od 0 do b.

Treść: Otrzymujesz dwie liczby, a oraz b. Stwórz macierz a identycznych wierszy składających się z liczb od 0 do b.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanych liczb: 3 i 2, powinna zostać zwrócona macierz: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

### Zad 2. (★☆☆)

Tytuł: Każdy element jest iloczynem współrzędnych.

Treść: Dla otrzymanej liczby, stwórz macierz kwadratową składającą się z liczby kolumn i wierszy równej otrzymanej liczbie, której każdy element jest iloczynem jego współrzędnych.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej liczby 3 powinna zostać zwrócona macierz: [[0, 0, 0], [0, 1, 2], [0, 2, 4]].

### Zad 3. (★☆☆)

Tytuł: Macierz z par odpowiadających sobie elementów dwóch list.

Treść: Dla otrzymanych dwóch list, stwórz dwukolumnową macierz, której pierwsza kolumna składa się z elementów pierwszej listy, a druga kolumna elementów drugiej listy. Jeśli otrzymane listy nie są równej długości, zwróć pustą macierz.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Lista list liczb naturalnych. 

Przykład:

Dla otrzymanych dwóch list: [3, 5, 2] oraz [2, 8, 1], powinna zostać zwrócona macierz: [[3, 2], [5, 8], [2, 1]].

### Zad 4. (★☆☆)

Tytuł: Dodawanie/odejmowanie macierzy.

Treść: Otrzymujesz dwie macierze o tych samych wymiarach, zwróć macierz będącą:

Wynikiem dodawania otrzymanych macierzy.
Wynikiem odejmowania pierwszej macierzy od drugiej.

Dane wejściowe: Dwie listy list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanych dwóch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinna zostać zwrócona macierz: [[6, -1], [-1, 7]].
Dla otrzymanych dwóch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinna zostać zwrócona macierz: [[-4, 5], [-3, -7]].

### Zad 5. (★★☆)

Tytuł: Magiczny kwadrat.

Treść: Otrzymujesz macierz kwadratową. Sprawdź, czy macierz jest kwadratem magicznym. 

Podpowiedź: Kwadrat magiczny składa się z powtarzających się dodatnich liczb naturalnych. Suma elementów w każdym wierszu, w każdej kolumnie oraz na każdej przekątnej jest taka sama.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanej macierzy: [[6, 7, 2], [1, 5, 9], [8, 3, 4]], powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 6. (★★☆)

Tytuł: Pokrywające się przedziały w liście przedziałów.

Treść: Otrzymujesz listę par liczb. Liczby w parze reprezentują początek i koniec przedziału. Niektóre przedziały mogą na siebie nachodzić. W takim przypadku połącz je ze sobą i zwróć listę niepokrywających się przedziałów.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11, 12], [42, 45]], powinna zostać zwrócona macierz: [[10, 22], [23, 88]].

### Zad 7. (★★☆)

Tytuł: Wyzeruj macierz.

Treść: Otrzymujesz listę list liczb naturalnych reprezentującą macierz. Jeśli element macierzy jest równy zero, zamień wszystkie elementy w tej samej kolumnie i tym samym wierszu na zera.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostać zwrócona macierz: [[1,0,3], [0,0,0], [7,0,9]].

### Zad 8. (★★☆)

Tytuł: Wypisz spiralnie.

Treść: Otrzymujesz listę list liczb naturalnych. Zbierz spiralnie elementy otrzymanej macierzy i zapisz je w liście.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostać zwrócona lista: [1, 2, 3, 6, 9, 8, 7, 4, 5].

### Zad 9. (★★☆)

Tytuł: Klepsydra o największej sumie.

Treść: Otrzymujesz listę list liczb naturalnych. Znajdź w macierzy klepsydrę o największej sumie. Klepsydra składa się z dokładnie 7 elementów. Trzy pierwsze elementy są kolejnymi elementami dowolnego wiersza macierzy. Następny element znajduje się w tej samej kolumnie co drugi element i w dokładnie jednym wierszu niżej. Trzy następne znajdują się w tych samych kolumnach co trzy pierwsze i dokładnie dwa wiersze niżej.

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

Dla otrzymanej macierzy: [[ 7 4 2 0], [ 4 8 10 8], [ 3 6 7 6], [ 3 9 19 14]], powinna zostać zwrócona liczba: 75.

### Zad 10. (★★☆)

Tytuł: Obróć o 90 stopni.

Treść: Otrzymujesz listę list liczb naturalnych. Obróć otrzymaną listę o 90 stopni. Tzn. zamień miejscami ostatnią kolumnę z ostatnim wierszem, przedostatnią kolumnę z przedostatnim wierszem itd.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostać zwrócona macierz: [[7,4,1], [8,5,2], [9,6,3]].

### Zad 11. (★★★)

Tytuł: Gra w statki.

Treść: Napisz program, realizujący grę w statki. 

Stwórz macierz składającą się z 10 wierszy i 10 kolumn. Wylosuj położenia statków i zapisz je w macierzy. Masz do dyspozycji następujące statki: 
1 statek o długości równej 4 polom, 
2 statki o długości równej 3 polom, 
3 statki o długości równej 2 polom, 
5 statków o długości równej 1 polu. 
Na danym polu może znajdować się tylko jeden statek.

Wypisz na standardowe wyjście planszę składającą się z 10x10 kropek i poproś użytkownika o podanie współrzędnych. Jeśli na podanych przez użytkownika znajduje się statek, zamień na planszy kropkę na literę o. W przeciwnym razie, zamień kropkę na literę x.

Powtarzaj krok 2, dopóki wszystkie pozycje statków nie zostaną odkryte przez użytkownika lub dopóki na planszy nie znajdzie się 10 literek x. W obu przypadkach zakończ grę i poinformuj użytkownika o wyniku.

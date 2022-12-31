## Listy — trudne

### Zad 1.  (★★☆)

Tytuł: Najdłuższy nieprzerwany ciąg jedynek.

Treść: Otrzymujesz listę składającą się wyłącznie z zer i jedynek. Znajdź indeks zera, które po zamianie na jedynkę dałoby najdłuższy nieprzerwany ciąg jedynek. Jeśli lista składa się wyłącznie z zer lub wyłącznie z jedynek, zwróć -1.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy:  [0, 0, 1, 0, 1, 1, 1, 0, 1, 1], powinna zostać zwrócona liczba: 7.

### Zad 2. (★★☆)

Tytuł: Przesuń zera. 

Treść: Otrzymujesz listę liczb całkowitych. Przesuń wszystkie zera na koniec listy.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0], powinna zostać zwrócona lista: [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]. 

### Zad 3.  (★★☆)

Tytuł: Trójka o minimalnym iloczynie.	

Treść: Otrzymujesz listę liczb całkowitych. Znajdź najmniejszy iloczyn dla trzech liczb wybranych z listy. Jeśli liczba składa się z mniej niż trzech liczb, zwróć iloczyn wszystkich elementów listy.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [3, -1, -3, 2, 9, 4], powinna zostać zwrócona liczba: -108.

### Zad 4.  (★★★)

Tytuł: Wspólny podciąg o największej sumie.	

Treść: Otrzymujesz dwie listy binarne, A oraz B. Znajdź największą długość takich dwóch podciągów, które dla obu list zaczynają się i kończą na tej samej pozycji i których suma elementów jest jednakowa.

Dane wejściowe: Dwie listy binarne.

Dane wyjściowe: Liczba naturalna.

Przykład

Dla otrzymanych list: [0, 0, 1, 1, 1, 1] i [0, 1, 1, 0, 1, 0], powinna zostać zwrócona liczba: 5.

Wyjaśnienia: Suma elementów obu list na pozycjach od 0 do 4 jest równa 3.

### Zad 5.

Tytuł: Zbiór potęgowy.	 (★★★)

Treść: Otrzymujesz listę liczb naturalnych. Zwróć zbiór potęgowy otrzymanej listy, czyli zbiór wszystkich jej podzbiorów.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej listy: [1, 2, 1], powinna zostać zwrócona lista: [(), (1,), (2,), (1, 2), (1, 1), (1, 1, 2)].

### Zad 6. (★★★)

Tytuł: M posortowanych list.

Treść: Otrzymujesz listę 2D składającą się z M posortowanych list. Połącz otrzymane listy w jedną posortowaną listę. Wszystkie elementy są unikalne.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista liczb naturalnych.

Przykład:

Dla otrzymanej listy:
[[ -6, 23, 29, 33],
	[ 6, 22, 35, 71 ],
	[ 5, 19, 21, 37 ],
	[ -12, -7, -3, 28 ]], 

powinna zostać zwrócona lista: [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71].

### Zad 7. (★★★)

Tytuł: Woda.

Treść: Otrzymujesz listę wysokości słupków. Wszystkie słupki mają jednakową szerokość, równą jednej jednostce wysokości i ustawione są jeden obok drugiego. Wysokość równa 0, oznacza brak słupka. Oblicz ile jednostek wody możemy maksymalnie umieścić między słupkami.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy:  [3, 0, 1, 0, 2], powinna zostać zwrócona liczba: 5.

o                               o
o      o          =>         o x x x o
o_o_o                       o x o x o

### Zad 8.  (★★★)

Tytuł: Sznurek. 

Treść: Otrzymujesz listę liczb naturalnych oraz liczbę n. Lista reprezentuje ceny sznurka o długości równej indeksowi powiększonemu o 1. Zależność między cenami i długością sznurka jest przypadkowa. Przykładowo sznurek o długości równej 2 jednostkom może kosztować tyle samo co sznurek o długości równej 3 jednostkom i być pięć razy droższy niż sznurek o długości 1 jednostce. Liczba n to długość sznurka, jaki mamy sprzedać. Oblicz ile maksymalnie można zarobić na sprzedaży sznurka o danej długości.

Dane wejściowe: Lista liczb i liczba.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [1, 5, 8, 9, 10, 17, 17, 20] oraz 4, powinna zostać zwrócona liczba: 10.

### Zad 9. (★★★)

Tytuł: Najdłuższy naprzemienny podciąg.  (★★★)

Treść: Otrzymujesz listę liczb. Znajdź najdłuższy naprzemienny podciąg w liście.

Podpowiedź: 

Ciąg {a1, a2, .. an} jest ciągiem naprzemiennym, jeśli prawdziwe jest:
x1 < x2 > x3 < x4 > x5 < …. xn lub 
x1 > x2 < x3 > x4 < x5 > …. xn

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista liczb naturalnych.

Przykład:

Dla otrzymanej listy: [1, -2, 6, 4, -3, 2, -4, -3], powinna zostać zwrócona lista: [4, -3, 2, -4].

## Listy — trudne

### Zad 1.  (★★☆)

Tytuł: Najdłuższy ciąg jedynek.

Treść: Otrzymujesz listę składającą się wyłącznie z zer i jedynek. Znajdź indeks zera, które po zamianie na jedynkę dałoby najdłuższy ciąg jedynek. Jeśli lista składa się wyłącznie z zer lub wyłącznie z jedynek, zwróć -1.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1], powinna zostać zwrócona liczba: 7.

### Zad 2. (★★☆)

Tytuł: Przesuń zera.

Treść: Otrzymujesz listę liczb całkowitych. Przesuń wszystkie zera na koniec listy.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0], powinna zostać zwrócona lista: [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0].

### Zad 3.  (★★☆)

Tytuł: Minimalny iloczyn.

Treść: Otrzymujesz listę liczb całkowitych. Znajdź najmniejszy iloczyn dla trzech liczb wybranych z listy. Jeśli lista składa się z mniej niż trzech liczb, zwróć iloczyn wszystkich elementów listy.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [3, -1, -3, 2, 9, 4], powinna zostać zwrócona liczba: -108.

### Zad 4.  (★★★)

Tytuł: Wspólny podciąg o największej sumie.

Treść: Otrzymujesz dwie listy binarne, A oraz B. Znajdź największą długość takich dwóch podciągów, które dla obu list zaczynają się i kończą na tej samej pozycji i których suma elementów jest jednakowa.

Dane wejściowe: Dwie listy binarne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych list: [0, 0, 1, 1, 1, 1] i [0, 1, 1, 0, 1, 0], powinna zostać zwrócona liczba: 5.

Wyjaśnienia: Suma elementów obu list na pozycjach od 0 do 4 jest równa 3.

### Zad 5. (★★★)

Tytuł: Zbiór potęgowy 

Treść: Otrzymujesz listę liczb naturalnych. Zwróć zbiór potęgowy otrzymanej listy, czyli zbiór wszystkich jej podzbiorów.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista list zawierająca elementy z wejściowej listy lub pustą listę.

Przykład:

Dla wejściowej listy [1, 2, 1], powinna zostać zwrócona lista: [[], [1], [2], [1, 2], [1, 1], [1, 2, 1]].

### Zad 6. (★★★)

Tytuł: Połączone posortowane listy 

Treść: Otrzymujesz listę zawierającą M posortowanych list. Połącz te listy w jedną posortowaną listę. Wszystkie elementy są unikalne.

Dane wejściowe: Lista list zawierających liczby naturalne.

Dane wyjściowe: Lista zawierająca liczby naturalne.

Przykład:

Dla wejściowej listy:
[[ -6, 23, 29, 33],
[ 6, 22, 35, 71 ],
[ 5, 19, 21, 37 ],
[ -12, -7, -3, 28 ]],

powinna zostać zwrócona lista: [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71].

### Zad 7. (★★★)

Tytuł: Woda

Treść: Otrzymujesz listę wysokości słupków. Wszystkie słupki mają jednakową szerokość, równą jednej jednostce wysokości, i ustawione są obok siebie. Wysokość równa 0 oznacza brak słupka. Oblicz ile jednostek wody maksymalnie możemy umieścić między słupkami.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla wejściowej listy [3, 0, 1, 0, 2], powinna zostać zwrócona liczba: 5.

Oto ilustracja dla powyższego przykładu:

```
   o           
   o      o    
o  o   o  o  o 
```

Możemy umieścić 5 jednostek wody pomiędzy słupkami.

### Zad 8.  (★★★)

Tytuł: Sznurek.

Treść: Masz do sprzedania sznurek o długości n, a także listę cen dla sznurków o długościach od 1 do n. Ceny mogą być różne dla różnych długości. Znajdź maksymalny zysk, który można osiągnąć poprzez sprzedaż danego sznurka.

Dane wejściowe: Lista n liczb całkowitych reprezentujących ceny dla sznurków o długościach od 1 do n, oraz liczba naturalna n reprezentująca długość sznurka, który chcesz sprzedać.

Dane wyjściowe: Największa możliwa wartość, jaką można uzyskać ze sprzedaży danego sznurka.

Przykład:

Dla listy cen: [1, 5, 8, 9, 10, 17, 17, 20] oraz długości sznurka 4, powinna zostać zwrócona liczba 10.

### Zad 9. (★★★)

Tytuł: Najdłuższy naprzemienny podciąg.

Treść: Masz daną listę liczb. Znajdź najdłuższy podciąg naprzemienny w tej liście. Ciąg jest naprzemienny, jeśli liczby w nim rosną i maleją na zmianę. Na przykład [1, 3, 2, 4, 3, 5] jest naprzemienny.

Dane wejściowe: Lista n liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych reprezentująca najdłuższy podciąg naprzemienny w tej liście.

Przykład:

Dla listy liczb: [1, -2, 6, 4, -3, 2, -4, -3], powinna zostać zwrócona lista [1, -2, 6, -3, 2, -4].

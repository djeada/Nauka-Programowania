## Klasy

### Zad 1. (★★☆)

Tytuł: Zaprojektuj klasę Koło.

Opis zadania: Napisz klasę Koło, która będzie reprezentowała koło. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje jedną liczbę jako argument, reprezentującą promień koła. Domyślną wartością promienia powinno być 1.
2. Funkcję obwód, która zwraca obwód koła.
3. Funkcję pole, która zwraca pole koła.
4. Funkcję, która wypisuje informacje o kole na standardowe wyjście.

Napisz program, który przetestuje twoją klasę. Stwórz koło o promieniu 3 i użyj funkcji wypisującej informacje o kole.

### Zad 2. (★★☆)

Tytuł: Zaprojektuj klasę Punkt.

Treść: Napisz klasę Punkt, która będzie reprezentowała punkt w układzie kartezjańskim. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje dwa argumenty (liczby). Pierwsza liczba reprezentuje współrzędną x, a druga współrzędną y. Domyślne wartości dla obu argumentów powinny wynosić 0.
2. Funkcję statyczną odległość, która zwraca odległość między dwoma punktami (obiektami klasy Punkt).
3. Funkcję, która wypisuje informacje o punkcie na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Punkt. Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.

Napisz program, który przetestuje twoją klasę. Stwórz punkty: A (5, 5) oraz B (-3, -3). Wypisz na standardowe wyjście informacje o utworzonych punktach oraz odległość między nimi.

### Zad 3. (★★☆)

Tytuł: Prostokąt powstały z nałożenia się dwóch prostokątów.

Opis zadania: Napisz klasę Prostokąt, która będzie reprezentowała prostokąt w układzie kartezjańskim. Prostokąt jest określony przez współrzędne jego czterech wierzchołków. Boki prostokąta są prostopadłe do osi układu współrzędnych. Klasa powinna zawierać funkcję statyczną, która zwraca pole prostokąta powstałego z nałożenia się dwóch prostokątów. Jeśli dwa prostokąty nie pokrywają się, funkcja powinna zwracać 0.

Napisz program, który przetestuje twoją klasę. Stwórz prostokąty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjście informacje o utworzonych prostokątach. Sprawdź, czy pole części wspólnej równe jest 6.

### Zad 4.  (★★☆)

Tytuł: Zaprojektuj klasy Wektor2D oraz Wektor3D.

Treść:  Napisz klasy Wektor2D oraz Wektor3D, które będą reprezentowały odpowiednio wektory w przestrzeni dwuwymiarowej i trzywymiarowej. Klasy powinny zawierać następujące funkcje:

1. Konstruktor, który przyjmuje dwa (trzy) argumenty (liczby). Liczby reprezentują współrzędne wektora. Domyślne wartości dla wszystkich argumentów powinny wynosić 0.
2. Funkcje, które zwracają wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie) oraz iloczyn wektorowy i skalarny. Jeśli jest to możliwe, należy przeciążyć operatory: +, -, *.
3. Funkcję, która wypisuje informacje o wektorze na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Wektor2D (Wektor3D). Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.
5. Funkcję moduł, która zwraca moduł wektora.

Napisz program, który przetestuje twoją klasę. Stwórz wektory: A (-3, -3, -3) oraz B (5, 5, 5). Wypisz na standardowe wyjście informacje o utworzonych wektorach oraz sumę wektorów, różnicę pierwszego i drugiego oraz ich iloczyn wektorowy.

### Zad 5.  (★★☆)

Tytuł: Zaprojektuj klasę Macierz.

Treść: Napisz klasę Macierz, która będzie reprezentowała macierz. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje jako argument listę list liczb całkowitych. Pobrana lista reprezentuje macierz. Domyślna wartość argumentu to pusta lista.
2. Funkcje, które zwracają wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnożenie) oraz odwracanie macierzy. Jeśli jest to możliwe, należy przeciążyć operatory: +, -, *.
3. Funkcję, która wypisuje informacje o macierzy na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Macierz. Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.

Napisz program, który przetestuje twoją klasę. Stwórz macierze: A ([[1, 3], [4, 2]]) oraz B ([[5, 0], [1, 3]]). Wypisz na standardowe wyjście informacje o utworzonych macierzach oraz ich sumę, różnicę pierwszej i drugiej oraz iloczyn macierzy.

### Zad 6. (★★☆)

Tytuł: Zaprojektuj klasę Zespolona.

Treść: Napisz klasę Zespolona, która będzie reprezentowała liczbę zespoloną. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje jako argument dwie liczby. Pierwsza liczba reprezentuje część rzeczywistą, a druga część urojoną liczby zespolonej. Domyślne wartości dla obu argumentów to 0.
2. Funkcje, które zwracają wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnożenie, dzielenie). Jeśli jest to możliwe, należy przeciążyć operatory: +, -, *, /.
3. Funkcję, która wypisuje informacje o liczbie zespolonej na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Zespolona. Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.
5. Funkcję moduł, która zwraca moduł liczby zespolonej.

Napisz program, który przetestuje twoją klasę. Stwórz liczby zespolone: A (9, 12) oraz B (-3, -3). Wypisz na standardowe wyjście informacje o utworzonych liczbach zespolonych oraz ich sumę, różnicę pierwszej i drugiej, iloraz pierwszej przez drugą oraz iloczyn liczb zespolonych.

### Zad 7.  (★☆☆)

Tytuł: Zlicz instancje klasy w programie.

Treść: Opis zadania: Stwórz klasę Klasa, która będzie zawierała funkcję statyczną, zwracającą aktualną liczbę instancji tej klasy w programie. Następnie stwórz kilka obiektów tej klasy i przetestuj działanie funkcji.

Dane wejściowe: brak

Dane wyjściowe: liczba naturalna, reprezentująca liczbę instancji klasy w programie.

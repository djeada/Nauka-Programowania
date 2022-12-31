## Klasy

### Zad 1. (★★☆)

Tytuł: Zaprojektuj klasę Koło.

Treść: Napisz klasę Koło reprezentującą koło. W skład klasy powinny wchodzić funkcje:
Konstruktor pobierający jedną liczbę jako argument, reprezentującą promień koła. Domyślna wartość promienia to 1.
Funkcja obwód, zwracająca obwód koła.
Funkcja pole, zwracająca pole koła.
Funkcja wypisująca informacje o kole na standardowe wyjście.

Napisz program testujący twoją klasę. Stwórz koło o promieniu równym 3 i użyj funkcji wypisującej informacje o kole.

### Zad 2. (★★☆)

Tytuł: Zaprojektuj klasę Punkt.

Treść: Napisz klasę Punkt reprezentującą punkt w układzie kartezjańskim. W skład klasy powinny wchodzić funkcje:
Konstruktor pobierający dwie liczby jako argumenty. Pierwsza liczba reprezentuje współrzędną x, a druga współrzędną y. Domyślne wartości dla obu argumentów wynoszą 0.
Funkcja statyczna odległość, zwracająca odległość między dwoma punktami (obiektami klasy Punkt).
Funkcja wypisująca informacje o punkcie na standardowe wyjście.
Funkcje umożliwiające porównanie dwóch obiektów klasy Punkt. Jeśli jest to możliwe, należy przeciążyć operatory ==, !=.

Napisz program testujący twoją klasę. Stwórz punkty: A (5, 5) oraz B (-3, -3). Wypisz na standardowe wyjście informacje o utworzonych punktach oraz odległość między nimi.

### Zad 3. (★★☆)

Tytuł: Prostokąt powstały z nałożenia się dwóch prostokątów.

Treść: Napisz klasę Prostokąt reprezentującą prostokąt w układzie kartezjańskim. Prostokąt określony jest przez współrzędne jego czterech wierzchołków. Boki prostokąta są prostopadłe do osi układu współrzędnych. Klasa powinna zawierać funkcję statyczną zwracającą pole prostokąta powstałego z nałożenia się dwóch prostokątów. Jeśli dwa prostokąty nie pokrywają się, funkcja powinna zwracać 0.

Napisz program testujący twoją klasę. Stwórz prostokąty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjście informacje o utworzonych prostokątach. Sprawdź, czy pole części wspólnej równe jest 6.

### Zad 4.  (★★☆)

Tytuł: Zaprojektuj klasy Wektor2D oraz Wektor3D.

Treść: Napisz klasy Wektor2D oraz Wektor3D reprezentujące odpowiednio wektory w przestrzeni dwuwymiarowej i trzywymiarowej. W skład klas powinny wchodzić funkcje:
Konstruktor pobierający dwie (trzy) liczby jako argumenty. Liczby reprezentują współrzędne wektora. Domyślne wartości dla wszystkich argumentów wynoszą 0.
Funkcje zwracające wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie) oraz iloczyn wektorowy  i skalarny. Jeśli jest to możliwe, należy przeciążyć operatory: ```+, -, *```.
Funkcja wypisująca informacje o wektorze na standardowe wyjście.
Funkcje umożliwiające porównanie dwóch obiektów klasy Wektor2D (Wektor3D). Jeśli jest to możliwe, należy przeciążyć operatory ==, !=.
Funkcja moduł, zwracająca moduł wektora.

Napisz program testujący twoją klasę. Stwórz wektory: A (-3, -3, -3) oraz B (5, 5, 5). Wypisz na standardowe wyjście informacje o utworzonych wektorach oraz sumę wektorów, różnice pierwszego i drugiego oraz ich iloczyn wektorowy.

### Zad 5.  (★★☆)

Tytuł: Zaprojektuj klasę Macierz.

Treść: Napisz klasę Macierz reprezentującą macierz. W skład klasy powinny wchodzić funkcje:
Konstruktor pobierający listę list liczb całkowitych. Pobrana lista reprezentuje macierz. Domyślna wartość argumentu to pusta lista.
Funkcje zwracające wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnożenie) oraz odwracanie macierzy. Jeśli jest to możliwe, należy przeciążyć operatory: ```+, -, *```.
Funkcja wypisująca informacje o macierzy na standardowe wyjście.
Funkcje umożliwiające porównanie dwóch obiektów klasy Macierz. Jeśli jest to możliwe, należy przeciążyć operatory ==, !=.

Napisz program testujący twoją klasę. Stwórz macierze: A ([[1, 3], [4, 2]]) i B ([[5, 0], [1, 3]]). Wypisz na standardowe wyjście informacje o utworzonych macierzach oraz ich sumę, różnicę pierwszej i drugiej oraz iloczyn macierzy. 

### Zad 6. (★★☆)

Tytuł: Zaprojektuj klasę Zespolona.

Treść: Napisz klasę Zespolona reprezentującą liczbę zespoloną. W skład klasy powinny wchodzić funkcje:
Konstruktor pobierający dwie liczby jako argumenty. Pierwsza liczba reprezentuje część rzeczywistą, a druga część urojoną liczby zespolonej. Domyślne wartości dla obu argumentów to 0.
Funkcje zwracające wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnożenie, dzielenie). Jeśli jest to możliwe, należy przeciążyć operatory: ```+, -, *, /```.
Funkcja wypisująca informacje o liczbie zespolonej na standardowe wyjście.
Funkcje umożliwiające porównanie dwóch obiektów klasy Zespolona. Jeśli jest to możliwe, należy przeciążyć operatory ==, !=.
Funkcja moduł, zwracająca moduł liczby zespolonej. 

Napisz program testujący twoją klasę. Stwórz liczby zespolone: A (9, 12) i B (-3, -3). Wypisz na standardowe wyjście informacje o utworzonych liczbach zespolonych oraz ich sumę, różnicę pierwszej i drugiej, iloraz pierwszej przez drugą oraz iloczyn liczb zespolonych.

### Zad 7.  (★☆☆)

Tytuł: Znajdź liczbę instancji klasy w programie.

Treść: Stwórz klasę Klasa. Klasa powinna zawierać funkcję statyczną zwracającą aktualną liczbę instancji klasy w programie. Stwórz kilka obiektów klasy i przetestuj działanie funkcji.

Dane wejściowe: Brak.

Dane wyjściowe: Liczba naturalna.

# Klasy

## Zadanie 1 - Zaprojektuj klasę Koło

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj klasę **Koło**, która będzie reprezentować koło w przestrzeni dwuwymiarowej. Klasa powinna zawierać następujące elementy:

1. **Konstruktor**, który przyjmuje jedną liczbę reprezentującą promień koła. Domyślną wartością promienia powinno być 1.
2. **Metodę** obliczającą **obwód** koła.
3. **Metodę** obliczającą **pole** koła.
4. **Metodę** wyświetlającą informacje o kole, takie jak promień, obwód i pole.

Napisz program, który utworzy obiekt klasy **Koło** o promieniu 3 i wyświetli informacje o tym kole.

### Dane wejściowe

- Liczba rzeczywista — promień koła (opcjonalnie, jeśli korzystasz z wartości domyślnej).

### Dane wyjściowe

- Informacje o kole:
  - Promień koła.
  - Obwód koła.
  - Pole koła.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  Koło o promieniu: 3
  Obwód koła: 18.8496
  Pole koła: 28.2743
  ```

*(Przyjmując, że π ≈ 3.1416)*

### Wskazówki

- Obwód koła można obliczyć ze wzoru:
  \[
  O = 2\pi r
  \]
- Pole koła można obliczyć ze wzoru:
  \[
  P = \pi r^2
  \]
- Upewnij się, że wszystkie wartości są obliczane z odpowiednią dokładnością.

---

## Zadanie 2 - Zaprojektuj klasę Punkt

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj klasę **Punkt**, która będzie reprezentować punkt w układzie kartezjańskim. Klasa powinna zawierać następujące elementy:

1. **Konstruktor**, który przyjmuje dwa argumenty liczbowe:
   - Pierwszy argument — współrzędna \( x \).
   - Drugi argument — współrzędna \( y \).
   - Domyślne wartości obu argumentów powinny wynosić 0.

2. **Metodę statyczną** obliczającą **odległość** między dwoma punktami.

3. **Metodę** wyświetlającą informacje o punkcie, takie jak jego współrzędne.

4. **Metody porównujące** dwa punkty pod względem równości i nierówności.

Napisz program, który:

- Utworzy dwa punkty:
  - Punkt A o współrzędnych (5, 5).
  - Punkt B o współrzędnych (-3, -3).
- Wyświetli informacje o obu punktach.
- Obliczy i wyświetli odległość między punktami A i B.

### Dane wejściowe

- Współrzędne punktów:
  - Punkt A: \( x = 5 \), \( y = 5 \).
  - Punkt B: \( x = -3 \), \( y = -3 \).

### Dane wyjściowe

- Informacje o punktach A i B.
- Odległość między punktami A i B.

### Przykład

- **Dane wejściowe**:
  ```
  Punkt A: x = 5, y = 5
  Punkt B: x = -3, y = -3
  ```
- **Oczekiwane wyjście**:
  ```
  Punkt A: (5, 5)
  Punkt B: (-3, -3)
  Odległość między punktami A i B: 11.3137
  ```

*(Odległość obliczona ze wzoru \( d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \))*

### Wskazówki

- Użyj wzoru na odległość między dwoma punktami w układzie kartezjańskim:
  \[
  d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
  \]
- Przy porównywaniu punktów sprawdź, czy ich współrzędne są identyczne.

---

## Zadanie 3 - Pole nałożenia się dwóch prostokątów

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj klasę **Prostokąt**, która będzie reprezentować prostokąt w układzie kartezjańskim. Prostokąt jest określony przez współrzędne jego przeciwległych wierzchołków. Boki prostokąta są równoległe do osi układu współrzędnych.

Klasa powinna zawierać:

1. **Konstruktor**, który przyjmuje cztery liczby:
   - \( x_{\text{lewy}} \) — współrzędna \( x \) lewego dolnego wierzchołka.
   - \( y_{\text{dolny}} \) — współrzędna \( y \) lewego dolnego wierzchołka.
   - \( x_{\text{prawy}} \) — współrzędna \( x \) prawego górnego wierzchołka.
   - \( y_{\text{górny}} \) — współrzędna \( y \) prawego górnego wierzchołka.

2. **Metodę statyczną** obliczającą **pole nałożenia się** dwóch prostokątów. Metoda powinna zwrócić pole prostokąta będącego częścią wspólną dwóch prostokątów. Jeśli prostokąty nie nachodzą na siebie, metoda powinna zwrócić 0.

3. **Metodę** wyświetlającą informacje o prostokącie, takie jak współrzędne wierzchołków i pole.

Napisz program, który:

- Utworzy dwa prostokąty:
  - Prostokąt A z wierzchołkami (3, 4) i (9, 6).
  - Prostokąt B z wierzchołkami (2, 2) i (7, 5).
- Wyświetli informacje o obu prostokątach.
- Obliczy i wyświetli pole części wspólnej tych prostokątów.

### Dane wejściowe

- Współrzędne prostokątów:
  - Prostokąt A: (3, 4), (9, 6)
  - Prostokąt B: (2, 2), (7, 5)

### Dane wyjściowe

- Informacje o prostokątach A i B.
- Pole nałożenia się prostokątów (oczekiwana wartość to 6).

### Przykład

- **Dane wejściowe**:
  ```
  Prostokąt A: (3, 4), (9, 6)
  Prostokąt B: (2, 2), (7, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
  Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
  Pole części wspólnej: 6
  ```

### Wskazówki

- Aby obliczyć pole części wspólnej:
  - Oblicz współrzędne części wspólnej:
    - \( x_{\text{lewy wspólny}} = \max(x_{\text{lewy A}}, x_{\text{lewy B}}) \)
    - \( y_{\text{dolny wspólny}} = \max(y_{\text{dolny A}}, y_{\text{dolny B}}) \)
    - \( x_{\text{prawy wspólny}} = \min(x_{\text{prawy A}}, x_{\text{prawy B}}) \)
    - \( y_{\text{górny wspólny}} = \min(y_{\text{górny A}}, y_{\text{górny B}}) \)
  - Jeśli \( x_{\text{lewy wspólny}} < x_{\text{prawy wspólny}} \) i \( y_{\text{dolny wspólny}} < y_{\text{górny wspólny}} \), to prostokąty nachodzą na siebie.
  - Pole części wspólnej to:
    \[
    (x_{\text{prawy wspólny}} - x_{\text{lewy wspólny}}) \times (y_{\text{górny wspólny}} - y_{\text{dolny wspólny}})
    \]

---

## Zadanie 4 - Zaprojektuj klasy Wektor2D i Wektor3D

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj klasy:

1. **Wektor2D** — reprezentującą wektor w przestrzeni dwuwymiarowej.
2. **Wektor3D** — reprezentującą wektor w przestrzeni trójwymiarowej.

Obie klasy powinny zawierać:

1. **Konstruktor**, który przyjmuje odpowiednio dwa lub trzy argumenty (współrzędne wektora). Domyślne wartości wszystkich argumentów powinny wynosić 0.

2. **Metody** realizujące podstawowe operacje arytmetyczne:
   - **Dodawanie** wektorów.
   - **Odejmowanie** wektorów.
   - **Iloczyn skalarny**.
   - **Iloczyn wektorowy** (tylko dla **Wektor3D**).

3. **Metodę** wyświetlającą informacje o wektorze.

4. **Metody porównujące** dwa wektory pod względem równości i nierówności.

5. **Metodę** obliczającą **moduł** (długość) wektora.

Napisz program, który:

- Utworzy dwa wektory:
  - Wektor A: (-3, -3, -3)
  - Wektor B: (5, 5, 5)
- Wyświetli informacje o obu wektorach.
- Obliczy i wyświetli:
  - Sumę wektorów A i B.
  - Różnicę wektorów A i B.
  - Iloczyn skalarny wektorów A i B.
  - Iloczyn wektorowy wektorów A i B.

### Dane wejściowe

- Współrzędne wektorów:
  - Wektor A: \( x = -3 \), \( y = -3 \), \( z = -3 \)
  - Wektor B: \( x = 5 \), \( y = 5 \), \( z = 5 \)

### Dane wyjściowe

- Informacje o wektorach A i B.
- Wyniki operacji arytmetycznych:
  - Suma wektorów.
  - Różnica wektorów.
  - Iloczyn skalarny.
  - Iloczyn wektorowy.

### Przykład

- **Dane wejściowe**:
  ```
  Wektor A: (-3, -3, -3)
  Wektor B: (5, 5, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  Wektor A: (-3, -3, -3)
  Wektor B: (5, 5, 5)
  Suma wektorów: (2, 2, 2)
  Różnica wektorów A - B: (-8, -8, -8)
  Iloczyn skalarny: -45
  Iloczyn wektorowy: (0, 0, 0)
  ```

### Wskazówki

- Iloczyn skalarny dla wektorów \( \vec{A} \) i \( \vec{B} \):
  \[
  \vec{A} \cdot \vec{B} = A_x B_x + A_y B_y (+ A_z B_z)
  \]
- Iloczyn wektorowy dla wektorów trójwymiarowych:
  \[
  \vec{A} \times \vec{B} = (A_y B_z - A_z B_y, A_z B_x - A_x B_z, A_x B_y - A_y B_x)
  \]
- Moduł wektora:
  \[
  |\vec{A}| = \sqrt{A_x^2 + A_y^2 (+ A_z^2)}
  \]

---

## Zadanie 5 - Zaprojektuj klasę Macierz

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj klasę **Macierz**, która będzie reprezentować macierz liczbową. Klasa powinna zawierać:

1. **Konstruktor**, który przyjmuje listę list liczb całkowitych, reprezentującą macierz. Domyślną wartością argumentu powinna być pusta lista.

2. **Metody** realizujące podstawowe operacje arytmetyczne:
   - **Dodawanie** macierzy.
   - **Odejmowanie** macierzy.
   - **Mnożenie** macierzy.
   - **Odwracanie** macierzy (jeśli jest odwracalna).

3. **Metodę** wyświetlającą informacje o macierzy.

4. **Metody porównujące** dwie macierze pod względem równości i nierówności.

Napisz program, który:

- Utworzy dwie macierze:
  - Macierz A:
    \[
    \begin{bmatrix}
    1 & 3 \\
    4 & 2 \\
    \end{bmatrix}
    \]
  - Macierz B:
    \[
    \begin{bmatrix}
    5 & 0 \\
    1 & 3 \\
    \end{bmatrix}
    \]
- Wyświetli informacje o obu macierzach.
- Obliczy i wyświetli:
  - Sumę macierzy A i B.
  - Różnicę macierzy A i B.
  - Iloczyn macierzy A i B.

### Dane wejściowe

- Elementy macierzy A: [[1, 3], [4, 2]]
- Elementy macierzy B: [[5, 0], [1, 3]]

### Dane wyjściowe

- Informacje o macierzach A i B.
- Wyniki operacji arytmetycznych:
  - Suma macierzy.
  - Różnica macierzy A - B.
  - Iloczyn macierzy A i B.

### Przykład

- **Dane wejściowe**:
  ```
  Macierz A:
  [1, 3]
  [4, 2]

  Macierz B:
  [5, 0]
  [1, 3]
  ```
- **Oczekiwane wyjście**:
  ```
  Macierz A:
  [1, 3]
  [4, 2]

  Macierz B:
  [5, 0]
  [1, 3]

  Suma macierzy:
  [6, 3]
  [5, 5]

  Różnica macierzy A - B:
  [-4, 3]
  [3, -1]

  Iloczyn macierzy A * B:
  [8, 9]
  [22, 12]
  ```

### Wskazówki

- Przy operacjach arytmetycznych upewnij się, że macierze mają odpowiednie wymiary.
- Mnożenie macierzy:
  \[
  C_{ij} = \sum_{k} A_{ik} \times B_{kj}
  \]
- Odwracanie macierzy jest możliwe tylko dla macierzy kwadratowych o wyznaczniku różnym od zera.

---

## Zadanie 6 - Zaprojektuj klasę LiczbaZespolona

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj klasę **LiczbaZespolona**, która będzie reprezentować liczbę zespoloną. Klasa powinna zawierać:

1. **Konstruktor**, który przyjmuje dwie liczby:
   - Pierwsza liczba — część rzeczywista.
   - Druga liczba — część urojona.
   - Domyślne wartości obu argumentów to 0.

2. **Metody** realizujące podstawowe operacje arytmetyczne:
   - **Dodawanie** liczb zespolonych.
   - **Odejmowanie** liczb zespolonych.
   - **Mnożenie** liczb zespolonych.
   - **Dzielenie** liczb zespolonych.

3. **Metodę** wyświetlającą informacje o liczbie zespolonej w formacie \( a + bi \).

4. **Metody porównujące** dwie liczby zespolone pod względem równości i nierówności.

5. **Metodę** obliczającą **moduł** liczby zespolonej.

Napisz program, który:

- Utworzy dwie liczby zespolone:
  - Liczba A: \( 9 + 12i \)
  - Liczba B: \( -3 - 3i \)
- Wyświetli informacje o obu liczbach.
- Obliczy i wyświetli:
  - Sumę liczb A i B.
  - Różnicę liczb A i B.
  - Iloczyn liczb A i B.
  - Iloraz liczby A przez liczbę B.

### Dane wejściowe

- Liczba A: część rzeczywista 9, część urojona 12
- Liczba B: część rzeczywista -3, część urojona -3

### Dane wyjściowe

- Informacje o liczbach A i B.
- Wyniki operacji arytmetycznych.

### Przykład

- **Dane wejściowe**:
  ```
  Liczba A: 9 + 12i
  Liczba B: -3 - 3i
  ```
- **Oczekiwane wyjście**:
  ```
  Liczba A: 9 + 12i
  Liczba B: -3 - 3i

  Suma: 6 + 9i
  Różnica A - B: 12 + 15i
  Iloczyn: 27 + 63i
  Iloraz A / B: -3.5 + 0.5i
  ```

### Wskazówki

- Dodawanie i odejmowanie liczb zespolonych:
  \[
  (a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i
  \]
- Mnożenie liczb zespolonych:
  \[
  (a + bi)(c + di) = (ac - bd) + (ad + bc)i
  \]
- Dzielenie liczb zespolonych:
  \[
  \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2}
  \]
- Moduł liczby zespolonej:
  \[
  |a + bi| = \sqrt{a^2 + b^2}
  \]

---

## Zadanie 7 - Zliczanie instancji klasy

**Poziom trudności**: ★☆☆

### Treść zadania

Zaprojektuj klasę **MojaKlasa**, która będzie posiadać mechanizm zliczania liczby utworzonych instancji tej klasy. Klasa powinna zawierać:

1. **Prywatne pole statyczne** przechowujące liczbę instancji.

2. **Konstruktor**, który zwiększa licznik instancji przy każdym utworzeniu obiektu.

3. **Metodę statyczną** zwracającą aktualną liczbę instancji klasy.

Napisz program, który:

- Utworzy kilka obiektów klasy **MojaKlasa**.
- Wyświetli aktualną liczbę instancji tej klasy.

### Dane wejściowe

- Brak danych wejściowych.

### Dane wyjściowe

- Liczba naturalna reprezentująca aktualną liczbę instancji klasy.

### Przykład

- **Oczekiwane wyjście** (przykładowo dla 3 instancji):
  ```
  Liczba utworzonych instancji: 3
  ```

### Wskazówki

- Upewnij się, że licznik instancji jest poprawnie aktualizowany przy tworzeniu obiektów.
- Pamiętaj o dostępie do pola statycznego i metod statycznych.

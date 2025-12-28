<div align="center">
<a href="https://github.com/djeada/Nauka-programowania/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/djeada/Nauka-programowania"></a>
<a href="https://github.com/djeada/Nauka-programowania/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/djeada/Nauka-programowania"></a>
<a href="https://github.com/djeada/Nauka-programowania/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/djeada/Nauka-programowania"></a>
<a href=""><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
</div>

# Nauka Programowania

Witaj w świecie programowania! Jeśli zastanawiasz się, od czego zacząć, to jesteś w idealnym miejscu. Ten projekt oferuje ciąg zadań, które przeprowadzą Cię przez kluczowe koncepcje potrzebne do zrozumienia programowania, od podstaw aż do bardziej zaawansowanych tematów.

![nauka_programowania](https://github.com/user-attachments/assets/64fb3baa-c080-45c0-bb8f-abb612581f18)

## Gdzie mogę znaleźć dodatkowe materiały do nauki?

Oferujemy też szeroki wybór dodatkowych materiałów, takich jak notatki i poradniki dotyczące Pythona i C++, które są dostępne na naszych stronach GitHub:

* [Notatki Python](https://github.com/djeada/Kurs-podstaw-Pythona)
* [Notatki C++](https://github.com/djeada/C-and-Cpp)

## Zbiór zadań

Nasz zbiór zadań to bogate źródło wiedzy:

* [Zbiór zadań](https://github.com/djeada/Nauka-Programowania/tree/master/zbior_zadan)
* Zbiór jest regularnie poszerzany i aktualizowany.
* Informacje o dodawaniu własnych rozwiązań znajdziesz [tutaj](https://github.com/djeada/Nauka-Programowania/blob/master/CONTRIBUTING.md).

### Generowanie PDF

Możesz wygenerować profesjonalny PDF ze wszystkimi zadaniami:

```bash
# Zainstaluj wymagane biblioteki
pip install weasyprint markdown2 pygments

# Wygeneruj PDF
python3 scripts/generate_pdf.py
```

Skrypt utworzy plik `Nauka_Programowania_Zbior_Zadan.pdf` zawierający wszystkie 25 rozdziałów w czystym, profesjonalnym formacie. PDF zawiera stronę tytułową, spis treści, oraz wszystkie zadania z odpowiednim formatowaniem kodu, tabel i wzorów matematycznych.

## O zadaniach

Zadania są podzielone tematycznie i ułożone według stopnia trudności, aby każdy mógł ćwiczyć podstawowe koncepcje programowania:

1. **Podstawy (Rozdziały 1-8):** Zmienne, warunki, pętle. Rozwiązania sprawdzane są ręcznie przez interakcję z konsolą.
2. **Poziom średnio zaawansowany (Rozdziały 9-17):** Struktury danych, rekurencja, binarna reprezentacja liczb. Wymagają automatycznych testów i uwzględnienia skrajnych przypadków.
3. **Zaawansowane (Rozdziały 18-25):** Praca z plikami, algorytmy sortowania, obsługa błędów. Wymagają głębszej wiedzy i narzędzi takich jak debugowanie.

Przykładowe rozwiązania służą jako wskazówki i często prezentują różne podejścia do rozwiązania problemów.

## Wspierane wersje języków

Przykłady zostały przetestowane w różnych wersjach języków:

### C++
- Standard: C++11, C++17, C++20.
- Kompilacja: `g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o plik_wykonwyalny.out sciezka_do_zadania.cpp`.
- Formatowanie: `clang-format -i -style=file sciezka_do_zadania.cpp`.

### Python
- Wersja:`3.10`.
- Uruchomienie: `python3 sciezka_do_zadania.py`.
- Formatowanie: `black sciezka_do_zadania.py`.

### Java
- Wersja: `Java SE 18`.
- Kompilacja: `javac -d . sciezka_do_zadania.java`.
- Formatowanie: `java -jar google-java-format-1.7-all-deps.jar sciezka_do_zadania.java`.

### JavaScript
- Środowisko: `NodeJS 20.0.0`.
- Uruchomienie: `node sciezka_do_zadania.js`.
- Formatowanie: `eslint --fix sciezka_do_zadania.js` z konfiguracją `.eslintrc.json`.

### Haskell
- Wersja: `GHC 9.2.1`.
- Kompilacja: `ghc -o plik_wykonawczy.out sciezka_do_zadania.hs`.
- Formatowanie: `ormolu --mode inplace sciezka_do_zadania.hs`.

### Rust
- Wersja: `1.74.0`.
- Kompilacja: `rustc sciezka_do_zadania.rs`.
- Formatowanie: `rustfmt --write-mode=overwrite sciezka_do_zadania.rs`.

Nauka programowania to proces wymagający czasu i praktyki, ale z naszymi zasobami będziesz miał solidną podstawę do rozwoju umiejętności programistycznych. Jeśli masz pytania lub potrzebujesz pomocy, skontaktuj się z nami - z chęcią Ci pomożemy!

## Rozwiązania

<!--ts-->
   1. [Interakcja z konsolą](#Interakcja-z-konsolą)
   1. [Instrukcja warunkowa](#Instrukcja-warunkowa)
   1. [Daty](#Daty)
   1. [Pętla - wprowadzenie](#Pętla---wprowadzenie)
   1. [Pętla - wyznaczanie cyfr liczby](#Pętla---wyznaczanie-cyfr-liczby)
   1. [Funkcje - wprowadzenie](#Funkcje---wprowadzenie)
   1. [Pętla - algorytmy matematyczne](#Pętla---algorytmy-matematyczne)
   1. [Pętla - pętle zagnieżdżone](#Pętla---pętle-zagnieżdżone)
   1. [Listy - wprowadzenie](#Listy---wprowadzenie)
   1. [Listy - dwie listy](#Listy---dwie-listy)
   1. [Napisy - wprowadzenie](#Napisy---wprowadzenie)
   1. [Napisy - anagramy i palindromy](#Napisy---anagramy-i-palindromy)
   1. [Listy 2d](#Listy-2d)
   1. [Funkcje - wielomiany](#Funkcje---wielomiany)
   1. [Funkcje - rekurencja](#Funkcje---rekurencja)
   1. [System binarny](#System-binarny)
   1. [Słowniki](#Słowniki)
   1. [Klasy](#Klasy)
   1. [Dziedziczenie](#Dziedziczenie)
   1. [Operacje na plikach](#Operacje-na-plikach)
   1. [Sortowanie - algorytmy](#Sortowanie---algorytmy)
   1. [Sortowanie - praktyka](#Sortowanie---praktyka)
   1. [Wyrażenia regularne](#Wyrażenia-regularne)
   1. [Listy - trudne](#Listy---trudne)
   1. [Napisy - trudne](#Napisy---trudne)

<!--te-->

## Interakcja z konsolą

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Wypisz na standardowe wyjście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zamiana kolejności.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Narysuj kształt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Operacje arytmetyczne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Wartość funkcji w punkcie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zamiana jednostek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pola figur i objętości brył.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Cena podłogi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad08.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Kalkulator kredytowy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad09.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
    </tbody>
</table>

## Instrukcja warunkowa

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Porównanie ze stałą.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Porównanie ze zmienną.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Znak liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Maks/min dwóch liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie trzech liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Maks czterech liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dowody praw logicznych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Warunek trójkąta.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcja_warunkowa/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcja_warunkowa/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcja_warunkowa/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcja_warunkowa/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcja_warunkowa/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcja_warunkowa/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcja_warunkowa/zad08.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
    </tbody>
</table>

## Daty
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Czy liczba jest poprawnym numerem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad1/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Czy osoba jest pełnoletnia?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad2/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Rok przestępny.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad3/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dzień tygodnia odpowiadający danej liczbie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad4/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Ile dni ma miesiąc?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad5/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Poprawność daty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad6/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Ile dni minęło od początku roku?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad7/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Jaki mamy dzień tygodnia?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad8/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Pętla - wprowadzenie
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Warunek kończący pętlę.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Liczby mniejsze od podanej liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Liczba *Pi*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Suma liczb mniejszych od liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Liczby z przedziału.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Suma wyrazów ciągu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Liczba *Pi* podniesiona do potęgi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Znajdź liczbę kur oraz owieczek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Pętla - wyznaczanie cyfr liczby
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Ile cyfr ma liczba?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Cyfry, z których składa się liczba.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma cyfr liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Cyfry liczby spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Czy liczba jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Wszystkie liczby spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
    </tbody>
</table>

## Funkcje - wprowadzenie
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Zwróć stałą.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Operacja arytmetyczna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sprawdź warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Maks i min.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zamień wartości miejscami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Cyfry liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Hasło.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Zaokrąglanie w dół.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Pętla - algorytmy matematyczne
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Średnia z *n* liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Podnieś *a* do *b*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Mnożenie i dzielenie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Silnia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>NWD.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad05.sh">Bash</a></td>
             <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>NWW.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pierwiastek metodą Newtona.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Naiwny test pierwszości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/07_petla_algorytmy_matematyczne/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/07_petla_algorytmy_matematyczne/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Pętla - pętle zagnieżdżone
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Kwadrat.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Trójkąt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Odwrócony trójkąt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Tabliczka mnożenia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad04.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Litera *X*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Litera *Z*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Choinka.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Trójkąt Pascala.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>*N* pierwszych liczb pierwszych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/08_petle_zagniezdzone/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/08_petle_zagniezdzone/zad09.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
    </tbody>
</table>

## Listy - wprowadzenie
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Wczytaj i wypisz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Wczytaj, zmodyfikuj i wypisz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Pierwsze wystąpienie klucza.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Minimum oraz maksimum.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zmodyfikuj elementy spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Czy średnia elementów znajduje się w liście?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Liczba mniejsza od największej i większa od wszystkich pozostałych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Usuń klucz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad08.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad09.py">Usuń duplikaty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad09.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Czy punkty mogą stanowić wierzchołki trójkąta?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad10.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Samochody.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad11.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Rotacja w lewo/prawo.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad12.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad12.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad12.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>13</td>
            <td>Brakujący element w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad13.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad13.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad13">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad13.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad13.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad13.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad13.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>14</td>
            <td>Element bez pary w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad14.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad14.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad14">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad14.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad14.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad14.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad14.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>15</td>
            <td>Element dominujący.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad15.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad15.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad15">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad15.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad15.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad15.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad15.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>16</td>
            <td>Suma dwóch.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad16.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad16.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad16">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad16.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad16.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad16.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad16.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>17</td>
            <td>Pary, których suma jest równa liczbie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad17.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad17">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad17.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad17.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad17.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad17.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>18</td>
            <td>Lista posortowane została przesunięta.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad18.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad18.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad18">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad18.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad18.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/09_listy_wprowadzenie/zad18.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/09_listy_wprowadzenie/zad18.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Listy - dwie listy
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Wypisz na przemian.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Połączenie list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Mnożenie wektorowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Średnia ważona wartości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Część wspólna dwóch list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Różnica między dwoma listami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Połącz posortowane listy w posortowaną listę.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń z pierwszej listy część wspólną obu list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad09.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Znajdź medianę dwóch posortowanych list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/10_listy_dwie_listy/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/10_listy_dwie_listy/zad10.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Napisy - wprowadzenie
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Odwróć napis.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Policz wystąpienia znaku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Z ilu słów składa się zdanie?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djea/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zamień wszystkie małe litery na wielkie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Napisy_wprowadzenie/blob/master/src/js/11_napisy_wprowadzenie/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Wypisz poziomo i pionowo co *k*-ty znak napisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zamień litery *a* na znaki zapytania.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Zamień znaki na numery ASCII.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wypisz pionowo słowa, z których składa się zdanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djea/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad08.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Wczytaj i rozdziel informacje o pracowniku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad09.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Znajdź najdłuższe/najkrótsze słowo w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad10.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Średnia długość słów w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad11.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Usuń spacje ze zdania.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad12.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad12.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad12.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>13</td>
            <td>Znaki znajdujące się na pozycjach będących liczbami pierwszymi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad13.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_napisy_wprowadzenie/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad13">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad13.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad13.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad13.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad13.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>14</td>
            <td>Napis składający się z liczb od 1 do *n*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad14.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad14.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad14">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad14.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad14.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad14.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad14.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>15</td>
            <td>Słowa ze zdania jako osobne elementy listy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad15.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad15.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad15">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad15.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad15.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad15.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad15.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>16</td>
            <td>Odległość Hamminga.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad16.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad16.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad16">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad16.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad16.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad16.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad16.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>17</td>
            <td>Zamień listę na napis.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad17.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad17.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad17">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad17.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad17.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad17.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad17.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>18</td>
            <td>Odwróć napisy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad18.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad18.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad18">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad18.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad18.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/11_napisy_wprowadzenie/zad18.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/11_napisy_wprowadzenie/zad18.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Napisy - anagramy i palindromy
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Czy słowo jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Wszystkie permutacje słowa.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy słowa są swoimi anagramami?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wszystkie palindromy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad04.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Znajdź anagramy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Permutacja będąca palindromem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Najmniej usunięć do anagramów</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad07.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wyjątkowe palindromy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/12_napisy_anagramy_palindromy/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/12_napisy_anagramy_palindromy/zad08.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## Listy 2d
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Macierz *a* identycznych wierszy składających się z liczb od 0 do *b*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Każdy element jest iloczynem współrzędnych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Macierz z par odpowiadających sobie elementów dwóch list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dodawanie/odejmowanie macierzy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Magiczny kwadrat.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Pokrywające się przedziały w liście przedziałów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Wyzeruj macierz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wypisz spiralnie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Klepsydra o największej sumie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad09.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Obróć o 90 stopni.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad10.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Gra w statki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/13_listy_2d/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/13_listy_2d/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/13_listy_2d/zad11.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## Funkcje - wielomiany
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Wartość wielomianu w punkcie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/14_funkcje_wielomiany/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/14_funkcje_wielomiany/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/14_funkcje_wielomiany/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Iloczyn wielomianu przez skalar.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/14_funkcje_wielomiany/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/14_funkcje_wielomiany/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/14_funkcje_wielomiany/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma wielomianów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/14_funkcje_wielomiany/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/14_funkcje_wielomiany/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/14_funkcje_wielomiany/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Mnożenie wielomianów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/14_funkcje_wielomiany/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/14_funkcje_wielomiany/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/14_funkcje_wielomiany/zad04.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>N-ta pochodna wielomianu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad5">Java</a></td>
            <td><a href="https://github.com/dje/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/14_funkcje_wielomiany/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/14_funkcje_wielomiany/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/14_funkcje_wielomiany/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Miejsce zerowe funkcji kwadratowej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/14_funkcje_wielomiany/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/14_funkcje_wielomiany/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/14_funkcje_wielomiany/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Funkcje - rekurencja
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Liczby naturalne mniejsze od *N*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Suma liczb naturalnych mniejszych od *N*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Potęgowanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Silnia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Liczba Fibonacciego.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>*N*-ty wyraz ciągu danego wzorem rekurencyjnym.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Wyszukiwanie liniowe rekurencyjnie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wieża Hanoi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Słowa elfickie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad09.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Gra.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/15_funkcje_rekurencja/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/15_funkcje_rekurencja/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/15_funkcje_rekurencja/zad10.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## System binarny
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Konwersja między systemami binarnym i dziesiętnym.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Konwersja gdy spełniony jest warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Operacje arytmetyczne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zera/jedynki w liczbie binarnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Min/maks z dwóch liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Konwersja między dowolnymi systemami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Zamiana sąsiadów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Następna potęga dwójki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad8">Java</a></td>
            <td><a href="https://github.com/dje/Nauka-programowania/blob/master/src/js/16_system_binarny/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad08.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Zmiana wielkości liter.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad09.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Zamień *A* w *B*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad10.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Czy liczba jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad11.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Najdłuższy ciąg zer w liczbie binarnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/16_system_binarny/zad12.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/16_system_binarny/zad12.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/16_system_binarny/zad12.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## Słowniki
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Kluczami są liczby, a wartościami ich kwadraty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Kluczami są elementy jednej listy, a wartościami elementy drugiej listy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad02.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Klucz to imię, wartość lista wypożyczonych książek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Usuń ze słownika.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Lista pracowników.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Histogram znaków w słowie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Histogram słów w tekście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Najczęściej występująca litera w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad08.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Powtarzające się znaki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad09.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Anagramy w tekście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad10.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Sortowanie względem kluczy/wartości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad11.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Czy słowniki są identyczne?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/17_slowniki/zad12.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/17_slowniki/zad12.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/17_slowniki/zad12.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Klasy
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Zaprojektuj klasę *Koło*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad01.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad01.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zaprojektuj klasę *Punkt*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad02.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Prostokąt powstały z nałożenia się dwóch prostokątów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad03.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad03.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zaprojektuj klasy *Wektor2d* oraz *Wektor3D*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad04.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad04.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zaprojektuj klasę *Zespolona*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad05.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zaprojektuj klasę *Macierz.*</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad06.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Znajdź liczbę instancji klasy w programie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_klasy/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_klasy/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_klasy/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_klasy/zad07.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/18_klasy/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
    </tbody>
</table>

## Dziedziczenie
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Wywołaj metodę klasy bazowej w klasie potomnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_dziedziczenie/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_dziedziczenie/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_dziedziczenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_dziedziczenie/zad01.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/19_dziedziczenie/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zaprojektuj klasę bazową *Kształt* oraz klasy potomne *Koło* i *Kwadrat*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_dziedziczenie/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_dziedziczenie/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_dziedziczenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_dziedziczenie/zad02.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/19_dziedziczenie/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Polimorfizm.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_dziedziczenie/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_dziedziczenie/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_dziedziczenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_dziedziczenie/zad03.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/19_dziedziczenie/zad03.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dziedziczenie wielopoziomowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_dziedziczenie/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_dziedziczenie/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_dziedziczenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_dziedziczenie/zad04.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/19_dziedziczenie/zad04.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Dziedziczenie wielokrotne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_dziedziczenie/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_dziedziczenie/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_dziedziczenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_dziedziczenie/zad05.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/19_dziedziczenie/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Operacje na plikach
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Sprawdź, czy ścieżka należy do pliku/folderu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Znajdź w folderze wszystkie pliki z danym rozszerzeniem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Znajdź ścieżkę pliku o danej nazwie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad03.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wczytaj i wypisz treść pliku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Plik z listą adresów ip.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Statystyki dla pliku tekstowego.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dodaj wiersz do pliku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Znajdź i zmodyfikuj pliki spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń pliki spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad09.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Skopiuj pliki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad10.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Podmień treści.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad11.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Przesuń wszystkie pliki csv do jednego folderu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_operacje_na_plikach/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_operacje_na_plikach/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_operacje_na_plikach/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_operacje_na_plikach/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/20_operacje_na_plikach/zad12.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/20_operacje_na_plikach/zad12.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/20_operacje_na_plikach/zad12.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Sortowanie - algorytmy
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Sortowanie bąbelkowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/21_sortowanie_algorytmy/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/21_sortowanie_algorytmy/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Sortowanie przez wybieranie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/21_sortowanie_algorytmy/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/21_sortowanie_algorytmy/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sortowanie przez wstawianie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/21_sortowanie_algorytmy/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/21_sortowanie_algorytmy/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad03.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Sortowanie przez scalanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/21_sortowanie_algorytmy/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/21_sortowanie_algorytmy/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad04.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie szybkie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/21_sortowanie_algorytmy/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/21_sortowanie_algorytmy/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Sortowanie - praktyka
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Posortuj znaki w słowie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad01.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Posortuj słowa w zdaniu</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Posortuj listę par względem jednej z kategorii.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Posortuj względem długości napisy w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie listy obiektów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad05.sh">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Tablica binarna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad06.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Tablica składająca się wyłącznie z zer, jedynek i dwójek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad07.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Tablica cykliczna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/22_sortowanie_praktyka/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/22_sortowanie_praktyka/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/22_sortowanie_praktyka/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Wyrażenia regularne
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Sprawdź poprawność adresu email.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad01.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Sprawdź poprawność hasła.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy napis składa się wyłącznie z cyfr?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad03.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Czy słowo należy do zdania?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad04.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Odfiltruj cyfry z tekstu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad05.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Wiersze kończące się napisem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad06.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Podziel względem znaków interpunkcyjnych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad07.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Cyfry będące częścią słów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad08.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń część wiersza.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad09.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Podmień napisy z listy *A* na napisy z listy *B*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad10.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad10.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad10.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Nazwa pliku ze ścieżki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/23_wyrazenia_regularne/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad11.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/23_wyrazenia_regularne/zad11.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/23_wyrazenia_regularne/zad11.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
    </tbody>
</table>

## Listy - trudne
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Najdłuższy nieprzerwany ciąg jedynek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad01.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Przesuń zera.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Trójka o minimalnym iloczynie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad03.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wspólny podciąg o największej sumie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad04.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zbiór potęgowy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad05.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>*M* posortowanych list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad06.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Woda.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad07.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Sznurek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad08.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Najdłuższy naprzemienny podciąg.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/24_listy_trudne/zad09.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/24_listy_trudne/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/24_listy_trudne/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/24_listy_trudne/zad09.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## Napisy - trudne
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Tytuł</th>
            <th colspan="7">Rozwiązania</th>
            <th>Poziom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Podmiana wszystkich wystąpień słowa.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad01.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad01.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad01.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad01.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad01.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad01.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Usuń wszystkie wystąpienia podnapisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad02.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad02.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad02.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad02.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad02.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad02.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy napis *A* stanowi początek napisu *B*?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad03.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad03.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad03.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad03.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad03.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad03.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Usuń powtórzenia z napisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad04.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad04.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad04.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad04.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad04.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad04.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Znaki stojące obok siebie nie mogą się powtarzać.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad05.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad05.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad05.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad05.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad05.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad05.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Czy napisy są swoimi rotacjami?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad06.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad06.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad06.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad06.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad06.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad06.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Znajdź powtórzenia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad07.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad07.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad07.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad07.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad07.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad07.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Najdłuższy wspólny przedrostek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad08.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad08.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad08.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad08.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad08.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad08.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Najdłuższy wspólny potomek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad09.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad09.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/25_napisy_trudne/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/25_napisy_trudne/zad09.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/25_napisy_trudne/zad09.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/25_napisy_trudne/zad09.rs">Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## Literatura

* Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. "*Introduction to Algorithms, 3rd Edition (The MIT Press)*"
* Steven Halim "*Competitive Programming 3*" 
* Narasimha Karumanchi "*Data Structures and Algorithms Made Easy: Data Structures and Algorithmic Puzzles*" 
* Brian Kernighan, Dennis Ritchie "*The C Programming Language*" 
* Steven Skiena, Miguel Revilla "*Programming Challenges: The Programming Contest Training Manual*" 
* Antti Laaksonen "*  Guide to Competitive Programming: Learning and Improving Algorithms Through Contests (Undergraduate Topics in Computer Science) *" 
* Nite Nimajneb "*The Hitchhiker’s Guide to the Programming Contests*" 

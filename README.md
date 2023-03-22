<div align="center">
  
<a href="https://github.com/djeada/Nauka-programowania/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/djeada/Nauka-programowania"></a>
<a href="https://github.com/djeada/Nauka-programowania/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/djeada/Nauka-programowania"></a>
<a href="https://github.com/djeada/Nauka-programowania/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/djeada/Nauka-programowania"></a>
<a href=""><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
</div>

# Nauka-programowania
Jeśli chcesz nauczyć się programować, ale nie wiesz od czego zacząć, to trafiłeś we właściwe miejsce. Ten projekt oferuje zbiór zadań, które przeprowadzą Cię przez wszystkie koncepcje potrzebne do zrozumienia w programowaniu.

![laptop_with_snake_Seed-7632331_Steps-50_Guidance-7 5](https://user-images.githubusercontent.com/37275728/221419671-2d82a012-509d-4331-866c-af8eeb2b84a9.png)

## Gdzie mogę znaleźć dodatkowe materiały do nauki?

Materiały dodatkowe, takie jak notatki z Python i C++, są dostępne na naszych osobnych repozytoriach na GitHubie:

* <a href="https://github.com/djeada/Kurs-podstaw-Pythona">Notatki Python.</a>  
* <a href="https://github.com/djeada/C-and-Cpp">Notatki C++.</a> 

# Zbiór zadań

* Aktualny zbiór zadań znajdziesz pod tym <a href="https://github.com/djeada/Nauka-Programowania/tree/master/zbior_zadan">linkiem</a>. </br>
* Zbiór będzie poszerzany i aktualizowany.
* Więcej informacji na temat tego jak dodać własne rozwiązania, znajdziesz na <a href="https://github.com/djeada/Nauka-Programowania/blob/master/CONTRIBUTING.md">tej stronie</a>.

## O zadaniach
Zadania zostały podzielone tematycznie i uporządkowane według stopnia zaawansowania. Przygotowaliśmy je w taki sposób, aby każdy - nawet początkujący uczeń - mógł przećwiczyć podstawowe koncepcje programowania. W odróżnieniu od wielu innych kursów, które szybko przechodzą do bardziej zaawansowanych mechanizmów, nasze zadania koncentrują się głównie na podstawach.

* Pierwsze 8 rozdziałów jest poświęcone najbardziej podstawowym koncepcjom, takim jak zmienne, warunki i pętle. Rozwiązania powinny być sprawdzane ręcznie poprzez komunikację z programem za pomocą konsoli. Dane wpisywane są z klawiatury, a wynik wyświetlany na ekranie.
* W rozdziałach 9-17 znajdują się zadania wymagające zrozumienia koncepcji z pierwszych 8 rozdziałów oraz rozszerzające je o zagadnienia takie jak struktury danych, rekurencja i binarna reprezentacja liczb. Osoba rozwiązująca zadania powinna przygotować automatyczne testy dla swojego rozwiązania, uwzględniając wszystkie skrajne przypadki.
* W rozdziałach 18-25 poruszane są bardziej zaawansowane tematy, takie jak praca z plikami, algorytmy sortowania i obsługa błędów. Zadania te wymagają już większej zaawansowanej wiedzy i umiejętności, a także znajomości narzędzi takich jak debugowanie i profilowanie kodu. Zadania te wymagają dużej samodzielności i umiejętności samodzielnego poszukiwania informacji oraz rozwiązywania problemów.

Przykładowe rozwiązania powinny być traktowane jako wskazówki, a nie jako jedyne słuszne sposoby rozwiązania zadania. W szczególności w dalszych rozdziałach, dane zadanie może mieć wiele różnych sposobów rozwiązania. Część przykładowych rozwiązań może zawierać nawet więcej niż jeden wariant rozwiązania. Alternatywne rozwiązania mogą różnić się między sobą pod względem złożoności czasowej, pamięciowej lub użycia funkcji języka.

Należy pamiętać, że nauka programowania to długi proces, ale dzięki naszemu zbiorowi zadań oraz dodatkowym materiałom, powinieneś być w stanie wypracować solidne podstawy i rozwijać swoje umiejętności, które pozwolą Ci na osiągnięcie sukcesu w sektorze IT.

Jeśli masz jakieś pytania lub potrzebujesz dodatkowej pomocy, nie wahaj się skontaktować z nami. Chętnie Ci pomożemy.

## Wspierane wersje języków

Przykłady zostały przetestowane i dostosowane do następujących wersji języków:

### C++

Większość przykładów wykorzystuje standard `C++11`. Niektóre zadania rozwiązane zostały przy użyciu składni wprowadzonej w wersjach `C++17` i `C++20`. Aby skompilować przykłady, należy użyć kompilatora `GCC` z flagami: `g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o plik_wykonwyalny.out sciezka_do_zadania.cpp`. Do formatowania kodu należy użyć narzędzia `clang-format` z flagami: `clang-format -i -style=file sciezka_do_zadania.cpp`. Przykłady nie używają bibliotek zewnętrznych.

### Python

Wszystkie przykłady zostały przetestowane i dostosowane do wersji `3.8`. Skrypty języka Python nie wymagają kompilacji - aby uruchomić skrypt, należy użyć komendy `python sciezka_do_zadania.py`. Do formatowania kodu należy użyć narzędzia `black` bez flag: `black sciezka_do_zadania.py`. Przykłady nie używają bibliotek zewnętrznych.

### Java
    
Przykłady zostały przetestowane i dostosowane do wersji `Java SE 17`. Aby skompilować przykłady z tego języka, należy użyć kompilatora `javac` z flagami: `javac -d . sciezka_do_zadania.java`. Do formatowania kodu należy użyć narzędzia `google-java-format` z flagami: `java -jar google-java-format-1.7-all-deps.jar sciezka_do_zadania.java`. Przykłady nie używają bibliotek zewnętrznych.

### JavaScript

Rozwiązania zostały przetestowane i dostosowane do środowiska `NodeJS 19.8.1`. Skrypty języka JavaScript nie wymagają kompilacji - aby uruchomić skrypt, należy użyć komendy `node sciezka_do_zadania.js`. Do formatowania kodu należy użyć narzędzia `eslint` z konfiguracją: `.eslintrc.json` oraz flagami: `eslint --fix sciezka_do_zadania.js`. Przykłady nie używają bibliotek zewnętrznych.

### Haskell

Przykłady zostały przetestowane i dostosowane do wersji `GHC 8.10.2`. Aby skompilować przykłady z tego języka, należy użyć kompilatora `ghc` z flagami: `ghc -O2 -threaded -rtsopts -eventlog sciezka_do_zadania.hs -o plik_wykonywalny`. Do formatowania kodu należy użyć narzędzia `ormolu` z flagami:
`ormolu --mode inplace sciezka_do_zadania.hs`. Przykłady nie używają bibliotek zewnętrznych.

### Rust

Przykłady zostały przetestowane i dostosowane do wersji `1.68.0`. Aby skompilować przykłady z tego języka, należy użyć kompilatora `rustc` bez flag: `rustc sciezka_do_zadania.rs`. Do formatowania kodu należy użyć narzędzia `rustfmt` z flagami: `rustfmt --write-mode=overwrite sciezka_do_zadania.rs`. Przykłady nie używają bibliotek zewnętrznych.

## Rozwiązania

<!--ts-->
   1. [Interakcja z konsolą](#Interakcja-z-konsolą)
   1. [Instrukcje sterujące](#Instrukcje-sterujące)
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
   1. [Operacje na plikach](#Operacje-na-plikach)
   1. [Klasy](#Klasy)
   1. [Dziedziczenie](#Dziedziczenie)
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad1.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad1.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zamiana kolejności.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad2.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad2.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Narysuj kształt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad3.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad3.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Operacje arytmetyczne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad4.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad4.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Wartość funkcji w punkcie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad5.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad5.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad5.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zamiana jednostek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad6.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad6.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad6.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pola figur i objętości brył.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad7.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad7.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad7.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Cena podłogi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad8.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad8.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad8.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Kalkulator kredytowy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/01_interakcja_z_konsola/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/01_interakcja_z_konsola/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/01_interakcja_z_konsola/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/01_interakcja_z_konsola/zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/01_interakcja_z_konsola/zad9.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/01_interakcja_z_konsola/zad9.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/01_interakcja_z_konsola/zad9.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
    </tbody>
</table>

## Instrukcje sterujące

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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad1.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad1.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Porównanie ze zmienną.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad2.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad2.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Znak liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad3.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad3.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Maks/min dwóch liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad4.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad4.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie trzech liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad5.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad5.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad5.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Maks czterech liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad6.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad6.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad6.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dowody praw logicznych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad7.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad7.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad7.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Warunek trójkąta.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/02_instrukcje_sterujace/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/02_instrukcje_sterujace/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/02_instrukcje_sterujace/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/02_instrukcje_sterujace/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/02_instrukcje_sterujace/zad8.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/02_instrukcje_sterujace/zad8.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/02_instrukcje_sterujace/zad8.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad1/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad1.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad1.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Czy osoba jest pełnoletnia?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad2/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad2.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad2.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Rok przestępny.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad3/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad3.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad3.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dzień tygodnia odpowiadający danej liczbie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad4/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad4.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad4.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Ile dni ma miesiąc?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad5/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad5.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad5.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad5.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Poprawność daty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad6/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad6.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad6.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad6.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Ile dni minęło od początku roku?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad7/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad7.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad7.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad7.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Jaki mamy dzień tygodnia?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/03_daty/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/03_daty/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/03_daty/zad8/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/03_daty/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/03_daty/zad8.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/03_daty/zad8.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/03_daty/zad8.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad1.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad1.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Liczby mniejsze od podanej liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad2.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad2.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Liczba *Pi*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad3.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad3.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Suma liczb mniejszych od liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad4.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad4.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Liczby z przedziału.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad5.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad5.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad5.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Suma wyrazów ciągu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad6.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad6.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad6.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Liczba *Pi* podniesiona do potęgi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad7.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad7.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad7.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Znajdź liczbę kur oraz owieczek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/04_petla_wprowadzenie/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/04_petla_wprowadzenie/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/04_petla_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/04_petla_wprowadzenie/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/04_petla_wprowadzenie/zad8.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/04_petla_wprowadzenie/zad8.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/04_petla_wprowadzenie/zad8.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad1.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad1.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Cyfry, z których składa się liczba.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad2.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad2.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma cyfr liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad3.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad3.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Cyfry liczby spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad4.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad4.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Czy liczba jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad5.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad5.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad5.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Wszystkie liczby spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/05_petla_wyznaczanie_cyfr_liczby/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/05_petla_wyznaczanie_cyfr_liczby/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/05_petla_wyznaczanie_cyfr_liczby/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/05_petla_wyznaczanie_cyfr_liczby/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/05_petla_wyznaczanie_cyfr_liczby/zad6.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/05_petla_wyznaczanie_cyfr_liczby/zad6.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/05_petla_wyznaczanie_cyfr_liczby/zad6.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad1.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad1.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Operacja arytmetyczna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad2.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad2.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sprawdź warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad3.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad3.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Maks i min.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad4.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad4.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zamień wartości miejscami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad5.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad5.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad5.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Cyfry liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad6.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad6.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad6.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Hasło.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad7.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad7.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad7.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Zaokrąglanie w dół.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/06_funkcje_wprowadzenie/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/06_funkcje_wprowadzenie/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/06_funkcje_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/06_funkcje_wprowadzenie/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/06_funkcje_wprowadzenie/zad8.sh">Bash</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/haskell/06_funkcje_wprowadzenie/zad8.hs">Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/06_funkcje_wprowadzenie/zad8.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Podnieś *a* do *b*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Mnożenie i dzielenie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Silnia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>NWD.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>NWW.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pierwiastek metodą Newtona.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Naiwny test pierwszości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/07_petla_algorytmy_matematyczne/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/07_petla_algorytmy_matematyczne/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/07_petla_algorytmy_matematyczne/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/07_petla_algorytmy_matematyczne/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/07_petla_algorytmy_matematyczne/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Trójkąt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Odwrócony trójkąt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Tabliczka mnożenia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Litera *X*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Litera *Z*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Choinka.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/08_petle_zagniezdzone/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Trójkąt Pascala.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>*N* pierwszych liczb pierwszych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/08_petle_zagniezdzone/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/08_petle_zagniezdzone/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/08_petle_zagniezdzone/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/08_petle_zagniezdzone/zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Wczytaj, zmodyfikuj i wypisz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Pierwsze wystąpienie klucza.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Minimum oraz maksimum.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zmodyfikuj elementy spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Czy średnia elementów znajduje się w liście?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Liczba mniejsza od największej i większa od wszystkich pozostałych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Usuń klucz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad9.py">Usuń duplikaty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>17</td>
            <td>Pary, których suma jest równa liczbie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/09_listy_wprowadzenie/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/09_listy_wprowadzenie/zad17.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/09_listy_wprowadzenie/zad17">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/09_listy_wprowadzenie/zad17.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/09_listy_wprowadzenie/zad17.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Połączenie list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Mnożenie wektorowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Średnia ważona wartości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Część wspólna dwóch list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Różnica między dwoma listami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Połącz posortowane listy w posortowaną listę.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń z pierwszej listy część wspólną obu list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/10_listy_dwie_listy/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/10_listy_dwie_listy/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/10_listy_dwie_listy/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/10_listy_dwie_listy/zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/10_listy_dwie_listy/zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Policz wystąpienia znaku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Z ilu słów składa się zdanie?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad3">Java</a></td>
            <td><a href="https://github.com/djea/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zamień wszystkie małe litery na wielkie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Napisy_wprowadzenie/blob/master/src/js/11_napisy_wprowadzenie/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Wypisz poziomo i pionowo co *k*-ty znak napisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zamień litery *a* na znaki zapytania.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Zamień znaki na numery ASCII.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wypisz pionowo słowa, z których składa się zdanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad8">Java</a></td>
            <td><a href="https://github.com/djea/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Wczytaj i rozdziel informacje o pracowniku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/11_napisy_wprowadzenie/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>13</td>
            <td>Znaki znajdujące się na pozycjach będących liczbami pierwszymi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/11_napisy_wprowadzenie/zad13.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_napisy_wprowadzenie/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/11_napisy_wprowadzenie/zad13">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/11_napisy_wprowadzenie/zad13.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/11_napisy_wprowadzenie/zad13.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Wszystkie permutacje słowa.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy słowa są swoimi anagramami?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wszystkie palindromy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Znajdź anagramy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Permutacja będąca palindromem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dla dwóch słów, ile minimalnie znaków musimy usunąć aby uzyskać anagramy?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wyjątkowe palindromy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/12_napisy_anagramy_palindromy/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/12_napisy_anagramy_palindromy/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/12_napisy_anagramy_palindromy/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/12_napisy_anagramy_palindromy/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/12_napisy_anagramy_palindromy/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Każdy element jest iloczynem współrzędnych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Macierz z par odpowiadających sobie elementów dwóch list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dodawanie/odejmowanie macierzy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Magiczny kwadrat.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Pokrywające się przedziały w liście przedziałów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Wyzeruj macierz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wypisz spiralnie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Klepsydra o największej sumie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Obróć o 90 stopni.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/13_listy_2d/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/13_listy_2d/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/13_listy_2d/zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Gra w statki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/13_listy_2d/zad11.py">Python</a></td>
            <td><a>Cpp</a></td>
            <td><a>Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Iloczyn wielomianu przez skalar.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma wielomianów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Mnożenie wielomianów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>N-ta pochodna wielomianu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad5">Java</a></td>
            <td><a href="https://github.com/dje/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Miejsce zerowe funkcji kwadratowej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/14_funkcje_wielomiany/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/14_funkcje_wielomiany/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/14_funkcje_wielomiany/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/14_funkcje_wielomiany/zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Suma liczb naturalnych mniejszych od *N*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Potęgowanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Silnia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Liczba Fibonacciego.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>*N*-ty wyraz ciągu danego wzorem rekurencyjnym.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Wyszukiwanie liniowe rekurencyjnie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad7.py">Python</a></td>
            <td><a>Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wieża Hanoi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Słowa elfickie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Gra.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/15_funkcje_rekurencja/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/15_funkcje_rekurencja/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/15_funkcje_rekurencja/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/15_funkcje_rekurencja/zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Konwersja gdy spełniony jest warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Operacje arytmetyczne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zera/jedynki w liczbie binarnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Min/maks z dwóch liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Konwersja między dowolnymi systemami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Zamiana sąsiadów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Następna potęga dwójki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad8">Java</a></td>
            <td><a href="https://github.com/dje/Nauka-programowania/blob/master/src/js/16_system_binarny/zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Zmiana wielkości liter.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Zamień *A* w *B*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Czy liczba jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad11.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Najdłuższy ciąg zer w liczbie binarnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/16_system_binarny/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/16_system_binarny/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/16_system_binarny/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/16_system_binarny/zad12.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Kluczami są elementy jednej listy, a wartościami elementy drugiej listy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Klucz to imię, wartość lista wypożyczonych książek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Usuń ze słownika.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Lista pracowników.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Histogram znaków w słowie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Histogram słów w tekście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Najczęściej występująca litera w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Powtarzające się znaki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Anagramy w tekście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Sortowanie względem kluczy/wartości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad11.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Czy słowniki są identyczne?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/17_slowniki/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/17_slowniki/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/17_slowniki/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/17_slowniki/zad12.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Znajdź w folderze wszystkie pliki z danym rozszerzeniem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Znajdź ścieżkę pliku o danej nazwie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wczytaj i wypisz treść pliku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Plik z listą adresów ip.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Statystyki dla pliku tekstowego.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dodaj wiersz do pliku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Znajdź i zmodyfikuj pliki spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń pliki spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Skopiuj pliki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad10.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Podmień treści.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad11.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Przesuń wszystkie pliki csv do jednego folderu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/18_operacje_na_plikach/zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/18_operacje_na_plikach/zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/18_operacje_na_plikach/zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/18_operacje_na_plikach/zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/18_operacje_na_plikach/zad12.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zaprojektuj klasę *Punkt*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Prostokąt powstały z nałożenia się dwóch prostokątów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zaprojektuj klasy *Wektor2d* oraz *Wektor3D*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zaprojektuj klasę *Zespolona*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zaprojektuj klasę *Macierz.*</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Znajdź liczbę instancji klasy w programie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/19_klasy/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/19_klasy/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/19_klasy/zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/19_klasy/zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_dziedziczenie/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_dziedziczenie/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_dziedziczenie/zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_dziedziczenie/zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zaprojektuj klasę bazową *Kształt* oraz klasy potomne *Koło* i *Kwadrat*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_dziedziczenie/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_dziedziczenie/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_dziedziczenie/zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_dziedziczenie/zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Polimorfizm.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_dziedziczenie/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_dziedziczenie/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_dziedziczenie/zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_dziedziczenie/zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dziedziczenie wielopoziomowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_dziedziczenie/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_dziedziczenie/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_dziedziczenie/zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_dziedziczenie/zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Dziedziczenie wielokrotne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/20_dziedziczenie/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/20_dziedziczenie/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/20_dziedziczenie/zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/js/20_dziedziczenie/zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Sortowanie przez wybieranie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad2.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sortowanie przez wstawianie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad3.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Sortowanie przez scalanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad4.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie szybkie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/21_sortowanie_algorytmy/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/21_sortowanie_algorytmy/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/21_sortowanie_algorytmy/zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/21_sortowanie_algorytmy/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/rust/21_sortowanie_algorytmy/zad5.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Posortuj słowa w zdaniu</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Posortuj listę par względem jednej z kategorii.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Posortuj względem długości napisy w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie listy obiektów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad5.sh">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Tablica binarna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Tablica składająca się wyłącznie z zer, jedynek i dwójek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Tablica cykliczna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/22_sortowanie_praktyka/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/22_sortowanie_praktyka/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/22_sortowanie_praktyka/zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/22_sortowanie_praktyka/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Sprawdź poprawność hasła.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy napis składa się wyłącznie z cyfr?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Czy słowo należy do zdania?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Odfiltruj cyfry z tekstu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Wiersze kończące się napisem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Podziel względem znaków interpunkcyjnych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Cyfry będące częścią słów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń część wiersza.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad9">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Podmień napisy z listy *A* na napisy z listy *B*.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad10">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad10.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Nazwa pliku ze ścieżki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/23_wyrazenia_regularne/zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/23_wyrazenia_regularne/zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/23_wyrazenia_regularne/zad11">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/bash/23_wyrazenia_regularne/zad11.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Przesuń zera.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Trójka o minimalnym iloczynie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wspólny podciąg o największej sumie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zbiór potęgowy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>*M* posortowanych list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Woda.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Sznurek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Najdłuższy naprzemienny podciąg.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/24_listy_trudne/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/24_listy_trudne/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/24_listy_trudne/zad9">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Usuń wszystkie wystąpienia podnapisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy napis *A* stanowi początek napisu *B*?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td>
                <aListy - trudne>Haskell</a>
            </td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Usuń powtórzenia z napisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Znaki stojące obok siebie nie mogą się powtarzać.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Czy napisy są swoimi rotacjami?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Znajdź powtórzenia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Najdłuższy wspólny przedrostek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Najdłuższy wspólny potomek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/python/25_napisy_trudne/zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/cpp/25_napisy_trudne/zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/java/25_napisy_trudne/zad9">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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

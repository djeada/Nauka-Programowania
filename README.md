<div align="center">
  
<a href="https://github.com/djeada/Nauka-programowania/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/djeada/Nauka-programowania"></a>
<a href="https://github.com/djeada/Nauka-programowania/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/djeada/Nauka-programowania"></a>
<a href="https://github.com/djeada/Nauka-programowania/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/djeada/Nauka-programowania"></a>
<a href=""><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
</div>

# Nauka-programowania
Jeśli chcesz nauczyć się programować, ale nie wiesz od czego zacząć, to trafiłeś we właściwe miejsce. Nasz projekt zawiera zestaw zadań, które przeprowadzą Cię przez wszystkie potrzebne do zrozumienia koncepcje programowania.

## Gdzie mogę znaleźć dodatkowe materiały do nauki?

Materiały dodatkowe, takie jak notatki z Python i C++, są dostępne na naszych osobnych repozytoriach na GitHubie:

* <a href="https://github.com/djeada/Kurs-podstaw-Pythona">Notatki Python.</a>  
* <a href="https://github.com/djeada/C-and-Cpp">Notatki C++.</a> 

# Zbiór zadań

* Aktualny zbiór zadań znajdziesz pod tym <a href="https://github.com/djeada/Nauka-Programowania/tree/master/zbior_zadan">linkiem</a>. </br>
* Zbiór będzie poszerzany i aktualizowany.
* Więcej informacji na temat tego jak dodać własne rozwiązania, znajdziesz na <a href="https://github.com/djeada/Nauka-Programowania/blob/master/CONTRIBUTING.md">tej stronie</a>.

## O zadaniach
Zadania są podzielone tematycznie i uporządkowane według stopnia zaawansowania. Przygotowaliśmy je tak, by każdy, nawet początkujący uczeń, mógł przećwiczyć podstawowe koncepcje programowania. W przeciwieństwie do wielu innych kursów, które szybko przechodzą do bardziej zaawansowanych mechanizmów, nasze zadania skupiają się głównie na podstawach.

* Pierwsze 8 rozdziałów poświęcone są najbardziej podstawowym koncepcjom, takim jak zmienna, warunek i pętla. Rozwiązania powinny być sprawdzane ręcznie poprzez komunikację z programem za pomocą konsoli. Dane wpisywane są z klawiatury, a wynik wyświetlany na ekranie.
* W rozdziałach 9-17 znajdują się zadania wymagające zrozumienia koncepcji z pierwszych 8 rozdziałów oraz rozszerzające je o zagadnienia takie jak struktury danych, rekurencja i binarna reprezentacja liczb. Osoba rozwiązująca zadania powinna przygotować automatyczne testy dla swojego rozwiązania, uwzględniając wszystkie skrajne przypadki.
* W rozdziałach 18-25 poruszone są bardziej zaawansowane tematy, takie jak praca z plikami, algorytmy sortowania i obsługa błędów. Zadania te wymagają już bardziej zaawansowanej wiedzy i umiejętności, a także znajomości narzędzi takich jak debugowanie i profilowanie kodu. Zadania te wymagają już dużej samodzielności i umiejętności samodzielnego poszukiwania informacji oraz rozwiązywania problemów.

Przykładowe rozwiązania powinny być traktowane jako wskazówki, a nie jako jedyne słuszne sposoby rozwiązania zadania. W szczególności w dalszych rozdziałach, dane zadanie może mieć wiele różnych sposobów rozwiązania. Część przykładowych rozwiązań może zawierać nawet więcej niż jeden wariant rozwiązania. Alternatywne rozwiązania mogą różnić się między sobą pod względem złożoności czasowej, pamięciowej lub użycia funkcji języka.

Pamiętaj, że nauka programowania to długi proces, ale z naszym zbiorem zadań i dodatkowymi materiałami, powinieneś być w stanie zbudować solidne podstawy i cieszyć się rozwijającą się karierą w branży IT.

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

Rozwiązania zostały przetestowane i dostosowane do środowiska `NodeJS 12.16.1`. Skrypty języka JavaScript nie wymagają kompilacji - aby uruchomić skrypt, należy użyć komendy `node sciezka_do_zadania.js`.Do formatowania kodu należy użyć narzędzia `js-beautify` z flagami: `js-beautify -r sciezka_do_zadania.js`. Przykłady wymagają zainstalowania biblioteki `readline` do komunikacji z konsolą.

### Haskell

Przykłady zostały przetestowane i dostosowane do wersji `GHC 8.10.2`. Aby skompilować przykłady z tego języka, należy użyć kompilatora `ghc` z flagami: `ghc -O2 -threaded -rtsopts -eventlog sciezka_do_zadania.hs -o plik_wykonywalny`. Do formatowania kodu należy użyć narzędzia `ormolu` z flagami: `ormolu --mode inplace sciezka_do_zadania.hs`. Przykłady nie używają bibliotek zewnętrznych.

### Rust

Przykłady zostały przetestowane i dostosowane do wersji `1.42.0`. Aby skompilować przykłady z tego języka, należy użyć kompilatora `rustc` bez flag: `rustc sciezka_do_zadania.rs`. Do formatowania kodu należy użyć narzędzia `rustfmt` z flagami: `rustfmt --write-mode=overwrite sciezka_do_zadania.rs`. Przykłady nie używają bibliotek zewnętrznych.

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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/01_Interakcja_z_konsola/Zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zamiana kolejności.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/01_Interakcja_z_konsola/Zad2.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Narysuj kształt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/01_Interakcja_z_konsola/Zad3.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Operacje arytmetyczne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/01_Interakcja_z_konsola/Zad4.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Wartość funkcji w punkcie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zamiana jednostek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pola figur i objętości brył.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Cena podłogi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/01_Interakcja_z_konsola/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Kalkulator kredytowy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/01_Interakcja_z_konsola/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/01_Interakcja_z_konsola/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/01_Interakcja_z_konsola/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/01_Interakcja_z_konsola/Zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Porównanie ze zmienną.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Znak liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Maks/min dwóch liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie trzech liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Maks czterech liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dowody praw logicznych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Warunek trójkąta.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/02_Instrukcje_sterujace/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/02_Instrukcje_sterujace/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/02_Instrukcje_sterujace/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/02_Instrukcje_sterujace/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/02_Instrukcje_sterujace/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad1/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Czy osoba jest pełnoletnia?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad2/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Rok przestępny.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad3/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dzień tygodnia odpowiadający danej liczbie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad4/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Ile dni ma miesiąc?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad5/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Poprawność daty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad6/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Ile dni minęło od początku roku?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad7/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Jaki mamy dzień tygodnia?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/03_Daty/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/03_Daty/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/03_Daty/Zad8/Main.java">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/03_Daty/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/03_Daty/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Liczby mniejsze od podanej liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Liczba <i>Pi</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Suma liczb mniejszych od liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Liczby z przedziału.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Suma wyrazów ciągu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Liczba <i>Pi</i> podniesiona do potęgi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Znajdź liczbę kur oraz owieczek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/04_Petla_wprowadzenie/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/04_Petla_wprowadzenie/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/04_Petla_wprowadzenie/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/04_Petla_wprowadzenie/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/04_Petla_wprowadzenie/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/05_Petla_wyznaczanie_cyfr_liczby/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/05_Petla_wyznaczanie_cyfr_liczby/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/05_Petla_wyznaczanie_cyfr_liczby/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/05_Petla_wyznaczanie_cyfr_liczby/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/05_Petla_wyznaczanie_cyfr_liczby/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Cyfry, z których składa się liczba.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/05_Petla_wyznaczanie_cyfr_liczby/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/05_Petla_wyznaczanie_cyfr_liczby/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/05_Petla_wyznaczanie_cyfr_liczby/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/05_Petla_wyznaczanie_cyfr_liczby/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/05_Petla_wyznaczanie_cyfr_liczby/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma cyfr liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/05_Petla_wyznaczanie_cyfr_liczby/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/05_Petla_wyznaczanie_cyfr_liczby/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/05_Petla_wyznaczanie_cyfr_liczby/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/05_Petla_wyznaczanie_cyfr_liczby/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/05_Petla_wyznaczanie_cyfr_liczby/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Cyfry liczby spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/05_Petla_wyznaczanie_cyfr_liczby/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/05_Petla_wyznaczanie_cyfr_liczby/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/05_Petla_wyznaczanie_cyfr_liczby/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/05_Petla_wyznaczanie_cyfr_liczby/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/05_Petla_wyznaczanie_cyfr_liczby/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Czy liczba jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/05_Petla_wyznaczanie_cyfr_liczby/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/05_Petla_wyznaczanie_cyfr_liczby/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/05_Petla_wyznaczanie_cyfr_liczby/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/05_Petla_wyznaczanie_cyfr_liczby/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/05_Petla_wyznaczanie_cyfr_liczby/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Wszystkie liczby spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/05_Petla_wyznaczanie_cyfr_liczby/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/05_Petla_wyznaczanie_cyfr_liczby/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/05_Petla_wyznaczanie_cyfr_liczby/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/05_Petla_wyznaczanie_cyfr_liczby/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/05_Petla_wyznaczanie_cyfr_liczby/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Operacja arytmetyczna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sprawdź warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Maks i min.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zamień wartości miejscami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Cyfry liczby.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Hasło.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Zaokrąglanie w dół.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/06_Funkcje_wprowadzenie/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/06_Funkcje_wprowadzenie/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/06_Funkcje_wprowadzenie/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/06_Funkcje_wprowadzenie/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/06_Funkcje_wprowadzenie/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
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
            <td>Średnia z <i>n</i> liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Podnieś <b>a</b> do <b>b</b>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Mnożenie i dzielenie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Silnia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>NWD.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>NWW.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pierwiastek metodą Newtona.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Naiwny test pierwszości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/07_Petla_algorytmy_matematyczne/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/07_Petla_algorytmy_matematyczne/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/07_Petla_algorytmy_matematyczne/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/07_Petla_algorytmy_matematyczne/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/07_Petla_algorytmy_matematyczne/Zad8.sh">Bash</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Trójkąt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Odwrócony trójkąt.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Tabliczka mnożenia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Litera <i>X</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Litera <i>Z</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Choinka.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/08_Petle_zagniezdzone/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Trójkąt Pascala.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td><i>N</i> pierwszych liczb pierwszych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/08_Petle_zagniezdzone/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/08_Petle_zagniezdzone/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/08_Petle_zagniezdzone/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/08_Petle_zagniezdzone/Zad9.js">JavaScript</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Wczytaj, zmodyfikuj i wypisz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Pierwsze wystąpienie klucza.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Minimum oraz maksimum.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zmodyfikuj elementy spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Czy średnia elementów znajduje się w liście?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Liczba mniejsza od największej i większa od wszystkich pozostałych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Usuń klucz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad9.py">Usuń duplikaty.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Czy punkty mogą stanowić wierzchołki trójkąta?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad10.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Samochody.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad11.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Rotacja w lewo/prawo.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad12.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>13</td>
            <td>Brakujący element w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad13.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad13.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad13">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad13.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad13.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>14</td>
            <td>Element bez pary w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad14.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad14.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad14">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad14.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad14.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>15</td>
            <td>Element dominujący.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad15.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad15.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad15">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad15.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad15.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>16</td>
            <td>Suma dwóch.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad16.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad16.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad16">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad16.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad16.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>17</td>
            <td>Pary, których suma jest równa liczbie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad17.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad17">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad17.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad17.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>18</td>
            <td>Lista posortowane została przesunięta.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/09_Listy_wprowadzenie/Zad18.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/09_Listy_wprowadzenie/Zad18.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/09_Listy_wprowadzenie/Zad18">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/09_Listy_wprowadzenie/Zad18.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/09_Listy_wprowadzenie/Zad18.sh">Bash</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Połączenie list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Mnożenie wektorowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Średnia ważona wartości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Część wspólna dwóch list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Różnica między dwoma listami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Połącz posortowane listy w posortowaną listę.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń z pierwszej listy część wspólną obu list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Znajdź medianę dwóch posortowanych list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/10_Listy_dwie_listy/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/10_Listy_dwie_listy/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/10_Listy_dwie_listy/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/10_Listy_dwie_listy/Zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/10_Listy_dwie_listy/Zad10.sh">Bash</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Policz wystąpienia znaku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Z ilu słów składa się zdanie?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad3">Java</a></td>
            <td><a href="https://github.com/djea/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zamień wszystkie małe litery na wielkie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Napisy_wprowadzenie/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Wypisz poziomo i pionowo co <i>k</i>-ty znak napisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zamień litery <i>a</i> na znaki zapytania.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Zamień znaki na numery ASCII.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wypisz pionowo słowa, z których składa się zdanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad8">Java</a></td>
            <td><a href="https://github.com/djea/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Wczytaj i rozdziel informacje o pracowniku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Znajdź najdłuższe/najkrótsze słowo w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad10.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Średnia długość słów w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad11.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Usuń spacje ze zdania.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad12.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>13</td>
            <td>Znaki znajdujące się na pozycjach będących liczbami pierwszymi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad13.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Napisy_wprowadzenie/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad13">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad13.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad13.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>14</td>
            <td>Napis składający się z liczb od 1 do <i>n</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad14.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad14.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad14">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad14.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad14.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>15</td>
            <td>Słowa ze zdania jako osobne elementy listy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad15.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad15.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad15">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad15.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad15.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>16</td>
            <td>Odległość Hamminga.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad16.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad16.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad16">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad16.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad16.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>17</td>
            <td>Zamień listę na napis.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad17.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad17.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad17">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad17.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad17.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>18</td>
            <td>Odwróć napisy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/11_Napisy_wprowadzenie/Zad18.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/11_Napisy_wprowadzenie/Zad18.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/11_Napisy_wprowadzenie/Zad18">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/11_Napisy_wprowadzenie/Zad18.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/11_Napisy_wprowadzenie/Zad18.sh">Bash</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Wszystkie permutacje słowa.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy słowa są swoimi anagramami?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wszystkie palindromy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Znajdź anagramy w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Permutacja będąca palindromem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dla dwóch słów, ile minimalnie znaków musimy usunąć aby uzyskać anagramy?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wyjątkowe palindromy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/12_Napisy_anagramy_palindromy/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/12_Napisy_anagramy_palindromy/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/12_Napisy_anagramy_palindromy/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/12_Napisy_anagramy_palindromy/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/12_Napisy_anagramy_palindromy/Zad8.sh">Bash</a></td>
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
            <td>Macierz <i>a</i> identycznych wierszy składających się z liczb od 0 do <i>b</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Każdy element jest iloczynem współrzędnych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Macierz z par odpowiadających sobie elementów dwóch list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dodawanie/odejmowanie macierzy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Magiczny kwadrat.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Pokrywające się przedziały w liście przedziałów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Wyzeruj macierz.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wypisz spiralnie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Klepsydra o największej sumie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Obróć o 90 stopni.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/13_Listy_2d/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/13_Listy_2d/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/13_Listy_2d/Zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Gra w statki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/13_Listy_2d/Zad11.py">Python</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/14_Funkcje_wielomiany/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/14_Funkcje_wielomiany/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/14_Funkcje_wielomiany/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/14_Funkcje_wielomiany/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Iloczyn wielomianu przez skalar.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/14_Funkcje_wielomiany/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/14_Funkcje_wielomiany/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/14_Funkcje_wielomiany/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/14_Funkcje_wielomiany/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Suma wielomianów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/14_Funkcje_wielomiany/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/14_Funkcje_wielomiany/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/14_Funkcje_wielomiany/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/14_Funkcje_wielomiany/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Mnożenie wielomianów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/14_Funkcje_wielomiany/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/14_Funkcje_wielomiany/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/14_Funkcje_wielomiany/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/14_Funkcje_wielomiany/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>N-ta pochodna wielomianu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/14_Funkcje_wielomiany/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/14_Funkcje_wielomiany/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/14_Funkcje_wielomiany/Zad5">Java</a></td>
            <td><a href="https://github.com/dje/Nauka-programowania/blob/master/src/JavaScript/14_Funkcje_wielomiany/Zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Miejsce zerowe funkcji kwadratowej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/14_Funkcje_wielomiany/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/14_Funkcje_wielomiany/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/14_Funkcje_wielomiany/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/14_Funkcje_wielomiany/Zad6.js">JavaScript</a></td>
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
            <td>Liczby naturalne mniejsze od <i>N</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Suma liczb naturalnych mniejszych od <i>N</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Potęgowanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Silnia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Liczba Fibonacciego.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td><i>N</i>-ty wyraz ciągu danego wzorem rekurencyjnym.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Wyszukiwanie liniowe rekurencyjnie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad7.py">Python</a></td>
            <td><a>Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Wieża Hanoi.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Słowa elfickie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Gra.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/15_Funkcje_rekurencja/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/15_Funkcje_rekurencja/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/15_Funkcje_rekurencja/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/15_Funkcje_rekurencja/Zad10.js">JavaScript</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Konwersja gdy spełniony jest warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Operacje arytmetyczne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zera/jedynki w liczbie binarnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Min/maks z dwóch liczb.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Konwersja między dowolnymi systemami.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Zamiana sąsiadów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Następna potęga dwójki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad8">Java</a></td>
            <td><a href="https://github.com/dje/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Zmiana wielkości liter.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Zamień <i>A</b> w <b>B</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Czy liczba jest palindromem?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad11.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Najdłuższy ciąg zer w liczbie binarnej.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/16_System_binarny/Zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/16_System_binarny/Zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/16_System_binarny/Zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/16_System_binarny/Zad12.js">JavaScript</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Kluczami są elementy jednej listy, a wartościami elementy drugiej listy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Klucz to imię, wartość lista wypożyczonych książek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Usuń ze słownika.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Lista pracowników.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Histogram znaków w słowie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Histogram słów w tekście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad7.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Najczęściej występująca litera w zdaniu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad8.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Powtarzające się znaki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad9.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Anagramy w tekście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad10.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Sortowanie względem kluczy/wartości.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad11.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Czy słowniki są identyczne?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/17_Slowniki/Zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/17_Slowniki/Zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/17_Slowniki/Zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/17_Slowniki/Zad12.js">JavaScript</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad1.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Znajdź w folderze wszystkie pliki z danym rozszerzeniem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad2.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Znajdź ścieżkę pliku o danej nazwie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad3.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wczytaj i wypisz treść pliku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad4.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Plik z listą adresów ip.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad5.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Statystyki dla pliku tekstowego.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad6.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Dodaj wiersz do pliku.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad7.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Znajdź i zmodyfikuj pliki spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad8">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad8.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń pliki spełniające warunek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad9">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad9.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Skopiuj pliki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad10">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad10.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad10.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Podmień treści.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad11">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad11.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad11.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Przesuń wszystkie pliki csv do jednego folderu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/18_Operacje_na_plikach/Zad12.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/18_Operacje_na_plikach/Zad12.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/18_Operacje_na_plikach/Zad12">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/18_Operacje_na_plikach/Zad12.js">JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/18_Operacje_na_plikach/Zad12.sh">Bash</a></td>
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
            <td>Zaprojektuj klasę <i>Koło</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zaprojektuj klasę <i>Punkt</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Prostokąt powstały z nałożenia się dwóch prostokątów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Zaprojektuj klasy <i>Wektor2d</i> oraz <i>Wektor3D</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zaprojektuj klasę <i>Zespolona</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad5.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Zaprojektuj klasę <i>Macierz.</i></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad6">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad6.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Znajdź liczbę instancji klasy w programie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/19_Klasy/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/19_Klasy/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/19_Klasy/Zad7">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/19_Klasy/Zad7.js">JavaScript</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/20_Dziedziczenie/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/20_Dziedziczenie/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/20_Dziedziczenie/Zad1">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/20_Dziedziczenie/Zad1.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Zaprojektuj klasę bazową <i>Kształt</i> oraz klasy potomne <i>Koło</i> i <i>Kwadrat</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/20_Dziedziczenie/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/20_Dziedziczenie/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/20_Dziedziczenie/Zad2">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/20_Dziedziczenie/Zad2.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Polimorfizm.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/20_Dziedziczenie/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/20_Dziedziczenie/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/20_Dziedziczenie/Zad3">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/20_Dziedziczenie/Zad3.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dziedziczenie wielopoziomowe.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/20_Dziedziczenie/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/20_Dziedziczenie/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/20_Dziedziczenie/Zad4">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/20_Dziedziczenie/Zad4.js">JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Dziedziczenie wielokrotne.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/20_Dziedziczenie/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/20_Dziedziczenie/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/20_Dziedziczenie/Zad5">Java</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/JavaScript/20_Dziedziczenie/Zad5.js">JavaScript</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/21_Sortowanie_algorytmy/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/21_Sortowanie_algorytmy/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/21_Sortowanie_algorytmy/Zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/21_Sortowanie_algorytmy/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/21_Sortowanie_algorytmy/Zad1.rs">Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Sortowanie przez wybieranie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/21_Sortowanie_algorytmy/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/21_Sortowanie_algorytmy/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/21_Sortowanie_algorytmy/Zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/21_Sortowanie_algorytmy/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/21_Sortowanie_algorytmy/Zad2.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sortowanie przez wstawianie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/21_Sortowanie_algorytmy/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/21_Sortowanie_algorytmy/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/21_Sortowanie_algorytmy/Zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/21_Sortowanie_algorytmy/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/21_Sortowanie_algorytmy/Zad3.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Sortowanie przez scalanie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/21_Sortowanie_algorytmy/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/21_Sortowanie_algorytmy/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/21_Sortowanie_algorytmy/Zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/21_Sortowanie_algorytmy/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/21_Sortowanie_algorytmy/Zad4.rs">Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie szybkie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/21_Sortowanie_algorytmy/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/21_Sortowanie_algorytmy/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/21_Sortowanie_algorytmy/Zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/21_Sortowanie_algorytmy/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Rust/21_Sortowanie_algorytmy/Zad5.rs">Rust</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Posortuj słowa w zdaniu</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Posortuj listę par względem jednej z kategorii.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Posortuj względem długości napisy w liście.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Sortowanie listy obiektów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad5.sh">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Tablica binarna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Tablica składająca się wyłącznie z zer, jedynek i dwójek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Tablica cykliczna.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/22_Sortowanie_praktyka/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/22_Sortowanie_praktyka/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/22_Sortowanie_praktyka/Zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/22_Sortowanie_praktyka/Zad8.sh">Bash</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad1.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Sprawdź poprawność hasła.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad2.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy napis składa się wyłącznie z cyfr?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad3.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Czy słowo należy do zdania?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad4.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Odfiltruj cyfry z tekstu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad5.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Wiersze kończące się napisem.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad6.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Podziel względem znaków interpunkcyjnych.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad7.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★☆☆</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Cyfry będące częścią słów.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad8.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Usuń część wiersza.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad9">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad9.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Podmień napisy z listy <i>A</i> na napisy z listy <i>B</i>.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad10.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad10.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad10">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad10.sh">Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Nazwa pliku ze ścieżki.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/23_Wyrazenia_regularne/Zad11.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/23_Wyrazenia_regularne/Zad11.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/23_Wyrazenia_regularne/Zad11">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Bash/23_Wyrazenia_regularne/Zad11.sh">Bash</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Przesuń zera.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Trójka o minimalnym iloczynie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad3">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Wspólny podciąg o największej sumie.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Zbiór potęgowy.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>6</td>
            <td><b>M</b> posortowanych list.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Woda.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Sznurek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Najdłuższy naprzemienny podciąg.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/24_Listy_trudne/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/24_Listy_trudne/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/24_Listy_trudne/Zad9">Java</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad1.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad1.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad1">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Usuń wszystkie wystąpienia podnapisu.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad2.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad2.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad2">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★☆</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Czy napis <b>A</b> stanowi początek napisu <b>B</b>?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad3.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad3.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad3">Java</a></td>
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
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad4.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad4.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad4">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Znaki stojące obok siebie nie mogą się powtarzać.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad5.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad5.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad5">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Czy napisy są swoimi rotacjami?</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad6.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad6.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad6">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Znajdź powtórzenia.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad7.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad7.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad7">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Najdłuższy wspólny przedrostek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad8.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad8.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad8">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Najdłuższy wspólny potomek.</td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Python/25_Napisy_trudne/Zad9.py">Python</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Cpp/25_Napisy_trudne/Zad9.cpp">Cpp</a></td>
            <td><a href="https://github.com/djeada/Nauka-programowania/blob/master/src/Java/25_Napisy_trudne/Zad9">Java</a></td>
            <td><a>JavaScript</a></td>
            <td><a>Bash</a></td>
            <td><a>Haskell</a></td>
            <td><a>Rust</a></td>
            <td>★★★</td>
        </tr>
    </tbody>
</table>

## Literatura

* Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. "<i>Introduction to Algorithms, 3rd Edition (The MIT Press)</i>"
* Steven Halim "<i>Competitive Programming 3</i>" 
* Narasimha Karumanchi "<i>Data Structures and Algorithms Made Easy: Data Structures and Algorithmic Puzzles</i>" 
* Brian Kernighan, Dennis Ritchie "<i>The C Programming Language</i>" 
* Steven Skiena, Miguel Revilla "<i>Programming Challenges: The Programming Contest Training Manual</i>" 
* Antti Laaksonen "<i>  Guide to Competitive Programming: Learning and Improving Algorithms Through Contests (Undergraduate Topics in Computer Science) </i>" 
* Nite Nimajneb "<i>The Hitchhiker’s Guide to the Programming Contests</i>" 

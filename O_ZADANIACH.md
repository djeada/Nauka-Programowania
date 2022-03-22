## Ogólnie
Zadania podzielone są tematycznie, a kolejne rozdziały uporządkowane są względem stopnia zaawansowania. Treści zadań zostały przygotowane w taki sposób, by każdy nawet najbardziej oporny uczeń był w stanie przećwiczyć wszystkie podstawowe koncepcje programowania. W odróżnieniu od wielu innych kursów, które starają się jak najszybciej przejść do bardziej zaawansowanych mechanizmów programowania, zadania te kładą nacisk przede wszystkim na podstawy.

* Pierwsze 8 rozdziałów ma na celu przećwiczenie najbardziej elementarnych koncepcji jak zmienna, warunek oraz pętla. Rozwiązania powinny być przez rozwiązującego sprawdzone manualnie poprzez komunikacje z programem za pomocą konsoli. Dane wpisywane są z klawiatury, a wynik wyświetlany jest na ekranie.
* Rozdziały 9-17 zawierają zadania wymagające zrozumienia koncepcji z pierwszych 8 rozdziałów oraz poszerzające je o zagadnienia struktur danych, rekurencji oraz binarnej reprezentacji liczb. Rozwiązujący powinien samodzielnie przygotować automatyczne testy dla swojego rozwiązania wraz z uwzględnieniem wszystkich warunków brzegowych.
* W rozdziały 18-25 poruszone są bardziej zaawansowane tematy. Ćwiczona jest praca z plikami, algorytmy sortowania oraz podstawy programowania obiektowego.

Przykładowe rozwiązania należy traktować jako wskazówki. W szczególności w dalszych rozdziałach dane zadanie może być rozwiązane na wiele sposobów. Część przykładowych rozwiązań może zawierać więcej niż jeden wariant rozwiązania. Alternatywne rozwiązania różnią się złożonością czasową, bądź pamięciową lub użyciem funkcji języka.

## Wspierane wersje języków

Przykłady zostały przetestowane w następujących wersjach języków:

### C++

Większość przykładów wykorzystuje standard C++11. Część zadań została rozwiązana przy użyciu składni wprowadzonej w wersjach C++17 i C++20.

#### Komenda kompilacji

Do kompilacji wykorzystano kompilator GCC z następującymi flagami:

g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra -pedantic -o plik_wykonwyalny.out sciezka_do_zadania.cpp

#### Styl formatowania

Do formatowania kodu zostało użyte narzędzie `clang-format`.

    clang-format -i -style=file sciezka_do_zadania.cpp

#### Zależności od bibliotek zewnętrznych

Brak.

### Python

Wszystkie przykłady zostały przetestowane w wersji 3.8. 

#### Komenda kompilacji

Skrypty języka Python nie były kompilowane. Do uruchomienia skryptów użyto następującej komendy:

    python3 sciezka_do_zadania.py

#### Styl formatowania

Do formatowania kodu zostało użyte narzędzie `black`.

    black sciezka_do_zadania.py

#### Zależności od bibliotek zewnętrznych

Brak.

### Java
    
Wszystkie przykłady zostały przetestowane w wersji Java SE 17.

#### Komenda kompilacji

Do kompilacji wykorzystano kompilator javac z następującymi flagami:

    javac -d . sciezka_do_zadania.java

#### Styl formatowania

Do formatowania kodu zostało użyte narzędzie google-java-format.

    java -jar google-java-format-1.7-all-deps.jar sciezka_do_zadania.java

#### Zależności od bibliotek zewnętrznych

Brak.

### JavaScript

Rozwiązania zostały przetestowane w środowisku NodeJS 12.16.1.

#### Zależności od bibliotek zewnętrznych

Do komunikacji z konsolą użyto biblioteki <a href="https://github.com/maleck13/readline">`readline`</a>.

### Haskell

Wszystkie przykłady zostały przetestowane w wersji Haskell 8.4.

#### Komenda kompilacji

Do kompilacji wykorzystano kompilator ghc z następującymi flagami:
    
        ghc -O2 -Wall -o sciezka_do_zadania sciezka_do_zadania.hs

#### Styl formatowania

Do formatowania kodu zostało użyte narzędzie ormolu.

    ormolu --mode inplace sciezka_do_zadania.hs

#### Zależności od bibliotek zewnętrznych

Brak.

### Rust

Wszystkie przykłady zostały przetestowane w wersji Rust 1.42.0.

#### Komenda kompilacji

Do kompilacji wykorzystano kompilator rustc z następującymi flagami:

    rustc -O --emit=asm --target=x86_64-unknown-linux-gnu -o sciezka_do_zadania sciezka_do_zadania.rs

#### Styl formatowania

Do formatowania kodu zostało użyte narzędzie rustfmt.

    rustfmt --write-mode=overwrite sciezka_do_zadania.rs

#### Zależności od bibliotek zewnętrznych

Brak.

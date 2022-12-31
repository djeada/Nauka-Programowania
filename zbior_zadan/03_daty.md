## Daty

### Zad 1. (★☆☆)

Tytuł: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiąca?

Treść: Wypisz pobraną od użytkownika liczbę naturalną, jeśli jest ona poprawnym numerem dnia tygodnia lub miesiąca.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

* Dla pobranej liczby: 10, powinna zostać wypisana liczba: 10.
* Dla pobranej liczby: 15, nie powinna być wypisana żadna liczba.

### Zad 2. (★☆☆)

Tytuł: Czy osoba jest pełnoletnia?

Treść: Dla pobranych sześciu liczb: dnia urodzenia osoby, miesiąca urodzenia osoby, roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiąca i aktualnego roku, sprawdź czy dana osoba jest pełnoletnia.

Dane wejściowe: 6 liczb.

Dane wyjściowe: Komunikat.

Przykład:

Dla pobranych liczb: 5, 12, 1999, 20, 11, 2020, powinna zostać wypisana informacja o pełnoletności osoby.

### Zad 3. (★☆☆)

Tytuł: Rok przestępny.

Treść: Napisz program, który dla pobranej liczby naturalnej będzie sprawdzał, czy dany rok jest przestępny.

Podpowiedź: Rok przestępny jest podzielny przez 4, ale nie jest podzielny przez 100, chyba że jest podzielny przez 400.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat o tym, czy rok jest przestępny, czy też nie.

Przykład:

Dla pobranej liczby 2100, program powinien wypisać informację, że rok nie jest przestępny.

### Zad 4. (★☆☆)

Tytuł: Dzień tygodnia odpowiadający danej liczbie.

Treść: Napisz program, który dla pobranej liczby naturalnej będzie wypisywał dzień tygodnia odpowiadający tej liczbie. Jeśli otrzymano liczbę niedodatnią bądź dodatnią większą niż 7, program powinien wypisać komunikat informujący użytkownika, że liczba jest niepoprawna.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat o dniu tygodnia.

Przykład:

Dla pobranej liczby 2, program powinien wypisać napis "Wtorek".

### Zad 5. (★☆☆)

Tytuł: Ile dni ma miesiąc?

Treść: Napisz program, który dla pobranej liczby naturalnej będzie wypisywał liczbę dni w miesiącu odpowiadającemu tej liczbie. Jeśli pobrana liczba nie jest poprawnym numerem miesiąca, program powinien poinformować o tym użytkownika.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla pobranej liczby 1, program powinien zwrócić liczbę 31.

### Zad 6. (★★☆)

Tytuł: Poprawność daty.	

Treść: Napisz program, który dla pobranych trzech liczb naturalnych sprawdzi, czy reprezentują one poprawną datę. Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem.

Podpowiedź: Wszystkie liczby nie mogą być mniejsze od 1. Druga liczba nie może być większa niż 12 itd.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Komunikat o poprawności lub niepoprawności daty.

Przykład:

Dla pobranych liczb 2, 1 i 4, program powinien wypisać informację o poprawności daty.

### Zad 7. (★★☆)

Tytuł: Ile dni minęło od początku roku?	

Treść: Dla trzech pobranych liczb: reprezentujących datę wypisz, ile dni minęło od początku roku. Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem. 

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostać zwrócona liczba 45. **

### Zad 8. (★★☆)

Tytuł: Jaki mamy dzień tygodnia?	

Treść: Napisz program, który dla trzech pobranych liczb naturalnych (reprezentujących datę) będzie wypisywał odpowiadający im dzień tygodnia. Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem.

Podpowiedź: Można użyć wzoru Gaussa:
Niech data będzie dana w formacie DD/MM/CCYY :

* DD - dzień
* MM - miesiąc
* CC - stulecie
* YY - rok

$$A = CC/4 - 2CC - 1$$

$$B = 5YY/4$$

$$C = 26*(MM + 1)/10$$

$$Dzien = (A + B + C + DD) mod 7$$

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Komunikat o dniu tygodnia.

Przykład:

Dla pobranych liczb 9, 10 i 2020, program powinien zwrócić napis "Czwartek".

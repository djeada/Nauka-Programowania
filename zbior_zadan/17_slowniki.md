## Słowniki

### Zad 1. (★☆☆)

Tytuł: Kluczami są liczby, a wartościami ich kwadraty.

Treść: Otrzymujesz liczbę naturalną. Zbuduj słownik składający się z kluczy będących kolejnymi liczbami naturalnymi mniejszymi od otrzymanej liczby oraz wartości będących kwadratami odpowiadających im kluczy.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Słownik par: liczba naturalna, liczba naturalna.

Przykład:

Dla otrzymanej liczby 5 powinien zostać zwrócony słownik: {1: 1, 2: 4, 3: 9, 4: 16}.

### Zad 2. (★☆☆)

Tytuł: Kluczami są elementy jednej listy, a wartościami elementy drugiej listy.

Treść: Otrzymujesz dwie listy liczb całkowitych. Zbuduj słownik składający się z kluczy będących elementami pierwszej listy i wartościami będącymi elementami drugiej listy. Jeśli listy są różnej długości, zwróć pusty słownik.

Dane wejściowe: Dwie listy liczb całkowitych.

Dane wyjściowe: Słownik par: liczba całkowita, liczba całkowita.

Przykład:

Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], powinien zostać zwrócony słownik: {3: 1, 5: 2, 8: -1}.

### Zad 3. (★☆☆)

Tytuł: Klucz to imię, wartość lista wypożyczonych książek.

Treść: Zbuduj prostą bazę danych dla biblioteki opartą o słownik, w którym kluczami są imiona czytelników, a wartościami listy wypożyczonych książek. Baza danych powinna umożliwiać:
Dodanie wypożyczonej książki do danego czytelnika.
Zwrócenie wypożyczonej książki przez czytelnika.
Wypisanie aktualnej listy wypożyczonych książek dla danego czytelnika.


### Zad 4. (★☆☆)

Tytuł: Usuń ze słownika.

Treść: Otrzymujesz słownik par napisów i liczb całkowitych oraz pojedynczą liczbę całkowitą. Usuń ze słownika pary, dla których wartość równa jest otrzymanej liczbie.

Dane wejściowe: Słownik par: napis, liczba całkowita oraz liczba całkowita.

Dane wyjściowe: Słownik par: napis, liczba całkowita.

Przykład:

Dla otrzymanego słownika oraz liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, powinien zostać zwrócony słownik: {“abc”: 1, “cba” : 3}.

### Zad 5. (★☆☆)

Tytuł: Lista pracowników.

Treść: Otrzymujesz listę par. Pierwszym elementem pary jest napis reprezentujący imię i nazwisko pracownika, drugim zysk z transakcji, jaką dany pracownik przeprowadził. Znajdź pracownika, który przyniósł firmie najwięcej zysku.

Dane wejściowe: Lista par: napis, liczba naturalna.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanej listy:

[[“Barnaba Barabash”, 120],
[“Jon Snow”, 100],
[“Kira Summer”, 300],
[“Barnaba Barabash”, 200],
[“Bob Marley”, 110]]

 powinien zostać zwrócony napis:  “Barnaba Barabash”.

### Zad 6. (★☆☆)

Tytuł: Histogram znaków w słowie.

Treść: Otrzymujesz napis. Znajdź częstość występowania znaków w otrzymanym napisie. Inaczej, zwróć histogram znaków w otrzymanym napisie.

Dane wejściowe: Napis.

Dane wyjściowe: Słownik par: znak, liczba naturalna.

Przykład:

Dla otrzymanego napisu: “klasa”, powinien zostać zwrócony słownik: {“k”: 1, “l”: 1, “a”: 2, “s”: 1}.

### Zad 7. (★☆☆)

Tytuł: Histogram słów w tekście.

Treść: Otrzymujesz tekst w postaci napisu. Znajdź częstość występowania każdego ze słów w tekście. Zignoruj różnice między małymi i wielkimi literami. Pamiętaj, słowa składają się wyłącznie z liter.

Dane wejściowe: Napis.

Dane wyjściowe: Słownik par: napis, liczba naturalna.

Przykład:

Dla otrzymanego napisu:

> Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now.

powinien zostać zwrócony słownik:

> {“here“: 1, “a“: 12, “tricksy“: 4, “corpus“: 5, “will“: 6, “exist“: 1, “very“: 2, “strange“: 1, “sometimes“: 1, “cryptic“: 1, “dumbfound“: 1, “you“: 2, “maybe“: 1, “perhaps“: 1, “bit“: 1, “in“: 1, “particular“: 1, “since“: 1, “my“: 1, “not“: 1, “match“: 1, “the“: 2, “pattern“: 1, “expect“: 1, "from": 2, "it": 2, "nor": 1, "look": 1, "like": 1, "fish,": 1, "boat": 1, "sunflower": 1, "or": 3, "handsome": 1, "kitten": 1, "surprise": 1, "user": 1, "named": 1, "ami": 1, "tavory;": 1, "this": 1, "be": 1, "fun": 1, "to": 1, "follow": 1, "year": 1, "month": 1, "minute": 1, "now": 1}

### Zad 8. (★☆☆)

Tytuł: Najczęściej występująca litera w zdaniu.

Treść: Otrzymujesz napis reprezentujący zdanie. Znajdź najczęściej występującą literę w zdaniu. Jeśli więcej niż jedna litera występuje tę samą liczbę razy, zwróć literę najwcześniej pojawiającą się w zdaniu.

Dane wejściowe: Napis.

Dane wyjściowe: Znak.

Przykład:

Dla otrzymanego napisu: “lezy jerzy na wiezy”, powinna zostać zwrócona litera: ‘e’.

### Zad 9. (★☆☆)

Tytuł: Powtarzające się znaki.

Treść: Otrzymujesz napis. Znajdź w otrzymanym napisie wszystkie znaki powtarzające się więcej niż raz.

Dane wejściowe: Napis.

Dane wyjściowe: Lista znaków.

Przykład:

Dla otrzymanego napisu: “podwodny”, powinna zostać zwrócona lista: [‘o’, ‘d’].

### Zad 10. (★★☆)

Tytuł: Anagramy w tekście.

Treść: Otrzymujesz tekst w postaci napisu. Znajdź wszystkie słowa, w których te same znaki występują tę samą liczbę razy. Inaczej, znajdź wszystkie anagramy w tekście. Zignoruj różnice między małymi i wielkimi literami. Pamiętaj, słowa składają się wyłącznie z liter.

Dane wejściowe: Napis.

Dane wyjściowe: Lista list napisów.

Przykład:

Dla otrzymanego napisu: 

“To absurd, że tyran Brudas, ten straszliwy bandzior sprawuje rządy w tym kraju. Burza nad galerią i alergia na narty to żadna zbrodnia jak bandzior i jego arbuz”., 

powinna zostać zwrócona lista: 

[[“absurd”, “brudas”], [“tyran”, “narty”], [“bandzior”, “zbrodnia”], [“burza”, “arbuz”], [“galeria”, “alergia”]].

### Zad 11. (★☆☆)

Tytuł: Sortowanie względem kluczy/wartości.

Treść: Otrzymujesz słownik składający się z par napisów i liczb całkowitych.
Wypisz pary posortowane względem napisów.
Wypisz pary posortowane względem liczb.

Dane wejściowe: Słownik par: napis, liczba całkowita.

Dane wyjściowe: Lista par.

Przykład:

Dla otrzymanego słownika: {“c”: 3, “x”: 5, “a”: -2, “b”: 4}, powinien zostać zwrócony słownik: [(“a”, -2), (“b”, 4), (“c”, 3), (“x”, 5)].
Dla otrzymanego słownika: {“c”: 3, “x”: 5, “a”: -2, “b”: 4}, powinien zostać zwrócony słownik: [(“a”, -2), (“c”, 3), (“b”, 4), (“x”, 5)].

### Zad 12. (★★☆)

Tytuł: Czy słowniki są identyczne?

Treść: Otrzymujesz dwa słowniki składające się z par napisów i list liczb całkowitych. Listy są nieuporządkowane. Sprawdź, czy słowniki składają się z tych samych par. Dwie listy uznajemy za identyczne, jeśli zawierają te same elementy, przy czym kolejność elementów może być zmieniona.

Dane wejściowe: Dwa słowniki par: napis, lista liczb całkowitych.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanych słowników:
{“c”: [3, 2, 1], “x”: [-2, 9, 11], “a”: [4, 6, 7]} i 
{“a”: [7, 4, 6], “c”: [2, 3, 1], “x”: [-2, 11, 9]}, 
powinna zostać zwrócona wartość logiczna: Prawda.

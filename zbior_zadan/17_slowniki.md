## Słowniki

### Zad 1. (★☆☆)

Tytuł: Słownik z kluczami będącymi liczbami naturalnymi i wartościami ich kwadratami.

Treść: Dostajesz liczbę naturalną. Stwórz słownik, w którym kluczami będą kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartościami będą ich kwadraty.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Słownik z kluczami i wartościami będącymi liczbami naturalnymi.

Przykład:

Dla liczby 5, słownik powinien wyglądać następująco: {1: 1, 2: 4, 3: 9, 4: 16}.

### Zad 2. (★☆☆)

Tytuł: Słownik z kluczami będącymi elementami jednej listy i wartościami elementami drugiej listy.

Treść: Dostajesz dwie listy liczb całkowitych. Stwórz słownik, w którym kluczami będą elementy pierwszej listy, a wartościami elementy drugiej listy. Jeśli listy są różnej długości, zwróć pusty słownik.

Dane wejściowe: Dwie listy liczb całkowitych.

Dane wyjściowe: Słownik z kluczami i wartościami będącymi liczbami całkowitymi.

Przykład:

Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], słownik powinien wyglądać następująco: {3: 1, 5: 2, 8: -1}.

### Zad 3. (★☆☆)

Tytuł: Klucz to imię, wartość lista wypożyczonych książek.

Treść: Zbuduj prostą bazę danych dla biblioteki opartą o słownik, w którym kluczami są imiona czytelników, a wartościami listy wypożyczonych książek. Baza danych powinna umożliwiać:

1. Dodanie wypożyczonej książki do danego czytelnika.
2. Zwrócenie wypożyczonej książki przez czytelnika.
3. Wypisanie aktualnej listy wypożyczonych książek dla danego czytelnika.

### Zad 4. (★☆☆)

Tytuł: Usuwanie z słownika.

Treść: Otrzymujesz słownik par napisów i liczb całkowitych oraz pojedynczą liczbę całkowitą. Usuń z słownika pary, dla których wartość jest równa otrzymanej liczbie.

Dane wejściowe: Słownik par napisów i liczb całkowitych oraz liczba całkowita.

Dane wyjściowe: Słownik par napisów i liczb całkowitych.

Przykład:

Dla słownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, słownik powinien wyglądać następująco: {“abc”: 1, “cba” : 3}.

### Zad 5. (★☆☆)

Tytuł: Lista pracowników z największymi zyskami.

Treść: Otrzymujesz listę par. Pierwszym elementem pary jest napis reprezentujący imię i nazwisko pracownika, drugim zysk z transakcji, jaką dany pracownik przeprowadził. Znajdź pracownika, który przyniósł firmie najwięcej zysku.

Dane wejściowe: Lista par napisów i liczb naturalnych.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanej listy:

[["Barnaba Barabash", 120],
["Jon Snow", 100],
["Kira Summer", 300],
["Barnaba Barabash", 200],
["Bob Marley", 110]]

zostanie zwrócony napis: “Barnaba Barabash”.

### Zad 6. (★☆☆)

Tytuł: Histogram wystąpień znaków w słowie.

Treść: Otrzymujesz napis. Znajdź częstość występowania znaków w otrzymanym napisie. Innymi słowy, zwróć histogram znaków w otrzymanym napisie.

Dane wejściowe: Napis.

Dane wyjściowe: Słownik par znaków i liczb naturalnych.

Przykład:

Dla otrzymanego napisu: “klasa”, słownik powinien wyglądać następująco: {“k”: 1, “l”: 1, “a”: 2, “s”: 1}.

### Zad 7. (★☆☆)

Tytuł: Histogram słów w tekście

Treść: Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znaleźć częstość występowania każdego ze słów w tekście. Należy zignorować różnice między małymi i wielkimi literami. Pamiętaj, że słowa składają się wyłącznie z liter.

Dane wejściowe: Napis.

Dane wyjściowe: Słownik par: napis, liczba naturalna.

Przykład:

Dla otrzymanego napisu: "Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now."

Powinien zostać zwrócony słownik:

{"here": 1, "a": 12, "tricksy": 4, "corpus": 5, "will": 6, "exist": 1, "very": 2, "strange": 1, "sometimes": 1, "cryptic": 1, "dumbfound": 1, "you": 2, "maybe": 1, "perhaps": 1, "bit": 1, "in": 1, "particular": 1, "since": 1, "my": 1, "not": 1, "match": 1, "the": 2, "pattern": 1, "expect": 1, "from": 2, "it": 2, "nor": 1, "look": 1, "like": 1, "fish": 1, "boat": 1, "sunflower": 1, "or": 3, "handsome": 1, "kitten": 1, "surprise": 1, "user": 1, "named": 1, "ami": 1, "tavory": 1, "this": 1, "be": 1, "fun": 1, "to": 1, "follow": 1, "year": 1, "month": 1, "minute": 1, "now": 1}

### Zad 8. (★☆☆)

Tytuł: Najczęściej występująca litera w zdaniu

Treść: Otrzymujesz napis reprezentujący zdanie. Twoim zadaniem jest znalezienie najczęściej występującej litery w zdaniu. Jeśli więcej niż jedna litera występuje tę samą liczbę razy, należy zwrócić literę najwcześniej pojawiającą się w zdaniu.

Dane wejściowe: Napis.

Dane wyjściowe: Znak.

Przykład:

Dla otrzymanego napisu: "lezy jerzy na wiezy"

Powinna zostać zwrócona litera: 'e'

### Zad 9. (★☆☆)

Tytuł: Powtarzające się znaki

Otrzymujesz napis. Twoim zadaniem jest znalezienie i zwrócenie wszystkich znaków, które występują co najmniej 2 razy w ciągu.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "aaabbbccc"

Powinien zostać zwrócony napis: "abc"

### Zad 10. (★★☆)

Tytuł: Anagramy w tekście

Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezienie wszystkich słów, w których te same znaki występują tę samą liczbę razy. Innymi słowy, szukasz anagramów w tekście. Należy zignorować różnice między małymi i wielkimi literami. Pamiętaj, że słowa składają się wyłącznie z liter.

Dane wejściowe: Napis.

Dane wyjściowe: Lista list napisów.

Przykład:

Dla otrzymanego napisu:

"To absurd, że tyran Brudas, ten straszliwy bandzior sprawuje rządy w tym kraju. Burza nad galerią i alergia na narty to żadna zbrodnia jak bandzior i jego arbuz.",

powinna zostać zwrócona lista:

[["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]].

### Zad 11. (★☆☆)

Tytuł: Sortowanie względem kluczy/wartości

Otrzymujesz słownik składający się z par napisów i liczb całkowitych. Twoim zadaniem jest wypisanie par posortowanych względem napisów oraz względem liczb.

Dane wejściowe: Słownik par: napis, liczba całkowita.

Dane wyjściowe: Lista par.

Przykład:

Dla otrzymanego słownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostać zwrócony słownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego słownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostać zwrócony słownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].

### Zad 12. (★★☆)

Tytuł: Czy słowniki są identyczne?

Otrzymujesz dwa słowniki składające się z par napisów i list liczb całkowitych. Listy są nieuporządkowane. Twoim zadaniem jest sprawdzenie, czy słowniki składają się z tych samych par. Dwie listy uznajemy za identyczne, jeśli zawierają te same elementy, niezależnie od kolejności, w jakiej się one znajdują.

Dane wejściowe: Dwa słowniki par: napis, lista liczb całkowitych.

Dane wyjściowe: Wartość boolowska.

Przykład:

Dla otrzymanych słowników:

{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}

Powinna zostać zwrócona wartość logiczna: Prawda.

Dla otrzymanych słowników:

{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}

Powinna zostać zwrócona wartość logiczna: Fałsz.

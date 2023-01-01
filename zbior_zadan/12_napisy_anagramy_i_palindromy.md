## Napisy — anagramy i palindromy

### Zad 1. (★☆☆)

Tytuł: Sprawdzenie, czy słowo jest palindromem.

Treść: Napisz program, który sprawdzi, czy słowo jest palindromem. Palindromem jest słowo, które brzmi tak samo czytane od lewej do prawej i od prawej do lewej.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “kajak”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 2. (★★☆)

Tytuł: Znalezienie wszystkich permutacji słowa.

Treść: Napisz program, który dla otrzymanego napisu znajdzie jego wszystkie permutacje.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “abc”, powinna zostać zwrócona lista: [“abc”, “bac”, “cab”, “acb”, “bca”, “cba”].

### Zad 3. (★☆☆)

Tytuł: Sprawdzenie, czy dwa słowa są anagramami.

Treść: Napisz program, który dla podanych dwóch napisów sprawdzi, czy są anagramami. Dwa napisy są anagramami, jeśli jeden z nich można zbudować poprzez przestawienie znaków w drugim.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “ula” oraz “lua”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 4. (★★☆)

Tytuł: Wyszukanie wszystkich palindromów w zdaniu.

Treść: Napisz program, który otrzymuje napis reprezentujący zdanie. Twoim zadaniem jest znalezienie wszystkich palindromów w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “Tata zabral kajak na wycieczke i uderzyl sie w oko”, powinna zostać zwrócona lista: ["kajak", "i", "w", "oko"].

### Zad 5. (★★☆)

Tytuł: Znalezienie anagramów słowa w zdaniu.

Treść: Napisz program, który otrzymuje napis reprezentujący zdanie oraz słowo. Twoim zadaniem jest znalezienie wszystkich anagramów otrzymanego słowa w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanych napisów: “Sroga kara.” oraz “arak”, powinna zostać zwrócona lista: [“kara”].

### Zad 6. (★★☆)

Tytuł: Permutacje słowa, które są palindromami.

Treść: Napisz program, który znajdzie permutacje danego słowa, które są palindromami.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “taco”, powinna zostać zwrócona lista: ["taco", "toca"].

### Zad 7. (★★★)

Tytuł: Minimalna ilość usuniętych znaków, aby uzyskać anagramy.

Treść: Napisz program, który dla dwóch słów zwróci minimalną ilość znaków, które trzeba usunąć, aby uzyskać anagramy. Jeśli słowa są różnej długości, zwróć -1.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych napisów: “grazyna” oraz “razynax”, powinna zostać zwrócona liczba: 2.

### Zad 8. (★★★)

Tytuł: Wyjątkowe palindromy.

Treść: Napisz program, który znajdzie wszystkie wyjątkowe palindromy, jakie można utworzyć ze znaków w słowie (bez zmiany kolejności występowania). Nie uwzględniaj duplikatów w liście.

Wyjątkowy palindrom musi spełniać jeden z dwóch warunków:

1. Wszystkie znaki są identyczne, np. “xxx”.
2. Wszystkie znaki poza środkowym znakiem są identyczne, np. “ccdcc”.

Pojedynczy znak jest również uznawany za wyjątkowy palindrom.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “xxxx”, powinna zostać zwrócona lista: [“x”, “xx”, 'xxx', 'xxxx'].

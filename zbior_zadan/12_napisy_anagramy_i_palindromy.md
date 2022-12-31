## Napisy — anagramy i palindromy

### Zad 1. (★☆☆)

Tytuł: Czy słowo jest palindromem?

Treść: Sprawdź, czy słowo jest palindromem. Palindrom to słowo brzmiące tak samo czytane od lewej do prawej i od prawej do lewej.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “kajak”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 2. (★★☆)

Tytuł: Wszystkie permutacje słowa.	

Treść: Dla otrzymanego napisu, znajdź jego wszystkie permutacje.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “abc”, powinna zostać zwrócona lista: [“abc”, “bac”, “cab”, “acb”, “bca”, “cba”].

### Zad 3. (★☆☆)

Tytuł: Czy słowa są swoimi anagramami?

Treść: Dla podanych dwóch napisów sprawdź, czy są swoimi anagramami. Dwa napisy są anagramami, jeśli jeden z nich można zbudować poprzez przestawienie znaków w drugim.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “ula” oraz “lua”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 4. (★★☆)

Tytuł: Wszystkie palindromy w zdaniu.

Treść: Otrzymujesz napis reprezentujący zdanie. Znajdź wszystkie palindromy w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “Tata zabral kajak na wycieczke i uderzyl sie w oko”, powinna zostać zwrócona lista: ["kajak", "i", "w", "oko"].

### Zad 5. (★★☆)

Tytuł: Znajdź anagramy w zdaniu.

Treść: Otrzymujesz napis reprezentujący zdanie oraz słowo. Znajdź wszystkie anagramy otrzymanego słowa w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanych napisów: “Sroga kara.” oraz “arak”, powinna zostać zwrócona lista: [“kara”].

### Zad 6. (★★☆)

Tytuł: Permutacje danego słowa będące palindromami.

Treść: Znajdź permutacje danego słowa będące palindromami.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “adamm”, powinna zostać zwrócona lista: [“madam”, “amdma”].

### Zad 7. (★★★)

Tytuł: Dla dwóch słów, ile minimalnie znaków musimy usunąć, aby uzyskać anagramy?

Treść: Dla dwóch słów, ile minimalnie znaków musimy usunąć, aby uzyskać anagramy. Zwróć -1 dla słów o różnych długościach.	

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych napisów:  “grazyna” oraz  “razynax”, powinna zostać zwrócona liczba: 2.

### Zad 8. (★★★)

Tytuł: Wyjątkowe palindromy.	

Treść: Znajdź wszystkie wyjątkowe palindromy, jakie można utworzyć ze znaków w słowie (bez zmiany kolejności występowania). Nie uwzględniaj duplikatów w liście.

Wyjątkowy palindrom musi spełniać jeden z dwóch warunków:
1. Wszystkie znaki są identyczne, np. “xxx”.
2. Wszystkie znaki poza środkowym znakiem są identyczne, np. “ccdcc”.

Pojedynczy znak jest również uznawany za wyjątkowy palindrom.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “xxxx”, powinna zostać zwrócona lista: [“x”, “xx”, 'xxx', 'xxxx'].

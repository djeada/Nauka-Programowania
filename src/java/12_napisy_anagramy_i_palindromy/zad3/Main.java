/*
ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez przestawienie liter drugiego).

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli anagramy
* `Fałsz` — jeśli nie

### Przykład

**Wejście:**

```
ula
lua
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

*/
import java.util.*;

public class Main {
    
    // Sprawdza czy dwa slowa sa anagramami.
    // Zlozonosc Czasowa: O(n log n)
    // Zlozonosc Pamieciowa: O(n)
    public static boolean czyAnagram(String slowo1, String slowo2) {
        if (slowo1.length() != slowo2.length()) {
            return false;
        }
        
        char[] tab1 = slowo1.toLowerCase().toCharArray();
        char[] tab2 = slowo2.toLowerCase().toCharArray();
        
        Arrays.sort(tab1);
        Arrays.sort(tab2);
        
        return Arrays.equals(tab1, tab2);
    }
    
    public static void test1() {
        assert czyAnagram("ula", "lua") == true;
    }
    
    public static void test2() {
        assert czyAnagram("kara", "arak") == true;
    }
    
    public static void test3() {
        assert czyAnagram("kot", "pies") == false;
    }
    
    public static void main(String[] args) {
        test1();
        test2();
        test3();
    }
}

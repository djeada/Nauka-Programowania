/*
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★★
**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

### Uwagi

* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

*/
import java.util.*;

public class Main {
    
    // Oblicza minimalna liczbe usuniec, aby otrzymac anagramy.
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(k), gdzie k to liczba unikalnych znakow
    public static int minUsuniecDoAnagramu(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return -1;
        }
        
        HashMap<Character, Integer> zliczenia1 = new HashMap<>();
        HashMap<Character, Integer> zliczenia2 = new HashMap<>();
        
        for (char c : s1.toCharArray()) {
            zliczenia1.put(c, zliczenia1.getOrDefault(c, 0) + 1);
        }
        
        for (char c : s2.toCharArray()) {
            zliczenia2.put(c, zliczenia2.getOrDefault(c, 0) + 1);
        }
        
        int usuniecia = 0;
        HashSet<Character> wszystkieZnaki = new HashSet<>();
        wszystkieZnaki.addAll(zliczenia1.keySet());
        wszystkieZnaki.addAll(zliczenia2.keySet());
        
        for (char c : wszystkieZnaki) {
            int count1 = zliczenia1.getOrDefault(c, 0);
            int count2 = zliczenia2.getOrDefault(c, 0);
            usuniecia += Math.abs(count1 - count2);
        }
        
        return usuniecia;
    }
    
    public static void test1() {
        assert minUsuniecDoAnagramu("grazyna", "razynax") == 2;
    }
    
    public static void test2() {
        assert minUsuniecDoAnagramu("abc", "cba") == 0;
    }
    
    public static void test3() {
        assert minUsuniecDoAnagramu("abc", "de") == -1;
    }
    
    public static void main(String[] args) {
        test1();
        test2();
        test3();
    }
}

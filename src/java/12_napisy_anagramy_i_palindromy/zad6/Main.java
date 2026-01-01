/*
ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `palindrom`, `permutacje`, `multiset`

### Treść

Wczytaj słowo i wypisz wszystkie **unikalne** palindromy, które są jego permutacjami.

### Wejście

* 1. linia: słowo (litery mogą się powtarzać)

### Wyjście

Każdy unikalny palindrom w osobnej linii. Jeśli nie istnieje żaden — puste wyjście.

### Przykład

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Uwagi

* Najpierw sprawdź warunek istnienia palindromu z liter: co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień.
* Generuj palindromy z połówek (bez wypisywania duplikatów).

*/
import java.util.*;

public class Main {
    
    // Sprawdza czy slowo jest palindromem.
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(1)
    public static boolean czyPalindrom(String slowo) {
        int lewy = 0;
        int prawy = slowo.length() - 1;
        
        while (lewy < prawy) {
            if (slowo.charAt(lewy) != slowo.charAt(prawy)) {
                return false;
            }
            lewy++;
            prawy--;
        }
        
        return true;
    }
    
    // Generuje permutacje i zwraca tylko te, ktore sa palindromami.
    // Zlozonosc Czasowa: O(n! * n)
    // Zlozonosc Pamieciowa: O(n!)
    public static void generujPalindromyPermutacje(String prefiks, String reszta, HashSet<String> wynik) {
        int n = reszta.length();
        if (n == 0) {
            if (czyPalindrom(prefiks)) {
                wynik.add(prefiks);
            }
        } else {
            for (int i = 0; i < n; i++) {
                generujPalindromyPermutacje(prefiks + reszta.charAt(i),
                                           reszta.substring(0, i) + reszta.substring(i + 1, n),
                                           wynik);
            }
        }
    }
    
    // Sprawdza czy mozna utworzyc palindrom z liter slowa.
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(k), gdzie k to liczba unikalnych znakow
    public static boolean czyMoznaPalindrom(String slowo) {
        HashMap<Character, Integer> zliczenia = new HashMap<>();
        for (char c : slowo.toCharArray()) {
            zliczenia.put(c, zliczenia.getOrDefault(c, 0) + 1);
        }
        
        int nieparzystych = 0;
        for (int count : zliczenia.values()) {
            if (count % 2 == 1) {
                nieparzystych++;
            }
        }
        
        return nieparzystych <= 1;
    }
    
    public static ArrayList<String> permutacjePalindromowe(String slowo) {
        ArrayList<String> wynik = new ArrayList<>();
        
        if (!czyMoznaPalindrom(slowo)) {
            return wynik;
        }
        
        HashSet<String> unikalne = new HashSet<>();
        generujPalindromyPermutacje("", slowo, unikalne);
        wynik.addAll(unikalne);
        Collections.sort(wynik);
        
        return wynik;
    }
    
    public static void test1() {
        ArrayList<String> wynik = permutacjePalindromowe("aabb");
        assert wynik.size() == 2;
        assert wynik.contains("abba");
        assert wynik.contains("baab");
    }
    
    public static void test2() {
        ArrayList<String> wynik = permutacjePalindromowe("abc");
        assert wynik.size() == 0;
    }
    
    public static void main(String[] args) {
        test1();
        test2();
    }
}

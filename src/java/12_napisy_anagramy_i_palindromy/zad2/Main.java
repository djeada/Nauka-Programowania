/*
ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `permutacje`, `backtracking`

### Treść

Wczytaj słowo z **unikalnych liter** i wypisz wszystkie jego permutacje — każdą w osobnej linii.

### Wejście

* 1. linia: słowo (litery nie powtarzają się)

### Wyjście

Wiele linii — wszystkie permutacje słowa, każda w osobnej linii.

### Przykład

**Wejście:**

```
abc
```

**Wyjście:**

```
abc
acb
bac
bca
cab
cba
```

### Uwagi o formatowaniu

* Kolejność wypisywania permutacji nie musi być dokładnie taka jak w przykładzie, o ile są wszystkie i bez powtórzeń.

*/
import java.util.*;

public class Main {
    
    // Generuje wszystkie permutacje slowa.
    // Zlozonosc Czasowa: O(n!)
    // Zlozonosc Pamieciowa: O(n!)
    public static void generujPermutacje(String prefiks, String reszta, ArrayList<String> wynik) {
        int n = reszta.length();
        if (n == 0) {
            wynik.add(prefiks);
        } else {
            for (int i = 0; i < n; i++) {
                generujPermutacje(prefiks + reszta.charAt(i),
                                reszta.substring(0, i) + reszta.substring(i + 1, n),
                                wynik);
            }
        }
    }
    
    public static ArrayList<String> permutacje(String slowo) {
        ArrayList<String> wynik = new ArrayList<>();
        generujPermutacje("", slowo, wynik);
        return wynik;
    }
    
    public static void test1() {
        ArrayList<String> wynik = permutacje("abc");
        assert wynik.size() == 6;
        assert wynik.contains("abc");
        assert wynik.contains("acb");
        assert wynik.contains("bac");
        assert wynik.contains("bca");
        assert wynik.contains("cab");
        assert wynik.contains("cba");
    }
    
    public static void test2() {
        ArrayList<String> wynik = permutacje("ab");
        assert wynik.size() == 2;
        assert wynik.contains("ab");
        assert wynik.contains("ba");
    }
    
    public static void main(String[] args) {
        test1();
        test2();
    }
}

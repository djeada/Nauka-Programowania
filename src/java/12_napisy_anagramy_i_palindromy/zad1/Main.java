/*
ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `string`, `palindrom`, `I/O`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej i od prawej do lewej jest takie samo).

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Uwagi o formatowaniu

* Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.

*/
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
    
    public static void test1() {
        assert czyPalindrom("kajak") == true;
    }
    
    public static void test2() {
        assert czyPalindrom("radar") == true;
    }
    
    public static void test3() {
        assert czyPalindrom("kot") == false;
    }
    
    public static void main(String[] args) {
        test1();
        test2();
        test3();
    }
}

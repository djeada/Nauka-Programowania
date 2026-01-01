/*
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.

*/
import java.util.*;

public class Main {
    
    // Sprawdza czy podciag jest wyj atkowym palindromem.
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(1)
    public static boolean czyWyjatkowyPalindrom(String s) {
        if (s.length() == 0) {
            return false;
        }
        
        if (s.length() == 1) {
            return true;
        }
        
        // Sprawdz czy wszystkie znaki sa identyczne
        boolean wszystkieIdentyczne = true;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(0)) {
                wszystkieIdentyczne = false;
                break;
            }
        }
        
        if (wszystkieIdentyczne) {
            return true;
        }
        
        // Sprawdz czy wszystkie znaki poza srodkowym sa identyczne
        // i czy jest palindromem
        int lewy = 0;
        int prawy = s.length() - 1;
        
        while (lewy < prawy) {
            if (s.charAt(lewy) != s.charAt(prawy)) {
                return false;
            }
            lewy++;
            prawy--;
        }
        
        // Jest palindromem, teraz sprawdz czy wszystkie oprócz srodkowego sa identyczne
        if (s.length() % 2 == 0) {
            return false; // Parzysty palindrom nie moze spelniac warunku
        }
        
        char brzegowy = s.charAt(0);
        int srodek = s.length() / 2;
        
        for (int i = 0; i < s.length(); i++) {
            if (i != srodek && s.charAt(i) != brzegowy) {
                return false;
            }
        }
        
        return true;
    }
    
    // Znajduje wszystkie unikalne wyjatkowe palindromy.
    // Zlozonosc Czasowa: O(n^3)
    // Zlozonosc Pamieciowa: O(k), gdzie k to liczba unikalnych palindromow
    public static ArrayList<String> wyjatkowePalindromyPodciagi(String slowo) {
        HashSet<String> unikalne = new HashSet<>();
        
        for (int i = 0; i < slowo.length(); i++) {
            for (int j = i + 1; j <= slowo.length(); j++) {
                String podciag = slowo.substring(i, j);
                if (czyWyjatkowyPalindrom(podciag)) {
                    unikalne.add(podciag);
                }
            }
        }
        
        ArrayList<String> wynik = new ArrayList<>(unikalne);
        Collections.sort(wynik);
        
        return wynik;
    }
    
    public static void test1() {
        ArrayList<String> wynik = wyjatkowePalindromyPodciagi("xxyxx");
        // Note: The docstring example appears to list "xxx" and "yxy" which are NOT substrings of "xxyxx"
        // Correct unique exceptional palindromes in "xxyxx" are:
        HashSet<String> oczekiwane = new HashSet<>(Arrays.asList("x", "xx", "xxyxx", "xyx", "y"));
        assert new HashSet<>(wynik).equals(oczekiwane);
    }
    
    public static void test2() {
        ArrayList<String> wynik = wyjatkowePalindromyPodciagi("aaa");
        assert wynik.contains("a");
        assert wynik.contains("aa");
        assert wynik.contains("aaa");
    }
    
    public static void main(String[] args) {
        test1();
        test2();
    }
}

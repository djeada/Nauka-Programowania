/*
ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Sroga kara.
arak
```

**Wyjście:**

```
kara
```

### Uwagi

* Tak jak wyżej: usuń interpunkcję z brzegów słów.
* Porównuj np. posortowane litery w `lower()`.

*/
import java.util.*;

public class Main {
    
    // Usuwa interpunkcje z brzegu slowa.
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(n)
    public static String wyczysc(String slowo) {
        return slowo.replaceAll("^\\p{Punct}+|\\p{Punct}+$", "");
    }
    
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
    
    // Znajduje wszystkie anagramy slowa-klucza w zdaniu.
    // Zlozonosc Czasowa: O(n * m log m), gdzie n - liczba slow, m - dlugosc slowa
    // Zlozonosc Pamieciowa: O(k), gdzie k - liczba znalezionych anagramow
    public static ArrayList<String> anagramyWZdaniu(String zdanie, String klucz) {
        ArrayList<String> wynik = new ArrayList<>();
        String[] slowa = zdanie.split("\\s+");
        
        for (String slowo : slowa) {
            String wyczyszczone = wyczysc(slowo);
            if (!wyczyszczone.isEmpty() && czyAnagram(wyczyszczone, klucz)) {
                wynik.add(wyczyszczone);
            }
        }
        
        return wynik;
    }
    
    public static void test1() {
        String zdanie = "Sroga kara.";
        String klucz = "arak";
        ArrayList<String> wynik = anagramyWZdaniu(zdanie, klucz);
        ArrayList<String> oczekiwane = new ArrayList<>(Arrays.asList("kara"));
        assert wynik.equals(oczekiwane);
    }
    
    public static void test2() {
        String zdanie = "kot pies tok";
        String klucz = "kot";
        ArrayList<String> wynik = anagramyWZdaniu(zdanie, klucz);
        ArrayList<String> oczekiwane = new ArrayList<>(Arrays.asList("kot", "tok"));
        assert wynik.equals(oczekiwane);
    }
    
    public static void main(String[] args) {
        test1();
        test2();
    }
}

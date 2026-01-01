/*
ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).

*/
import java.util.*;

public class Main {
    
    // Usuwa interpunkcje z brzegu slowa.
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(n)
    public static String wyczysc(String slowo) {
        return slowo.replaceAll("^\\p{Punct}+|\\p{Punct}+$", "");
    }
    
    // Sprawdza czy slowo jest palindromem (ignorujac wielkosc liter).
    // Zlozonosc Czasowa: O(n)
    // Zlozonosc Pamieciowa: O(1)
    public static boolean czyPalindrom(String slowo) {
        slowo = slowo.toLowerCase();
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
    
    // Znajduje wszystkie palindromy w zdaniu.
    // Zlozonosc Czasowa: O(n * m), gdzie n - liczba slow, m - srednia dlugosc slowa
    // Zlozonosc Pamieciowa: O(k), gdzie k - liczba znalezionych palindromow
    public static ArrayList<String> palindromyWZdaniu(String zdanie) {
        ArrayList<String> wynik = new ArrayList<>();
        String[] slowa = zdanie.split("\\s+");
        
        for (String slowo : slowa) {
            String wyczyszczone = wyczysc(slowo);
            if (!wyczyszczone.isEmpty() && czyPalindrom(wyczyszczone)) {
                wynik.add(slowo.replaceAll("\\p{Punct}+$", ""));
            }
        }
        
        return wynik;
    }
    
    public static void test1() {
        String zdanie = "Tata zabral kajak na wycieczke i uderzyl sie w oko";
        ArrayList<String> wynik = palindromyWZdaniu(zdanie);
        // Note: "Tata" is NOT a palindrome (t-a-t-a != a-t-a-t)
        // The docstring example appears to have an error
        ArrayList<String> oczekiwane = new ArrayList<>(Arrays.asList("kajak", "i", "w", "oko"));
        assert wynik.equals(oczekiwane);
    }
    
    public static void test2() {
        String zdanie = "Ala ma kota";
        ArrayList<String> wynik = palindromyWZdaniu(zdanie);
        ArrayList<String> oczekiwane = new ArrayList<>(Arrays.asList("Ala"));
        assert wynik.equals(oczekiwane);
    }
    
    public static void main(String[] args) {
        test1();
        test2();
    }
}

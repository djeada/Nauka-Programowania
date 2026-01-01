/*
ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj `N` liczb naturalnych. Lista jest fragmentem ciągu arytmetycznego z **jednym brakującym elementem**. Znajdź i wypisz brakującą wartość.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — brakujący element.

### Przykład

**Wejście:**

```
4
5
2
1
3
```

**Wyjście:**

```
4
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy, skladajacej sie z nieuporzadkowanych
  // kolejnych (za wyjatkiem jednego) wyrazow ciagu arytmetycznego,
  // znajdz brakujacy element.

  public static int sumaCiaguArt(ArrayList<Integer> lista) {
    int min = Collections.min(lista);
    int maks = Collections.max(lista);
    return (lista.size() + 1) * (min + maks) / 2;
  }

  public static int znajdzBrakujacyElement(ArrayList<Integer> lista) {

    int suma = 0;

    for (var liczba : lista) {
      suma += liczba;
    }

    int sumaPrzedzialu = sumaCiaguArt(lista);

    return sumaPrzedzialu - suma;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 8, 4, 10, 14, 2));
    int wynik = 12;
    assert znajdzBrakujacyElement(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 4, 5, 6));
    int wynik = 3;
    assert znajdzBrakujacyElement(lista) == wynik;
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}


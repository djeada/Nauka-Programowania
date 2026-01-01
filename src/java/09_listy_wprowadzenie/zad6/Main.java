/*
ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.

Wypisz:

* `Tak` — jeśli średnia występuje w liście,
* `Nie` — w przeciwnym razie.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
```

**Wyjście:**

```
Nie
```

### Uwagi

* Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb całkowitych.

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


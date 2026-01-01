/*
ZAD-07 — Zliczanie instancji klasy

**Poziom:** ★☆☆
**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę **MojaKlasa**, która zlicza ile instancji utworzono:

* prywatne pole statyczne licznik,
* konstruktor zwiększa licznik,
* metoda statyczna zwraca licznik.

Program tworzy np. 3 obiekty i wypisuje liczbę instancji.

### Wejście

Brak.

### Wyjście

Jedna linia.

### Przykład

**Wyjście:**

```
Liczba utworzonych instancji: 3
```

*/
import java.io.*;
import java.util.*;

public class Main implements Closeable {
  private static int licznik = 0;

  public Main() {
    licznik++;
  }

  public final void close() {
    licznik--;
  }

  public static int liczbaInstancji() {
    return licznik;
  }

  public static void wyswietl() {
    System.out.print("Aktualna liczba instancji: ");
    System.out.print(licznik);
    System.out.print("\n");
  }

  public static void test1() {
    int n = 5;
    ArrayList<Main> lista = new ArrayList<Main>();
    for (int i = 0; i < n; i++) {
      lista.add(new Main());
    }
    assert Main.liczbaInstancji() == n;
    // Clean up
    for (Main m : lista) {
      m.close();
    }
  }

  public static void test2() {
    assert Main.liczbaInstancji() == 0;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}


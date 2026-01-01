/*
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
```

*/
import java.util.*;

public class Main {

  public static List<Integer> usunDuplikatyV1(List<Integer> lista) {

    List<Integer> wynik = new ArrayList<Integer>();

    for (int x : lista) if (!wynik.contains(x)) wynik.add(x);

    return wynik;
  }

  public static List<Integer> usunDuplikatyV2(List<Integer> lista) {

    List<Integer> wynik = new ArrayList<Integer>();
    Set<Integer> zbior = new HashSet<>();

    for (int x : lista) if (zbior.add(x)) wynik.add(x);

    return wynik;
  }

  public static void main(String[] args) {

    List<Integer> lista = new ArrayList<>(Arrays.asList(2, 1, 2, 2, 3, 3));
    List<Integer> wynik = new ArrayList<>(Arrays.asList(2, 1, 3));

    assert usunDuplikatyV1(lista).equals(wynik);
    assert usunDuplikatyV2(lista).equals(wynik);
  }
}


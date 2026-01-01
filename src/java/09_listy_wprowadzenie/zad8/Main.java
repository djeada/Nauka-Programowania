/*
ZAD-08 — Usuń klucz

**Poziom:** ★☆☆
**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych oraz `klucz`. Usuń **pierwsze** wystąpienie `klucz` (jeśli istnieje). Następnie wypisz listę po modyfikacji w jednej linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna linia: lista po usunięciu, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
4
```

**Wyjście:**

```
6,2,1,27
```

### Uwagi

* Jeśli `klucz` nie występuje, wypisz listę bez zmian.

*/
import java.util.*;

public class Main {
  // Usun wszystkie wystapienia klucza z listy.
  // Kolejnosc elementow w liscie powinna zostac zachowana.

  public static ArrayList<Integer> usunWszystkieWystapieniaV1(ArrayList<Integer> lista, int klucz) {
    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i).equals(klucz)) {
        lista.remove(i--);
      }
    }
    return lista;
  }

  public static ArrayList<Integer> usunWszystkieWystapieniaV2(ArrayList<Integer> lista, int klucz) {
    lista.removeAll(Collections.singleton(klucz));
    return lista;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 7, 2, 1, 8));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 7, 1, 8));
    int klucz = 2;

    assert wynik.equals(usunWszystkieWystapieniaV1(lista, klucz));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 7, 2, 1, 8));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 7, 1, 8));
    int klucz = 2;

    assert wynik.equals(usunWszystkieWystapieniaV2(lista, klucz));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}


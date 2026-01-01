/*
ZAD-08 — Cyfry w słowach

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz zdanie. Wyodrębnij wszystkie ciągi cyfr, które są częścią słów (czyli są bezpośrednio połączone z literami). Nie uwzględniaj cyfr oddzielonych od liter spacjami.

### Wejście

Jedna linia:

* `zdanie`

### Wyjście

Każdy znaleziony ciąg cyfr w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

**Wyjście:**

```
29
37
3
91
```

*/
import java.util.*;

public class Main {
  public static List<String> cyfryV1(String napis) {
    String[] tablica = napis.split("\\p{Punct}+");
    List<String> lista = new ArrayList<String>();
    for (String slowo : tablica) {
      if (slowo.matches("[0-9]+") && !slowo.matches("[^0-9]+")) {
        lista.add(slowo.replaceAll("[^0-9]", ""));
      }
    }
    return lista;
  }

  public static void test1() {
    String napis = "jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("29");
    oczekiwane.add("37");
    oczekiwane.add("3891");
    oczekiwane.add("3");
    assert cyfryV1(napis).equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
  }
}


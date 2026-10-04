/*
ZAD-07 — Podziel tekst względem znaków interpunkcyjnych

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis (jedno lub kilka zdań). Podziel tekst na fragmenty w miejscach występowania znaków interpunkcyjnych (np. `, . ! ? ; :`). Usuń spacje na początku i końcu każdego fragmentu.

### Wejście

Jedna linia:

* `tekst`

### Wyjście

Każdy fragment w osobnej linii.

### Przykład

**Wejście:**

```
Ani nie poszedł do kina, ani nie wybrał się do teatru.
```

**Wyjście:**

```
Ani nie poszedł do kina
ani nie wybrał się do teatru
```

*/
import java.util.*;

public class Main {
  // Dzieli napis na fragmenty w miejscach znaków interpunkcyjnych i usuwa
  // białe znaki z początku i końca każdego fragmentu
  // Złożoność czasowa: O(n) gdzie n to długość napisu
  // Złożoność pamięciowa: O(m) gdzie m to liczba fragmentów
  public static ArrayList<String> podzielNapisV1(String napis) {
    String[] tablica = napis.split("[,.!?;:]+");
    ArrayList<String> lista = new ArrayList<String>();
    for (String fragment : tablica) {
      String przyciety = fragment.strip();
      if (!przyciety.isEmpty()) {
        lista.add(przyciety);
      }
    }
    return lista;
  }

  public static void test1() {
    String napis = "Ani nie poszedl do kina, ani nie wybral sie do teatru.";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Ani nie poszedl do kina");
    oczekiwane.add("ani nie wybral sie do teatru");
    assert podzielNapisV1(napis).equals(oczekiwane);
  }

  public static void test2() {
    String napis = "Tak!  Nie?Moze; a moze nie: kto wie...";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Tak");
    oczekiwane.add("Nie");
    oczekiwane.add("Moze");
    oczekiwane.add("a moze nie");
    oczekiwane.add("kto wie");
    assert podzielNapisV1(napis).equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}


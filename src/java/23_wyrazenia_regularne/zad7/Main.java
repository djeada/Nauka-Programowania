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
  public static ArrayList<String> podzielNapisV1(String napis) {
    String[] tablica = napis.split("\\p{Punct}+");
    ArrayList<String> lista = new ArrayList<String>();
    for (String slowo : tablica) {
      if (!slowo.isEmpty()) {
        lista.add(slowo);
      }
    }
    return lista;
  }

  public static void test1() {
    String napis = "Ani nie poszedl do kina, ani nie wybral sie do teatru.";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Ani");
    oczekiwane.add("nie");
    oczekiwane.add("poszedl");
    oczekiwane.add("do");
    oczekiwane.add("kina");
    oczekiwane.add("ani");
    oczekiwane.add("nie");
    oczekiwane.add("wybral");
    oczekiwane.add("sie");
    oczekiwane.add("do");
    oczekiwane.add("teatru");
    assert podzielNapisV1(napis).equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
  }
}


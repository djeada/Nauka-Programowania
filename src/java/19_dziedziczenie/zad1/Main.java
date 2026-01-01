/*
ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

**Poziom:** ★☆☆
**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. **Bazowa** — posiada metodę `przedstaw_sie()`, która wypisuje komunikat o klasie bazowej.
2. **Potomna** — dziedziczy po **Bazowej** i **nadpisuje** metodę `przedstaw_sie()`, ale w swojej implementacji:

   * najpierw **wywołuje** wersję metody z klasy bazowej,
   * potem dopisuje własny komunikat.

Program testowy:

* tworzy obiekt klasy potomnej,
* wywołuje metodę `przedstaw_sie()`.

### Wejście

Brak.

### Wyjście

Dwie linie, pokazujące najpierw komunikat klasy bazowej, a potem potomnej.

### Przykład

**Wyjście:**

```
Jestem klasą bazową.
A ja jestem klasą potomną.
```

*/
public class Main {
  public static class Bazowa {
    public void przedstaw_sie() {
      System.out.println("Jestem klasą bazową.");
    }
  }

  public static class Potomna extends Bazowa {
    @Override
    public void przedstaw_sie() {
      super.przedstaw_sie();
      System.out.println("A ja jestem klasą potomną.");
    }
  }

  public static void main(String[] args) {
    Potomna potomna = new Potomna();
    potomna.przedstaw_sie();
  }
}


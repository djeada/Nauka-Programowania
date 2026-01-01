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
  public static class Rodzic {
    public void info() {
      System.out.print("Jestem rodzicem");
      System.out.print("\n");
    }
  }

  public static class DzieckoA extends Rodzic {
    @Override
    public void info() {
      System.out.print("Jestem dzieckiem A");
      System.out.print("\n");
    }
  }

  public static class DzieckoB extends Rodzic {
    @Override
    public void info() {
      System.out.print("Jestem dzieckiem B");
      System.out.print("\n");
      super.info();
    }
  }

  public static void main(String[] args) {

    Rodzic rodzic = new Rodzic();
    rodzic.info();

    DzieckoA dzieckoA = new DzieckoA();
    dzieckoA.info();

    DzieckoB dzieckoB = new DzieckoB();
    dzieckoB.info();
  }
}


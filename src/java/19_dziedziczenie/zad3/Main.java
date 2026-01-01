/*
ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metoda `odglos()` zwraca/drukuje ogólny dźwięk.
* **Pies** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
* **Kot** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.

Program testowy:

* tworzy obiekty: `Zwierz`, `Pies`, `Kot`,
* umieszcza je w jednej kolekcji,
* iteruje i dla każdego wypisuje linię w formacie:
  `NazwaKlasy wydaje odgłos: ...`

### Wejście

Brak.

### Wyjście

Trzy linie, po jednej dla każdego obiektu.

### Przykład

**Wyjście:**

```
Zwierz wydaje odgłos: ...
Pies wydaje odgłos: Hau!
Kot wydaje odgłos: Miau!
```

*/
import java.util.*;

public class Main {
  private static class Zwierz {

    public void odglos() {
      System.out.println("Zwierz wydaje odgłos: ...");
    }
    
    public String getNazwaKlasy() {
      return "Zwierz";
    }
  }

  private static class Kot extends Zwierz {

    @Override
    public void odglos() {
      System.out.println("Kot wydaje odgłos: Miau!");
    }
    
    @Override
    public String getNazwaKlasy() {
      return "Kot";
    }
  }

  private static class Pies extends Zwierz {

    @Override
    public void odglos() {
      System.out.println("Pies wydaje odgłos: Hau!");
    }
    
    @Override
    public String getNazwaKlasy() {
      return "Pies";
    }
  }

  public static void main(String[] args) {

    ArrayList<Zwierz> zwierzaki =
        new ArrayList<Zwierz>(Arrays.asList(new Zwierz(), new Pies(), new Kot()));

    for (var zwierz : zwierzaki) {
      zwierz.odglos();
    }
  }
}


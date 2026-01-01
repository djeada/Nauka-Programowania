/*
ZAD-05 — Dziedziczenie wielokrotne: Ptak

**Poziom:** ★★☆
**Tagi:** `multiple inheritance`, `dziedziczenie`, `metody`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metody:

  * `jedz()` → wypisuje `Ptak je.`
  * `spij()` → wypisuje `Ptak śpi.`
  * `wydaj_dzwiek()` → wypisuje `Ptak wydaje dźwięk.`

* **ObiektLatajacy** — metody:

  * `lec()` → wypisuje `Ptak leci.`
  * `wyladuj()` → wypisuje `Ptak ląduje.`

* **Ptak** — dziedziczy po `Zwierz` oraz `ObiektLatajacy`.

Program testowy:

* tworzy obiekt `Ptak`,
* wywołuje metody w kolejności: `jedz`, `spij`, `wydaj_dzwiek`, `lec`, `wyladuj`.

### Wejście

Brak.

### Wyjście

Pięć linii jak w przykładzie.

### Przykład

**Wyjście:**

```
Ptak je.
Ptak śpi.
Ptak wydaje dźwięk.
Ptak leci.
Ptak ląduje.
```

*/
public class Main {

  private static interface ZwierzInterfejs {

    public void jedz();

    public void spij();

    public void wydajDzwiek();
  }

  private static interface ObiektLatajacyInterfejs {

    public void lec();

    public void wyladuj();
  }

  private static class Zwierz implements ZwierzInterfejs {

    public void jedz() {
      System.out.println("Ptak je.");
    }

    public void spij() {
      System.out.println("Ptak śpi.");
    }

    public void wydajDzwiek() {
      System.out.println("Ptak wydaje dźwięk.");
    }
  }

  private static class ObiektLatajacy implements ObiektLatajacyInterfejs {

    public void lec() {
      System.out.println("Ptak leci.");
    }

    public void wyladuj() {
      System.out.println("Ptak ląduje.");
    }
  }

  private static class Ptak implements ZwierzInterfejs, ObiektLatajacyInterfejs {
    Zwierz zwierz;
    ObiektLatajacy obiektLatajacy;

    public Ptak() {
      zwierz = new Zwierz();
      obiektLatajacy = new ObiektLatajacy();
    }

    public void jedz() {
      zwierz.jedz();
    }

    public void spij() {
      zwierz.spij();
    }

    public void wydajDzwiek() {
      zwierz.wydajDzwiek();
    }

    public void lec() {
      obiektLatajacy.lec();
    }

    public void wyladuj() {
      obiektLatajacy.wyladuj();
    }
  }

  public static void main(String[] args) {

    Ptak ptak = new Ptak();
    ptak.jedz();
    ptak.spij();
    ptak.wydajDzwiek();
    ptak.lec();
    ptak.wyladuj();
  }
}


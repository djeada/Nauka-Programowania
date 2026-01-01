/*
ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

* **Kształt** — klasa bazowa (ogólna) dla kształtów.
* **Koło** — dziedziczy po `Kształt`.
* **Kwadrat** — dziedziczy po `Kształt`.

Każda klasa ma mieć:

* metodę obliczającą **pole**,
* metodę wypisującą informacje o obiekcie: typ, parametry i pole.

Program:

* wczytuje promień `r` koła oraz bok `a` kwadratu,
* tworzy obiekty `Koło(r)` i `Kwadrat(a)`,
* wypisuje informacje o obu.

**Uwaga do formatowania:**
*Pole koła wypisz do 4 miejsc po przecinku.*
*Pole kwadratu wypisz bez wymuszania miejsc po przecinku (jak w przykładzie).*

### Wejście

* 1 linia: `r` (liczba rzeczywista)
* 2 linia: `a` (liczba rzeczywista)

### Wyjście

Blok informacji o kole, pusta linia, blok informacji o kwadracie.

### Przykład

**Wejście:**

```
5
4
```

**Wyjście:**

```
Kształt: Koło
Promień: 5
Pole powierzchni: 78.5398

Kształt: Kwadrat
Długość boku: 4
Pole powierzchni: 16
```

*/
// Zaprojektuj klase Ksztalt oraz klasy pochodne Kolo oraz Kwadrat.

import java.util.Scanner;

public class Main {

  private static abstract class Ksztalt {
    abstract double pole();
    abstract void wypisz();
  }

  private static class Kolo extends Ksztalt {
    private double promien;

    public Kolo(double promien) {
      if (promien <= 0) {
        throw new IllegalArgumentException("Wartosc musi byc dodatnia.");
      }
      this.promien = promien;
    }

    public double pole() {
      return Math.PI * Math.pow(promien, 2);
    }

    public void wypisz() {
      System.out.println("Kształt: Koło");
      System.out.println("Promień: " + (int)promien);
      System.out.printf("Pole powierzchni: %.4f%n", pole());
    }
  }

  private static class Kwadrat extends Ksztalt {
    private double bok;

    public Kwadrat(double bok) {
      if (bok <= 0) {
        throw new IllegalArgumentException("Wartosc musi byc dodatnia.");
      }
      this.bok = bok;
    }

    public double pole() {
      return Math.pow(bok, 2);
    }

    public void wypisz() {
      System.out.println("Kształt: Kwadrat");
      System.out.println("Długość boku: " + (int)bok);
      System.out.println("Pole powierzchni: " + (int)pole());
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    double r = scanner.nextDouble();
    double a = scanner.nextDouble();
    
    Kolo kolo = new Kolo(r);
    Kwadrat kwadrat = new Kwadrat(a);
    
    kolo.wypisz();
    System.out.println();
    kwadrat.wypisz();
    
    scanner.close();
  }
}


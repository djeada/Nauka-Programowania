/*
ZAD-01 — Klasa Koło

**Poziom:** ★★☆
**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę **Koło**:

1. Konstruktor przyjmuje promień `r` (domyślnie 1).
2. Metoda licząca **obwód**: ( 2\pi r )
3. Metoda licząca **pole**: ( \pi r^2 )
4. Metoda wypisująca informacje: promień, obwód i pole.

Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać informacje.

### Wejście

* 1 linia: `r` (liczba rzeczywista)

### Wyjście

Trzy linie jak w przykładzie (obwód i pole do 4 miejsc po przecinku).

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
Koło o promieniu: 3
Obwód koła: 18.8496
Pole koła: 28.2743
```

*/
import java.text.MessageFormat;

public class Kolo {

  public Kolo() {
    this(1);
  }

  public Kolo(double r) {
    if (r <= 0) {
      System.out.print("Promien nie moze byc liczba ujemna.\n");
      System.out.print("Promien ustawiono na 1.\n");
      promien = 1.0;
    } else {
      promien = r;
    }
  }

  public final void setPromien(double r) {
    promien = r;
  }

  public final double getPromien() {
    return promien;
  }

  public final double pole() {
    return Math.PI * Math.pow(promien, 2);
  }

  public final double obwod() {
    return 2 * Math.PI * promien;
  }

  public final double srednica() {
    return 2 * promien;
  }

  @Override
  public String toString() {

    return MessageFormat.format(
        "Promien = {0}.\nSrednica = {1}.\nPole = {2}.\nObwod = {3}.",
        this.promien, this.srednica(), this.pole(), this.obwod());
  }

  private double promien;

  public static void main(String[] args) {

    Kolo kolo = new Kolo(3);
    System.out.print(kolo);
  }
}


/*
ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

* `Rok jest przestępny.`
* `Rok nie jest przestępny.`

### Wejście

* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

*/
public class Main {
  public static void main(String[] args) {

    // Czy rok jest przestepny?

    System.out.print("Podaj rok:\n");

    Scanner s = new Scanner(System.in);
    int rok = Integer.parseInt(s.nextLine());

    if (rok % 4 == 0) {

      if (rok % 100 == 0) {
        if (rok % 400 == 0) {
          System.out.print("rok jest przestepny\n");
        } else {
          System.out.print("rok nie jest przestepny\n");
        }
      } else {
        System.out.print("rok jest przestepny\n");
      }
    } else {
      System.out.print("rok nie jest przestepny\n");
    }
  }
}


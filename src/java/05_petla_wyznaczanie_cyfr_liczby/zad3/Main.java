/*
ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

### Uwagi o formatowaniu

* Dla `n = 0` suma cyfr wynosi `0`.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, wyswietl liczbe Pi tyle razy
    // ile wynosi pobrana liczba, z dokladnoscia do tylu
    // miejsc po przecinku ile wynosi pobrana liczba.

    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    int suma = 0;

    while (a > 0) {
      suma += (a % 10);
      a = a / 10;
    }

    System.out.print("Suma cyfr podanej liczby wynosi " + suma + "\n");
  }
}


/*
ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p`,
* bok płytki `t` (płytka kwadratowa),
* długość podłogi `L`,
* szerokość podłogi `W`.

Oblicz liczbę płytek potrzebnych do pokrycia całej podłogi, zakładając układ bez docinania „na styk” (czyli wzdłuż każdego wymiaru zaokrąglasz w górę), a następnie podaj koszt całkowity.

### Wejście

4 liczby (każda w osobnej linii): `p`, `t`, `L`, `W`

### Wyjście

Jedna liczba: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia / gwarancje

* `p > 0`, `t > 0`, `L > 0`, `W > 0`
* Liczba płytek:

  * `nL = ceil(L / t)`
  * `nW = ceil(W / t)`
  * `n = nL * nW`
* Koszt: `n * p`

### Przykład

**Wejście:**

```
2
3
20
40
```

**Wyjście:**

```
196.00
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    System.out.print("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi");
    System.out.print("\n");

    int cena;
    int bokPlytki;
    int szerokoscPodlogi;
    int dlugoscPodlogi;

    Scanner s = new Scanner(System.in);
    cena = Integer.parseInt(s.nextLine());
    bokPlytki = Integer.parseInt(s.nextLine());
    szerokoscPodlogi = Integer.parseInt(s.nextLine());
    dlugoscPodlogi = Integer.parseInt(s.nextLine());

    int szerokoscKonieczna = szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki;
    int dlugoscKonieczna = dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki;

    int polePlytki = (int) Math.pow(bokPlytki, 2);
    int polePodlogi = szerokoscKonieczna * dlugoscKonieczna;

    float calkowityKoszt = cena * (float) polePodlogi / polePlytki;

    System.out.print("Dla plytki o dlugosci boku " + bokPlytki + " i ceny " + cena);
    System.out.print(" calkowity koszt wylozenia podlogi o wymiarach " + szerokoscPodlogi);
    System.out.print("x" + dlugoscPodlogi + " wynosi " + calkowityKoszt + "\n");
  }
}


/*
ZAD-10 — Podmień napisy z listy A na napisy z listy B

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `zamiana`

### Treść

Otrzymujesz:

* tekst,
* listę A (napisy do znalezienia),
* listę B (napisy do podmiany), tej samej długości co A.

Zastąp w tekście wszystkie wystąpienia słów z listy A odpowiadającymi im słowami z listy B (ten sam indeks). Zamieniaj tylko **całe słowa**, nie fragmenty innych słów.

### Wejście

1. Tekst (jedna lub wiele linii)
2. Liczba naturalna `n` — długość list
3. `n` wierszy: elementy listy A
4. `n` wierszy: elementy listy B

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści — z listami A/B)*

*/
import java.util.*;

public class Main {
  
  // Podmienia słowa z listaA na odpowiadające słowa z listaB
  // Złożoność czasowa: O(n*m) gdzie n to długość napisu, m to liczba zamian
  // Złożoność pamięciowa: O(n)
  public static void podmien(String napis, List<String> listaA, List<String> listaB) {
    if (listaA.size() != listaB.size())
      return;

    Iterator<String> itA = listaA.iterator();
    Iterator<String> itB = listaB.iterator();

    while (itA.hasNext() || itB.hasNext()) {
      napis = napis.replaceAll("\\b" + itA.next() + "\\b", itB.next());
    }
  }

  public static void test1() {
    String napis =
        "Every mile was tilted at seven or. Wished her entire esteem mr oh by. " +
        "He prevents requests by if in pleased. Picture too and concerned was " +
        "comforting. Ten difficult resembled eagerness nor. Same park bore on " +
        "be. Warmth his law design says he is a person. Pronunciation suspected " +
        "in belonging conveying ye repulsive.";

    List<String> listaA = Arrays.asList("or", "be", "he");
    List<String> listaB = Arrays.asList("and", "off", "she");

    String oczekiwane =
        "Every mile was tilted at seven and. Wished her entire esteem mr oh by. " +
        "He prevents requests by if in pleased. Picture too and concerned was " +
        "comforting. Ten difficult resembled eagerness nor. Same park bore on " +
        "off. Warmth his law design says she is a person. Pronunciation " +
        "suspected in belonging conveying ye repulsive.";

    podmien(napis, listaA, listaB);

    assert(napis.equals(oczekiwane));
  }

  public static void main(String[] args) {

    test1();

  }
}


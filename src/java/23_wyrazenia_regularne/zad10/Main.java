import java.util.*;

/*
Otrzymujesz napis i dwie listy napisow. Podmien w pierwszym napisie, 
napisy z pierwszej listy na odpowiadajace im napisy z drugiej listy.
*/

public class Main {
  
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
        "Every mile was tilted at seven or. Wished her entire esteem mr oh by. "
        "He prevents requests by if in pleased. Picture too and concerned was "
        "comforting. Ten difficult resembled eagerness nor. Same park bore on "
        "be. Warmth his law design says he is a person. Pronunciation suspected "
        "in belonging conveying ye repulsive.";

    List<String> listaA = Arrays.asList("or", "be", "he");
    List<String> listaB = Arrays.asList("and", "off", "she");

    String oczekiwane =
        "Every mile was tilted at seven and. Wished her entire esteem mr oh by. "
        "He prevents requests by if in pleased. Picture too and concerned was "
        "comforting. Ten difficult resembled eagerness nor. Same park bore on "
        "off. Warmth his law design says she is a person. Pronunciation "
        "suspected in belonging conveying ye repulsive.";

    podmien(napis, listaA, listaB);

    assert(napis.equals(oczekiwane));
  }

  public static void main(String[] args) {

    test1();

  }
}
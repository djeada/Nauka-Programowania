/*
Tytul: Podmien napisy z listy A na napisy z listy B.
Tresc: Dostajesz napis oraz dwie listy napisow. Zastap napisy z pierwszej listy w pierwszym napisie odpowiadajacymi im napisami z drugiej listy.
Dane wejsciowe: Napis oraz dwie listy napisow.
Dane wyjsciowe: Napis.
Przyklad:
Dla podanych danych:
> 'Every mile was tilted at seven or.
Wished her entire esteem mr oh by.
He prevents requests by if in pleased.
Picture too and concerned was comforting.
Ten difficult resembled eagerness nor.
Same park bore on be.
Warmth his law design says he is a person.
Pronunciation suspected in belonging conveying ye repulsive.
oraz ['or', 'be', 'he'] i ['and', 'off', 'she'], powinien zostac zwrocony napis:
> Every mile was tilted at seven and.
Wished her entire esteem mr oh by.
She prevents requests by if in pleased.
Picture too and concerned was comforting.
Ten difficult resembled eagerness nor.
Same park bore on and off.
Warmth his law design says she is a person.
Pronunciation suspected in belonging conveying ye repulsive.

*/
import java.util.*;

public class Main {
  public static cyfryV1(String napis) {
    String[] tablica = napis.split("\\p{Punct}+");
    List<String> lista = new ArrayList<String>();
    for (String slowo : tablica) {
      if (slowo.matches("[0-9]+") && !slowo.matches("[^0-9]+")) {
        lista.add(slowo.replaceAll("[^0-9]", ""));
      }
    }
    return lista;
  }

  public static void test1() {
    String napis = "jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("29");
    oczekiwane.add("37");
    oczekiwane.add("3891");
    oczekiwane.add("3");
    assert cyfryV1(napis).equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
  }
}


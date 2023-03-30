/*
Tytul: Rysowanie ksztaltow za pomoca znakow.
Tresc zadania: Napisz program, ktory wypisze na standardowe wyjscie ciagi znakow tworzace kwadrat, trojkat oraz romb z jedynek. Pamietaj o dodawaniu odpowiednich spacji i przejsciach do nowej linii.
Przyklady:
Kwadrat:
xx
xx
Trojkat:
1
22
333
Romb z jedynek:
1
111
11111
111
1
Dane wejsciowe: Brak.
Dane wyjsciowe: Komunikat.

*/
public class Main {
  // Narysuj ksztalt.

  public static void main(String[] args) {

    System.out.print("xx\n");
    System.out.print("xx\n");
    System.out.print("\n");

    /*Trojkat.
    1
    22
    333
    */

    System.out.print("1\n");
    System.out.print("22\n");
    System.out.print("333\n");
    System.out.print("\n");

    /*Romb z jedynek.
      1
     111
    11111
     111
      1
     */

    System.out.print("  1\n");
    System.out.print(" 111\n");
    System.out.print("11111\n");
    System.out.print(" 111\n");
    System.out.print("  1\n");
  }
}


/*
Tytul: Rok przestepny.
Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie sprawdzal, czy dany rok jest przestepny.
Podpowiedz: Rok przestepny jest podzielny przez 4, ale nie jest podzielny przez 100, chyba ze jest podzielny przez 400.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat o tym, czy rok jest przestepny, czy tez nie.
Przyklad:
Dla pobranej liczby 2100, program powinien wypisac informacje, ze rok nie jest przestepny.

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


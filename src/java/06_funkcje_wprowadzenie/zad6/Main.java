/*
Tytul: Zamien wartosci miejscami.
Tresc: Napisz funkcje, ktora zamieni wartosci zmiennych a i b miejscami. Po wykonaniu funkcji zmienna a powinna przechowywac wartosc zmiennej b, a zmienna b powinna przechowywac wartosc zmiennej a.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla otrzymanych liczb: 8 i 5, powinny zostac zwrocone liczby 5 i 8.

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

  public static int sumaCyfr(int a) {
    int suma = 0;

    while (a > 0) {
      suma += (a % 10);
      a /= 10;
    }

    return suma;
  }

  public static void main(String[] args) {
    System.out.print("Podaj liczbe: \n");

    Scanner s = new Scanner(System.in);

    int a = Integer.parseInt(s.nextLine());

    System.out.print("Suma cyfr liczby to: " + sumaCyfr(a) + "\n");
  }
}


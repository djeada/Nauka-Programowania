/*
Tytul: Ile dni minelo od poczatku roku?
Tresc: Dla trzech pobranych liczb: reprezentujacych date wypisz, ile dni minelo od poczatku roku. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostac zwrocona liczba 45. **

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);

    System.out.print("Podaj dzien:\n");
    int DD = Integer.parseInt(s.nextLine());

    System.out.print("Podaj miesiac:\n");
    int MM = Integer.parseInt(s.nextLine());
    ;

    System.out.print("Podaj rok:\n");
    int rok = Integer.parseInt(s.nextLine());
    ;

    int CC = rok / 100;
    int YY = rok % 100;

    int A = (CC / 4) - 2 * CC - 1;
    int B = 5 * YY / 4;
    int C = 26 * (MM + 1) / 10;

    int wynik = (A + B + C + DD) % 7;

    switch (wynik) {
      case 1:
        System.out.print("pierwszym dniem tygodnia jest poniedzialek\n");
        break;

      case 2:
        System.out.print("drugim dniem tygodnia jest wtorek\n");
        break;

      case 3:
        System.out.print("trzecim dniem tygodnia jest sroda\n");
        break;

      case 4:
        System.out.print("czwartym dniem tygodnia jest czwartek\n");
        break;

      case 5:
        System.out.print("piatym dniem tygodnia jest piatek\n");
        break;

      case 6:
        System.out.print("szostym dniem tygodnia jest sobota\n");
        break;

      case 7:
        System.out.print("siodmym dniem tygodnia jest niedziela\n");
        break;

      default:
        System.out.print("bledne dane\n");
    }
  }
}


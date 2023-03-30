/*
Tytul: Konwersja jednostek.
Tresc zadania: Napisz program, ktory bedzie konwertowac jednostki zgodnie z nastepujacymi instrukcjami:
a) Pobierz wielkosc w kilogramach i wypisz, ile gramow odpowiada.
b) Pobierz wielkosc w calach i wypisz, ile centymetrow odpowiada.
c) Pobierz liczbe sekund i przelicz na godziny.
d) Pobierz liczbe w euro i wypisz, ile zlotowek odpowiada.
e) Pobierz miare kata w stopniach i wypisz, ile radianow odpowiada.
f) Pobierz temperature w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.
Dane wejsciowe: Liczba naturalna we wszystkich podpunktach.
Dane wyjsciowe:
* Liczba naturalna dla podpunktow 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostalych podpunktow.
Przyklad:
a) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 2000.
b) Dla pobranej liczby: 12, powinna zostac wypisana liczba: 4.724.
c) Dla pobranej liczby: 3600, powinna zostac wypisana liczba: 1.
d) Dla pobranej liczby: 4, powinna zostac wypisana liczba: 17.6.
e) Dla pobranej liczby: 120, powinna zostac wypisana liczba:  2.094.
f) Dla pobranej liczby: 100, powinny zostac wypisane liczby: 37.777 i -235.222.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

    System.out.print("podaj wielkosc w kilogramach:\n");

    int kilogramy;
    Scanner s = new Scanner(System.in);

    kilogramy = Integer.parseInt(s.nextLine());
    int gramy = kilogramy * 1000;

    System.out.print(kilogramy);
    System.out.print(" kg to ");
    System.out.print(gramy);
    System.out.print(" g.\n");

    // Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

    System.out.print("podaj wielkosc w calach:");
    System.out.print("\n");

    float cal;
    cal = Float.parseFloat(s.nextLine());
    float cm = (float) (cal / 2.54);

    System.out.print(cal);
    System.out.print(" cal to ");
    System.out.print(cm);
    System.out.print(" cm.\n");

    // Pobierz ilosc sekund i przelicz na godziny.

    System.out.print("podaj ilosc sekund:\n");

    float sekundy;
    sekundy = Float.parseFloat(s.nextLine());
    float godziny = sekundy / 3600;

    System.out.print(sekundy);
    System.out.print(" sekund to ");
    System.out.print(godziny);
    System.out.print(" godzin\n");

    // Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada.

    System.out.print("podaj liczbe w euro:\n");

    float euro;
    euro = Float.parseFloat(s.nextLine());
    float zloty = (float) (euro * 4.40);

    System.out.print(euro);
    System.out.print(" euro to ");
    System.out.print(zloty);
    System.out.print(" zlotych");
    System.out.print("\n");

    // Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.

    System.out.print("podaj miare kata w stopniach:\n");

    float katStopnie;
    katStopnie = Float.parseFloat(s.nextLine());
    float katRad = (float) (katStopnie * 0.0174532);

    System.out.print(katStopnie);
    System.out.print(" stopni to ");
    System.out.print(katRad);
    System.out.print(" radianow.\n");

    // Pobierz temperature w stopniach Farenheita i wypisz
    // ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada.

    System.out.print("podaj temperature w Farenheitach:\n");

    float tempF;
    tempF = Float.parseFloat(s.nextLine());
    float tempC = (tempF - 32) * 5 / 9;
    float tempK = tempC - 273;

    System.out.print(tempF);
    System.out.print(" F to ");
    System.out.print(tempC);
    System.out.print(" C i ");
    System.out.print(tempK);
    System.out.print(" K\n");
  }
}


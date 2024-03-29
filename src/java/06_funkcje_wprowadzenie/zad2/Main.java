/*
Tytul: Operacje arytmetyczne.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci:
a) Ich sume.
b) Roznice drugiej i pierwszej.
c) Ich iloczyn.
d) Iloraz pierwszej przez druga.
e) Reszte z dzielenia pierwszej przez druga.
Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.
Dane wyjsciowe: Liczba calkowita dla wszystkich podpunktow.
Przyklad:
Dla pobranych liczb: 3 i 5, funkcja powinna zwrocic:
a) Sume: 8
b) Roznice: 2
c) Iloczyn: 15
d) Iloraz: 0
e) Reszte z dzielenia: 3

*/
import java.util.*;

public class Main {
  // Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora
  // dla otrzymanych dwoch liczb zwroci:

  // a) ich sume
  public static int suma(int a, int b) {
    return a + b;
  }

  // b) roznice drugiej i pierwszej
  public static int roznica(int a, int b) {
    return b - a;
  }

  // c) ich iloczyn
  public static int iloczyn(int a, int b) {
    return a * b;
  }

  // d) reszte z dzielenia pierwszej przez druga
  public static int reszta(int a, int b) {
    return a % b;
  }

  public static void main(String[] args) {

    System.out.print("Podaj dwie liczby: \n");

    Scanner s = new Scanner(System.in);

    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    System.out.print("suma liczb to: " + suma(a, b) + "\n");
    System.out.print("roznice drugiej i pierwszej to: " + roznica(a, b) + "\n");
    System.out.print("iloczyn liczb to: " + iloczyn(a, b) + "\n");
    System.out.print("reszte z dzielenia pierwszej przez druga to: " + reszta(a, b) + "\n");
  }
}


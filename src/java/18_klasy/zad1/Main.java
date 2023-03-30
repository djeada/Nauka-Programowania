/*
Tytul: Zaprojektuj klase Kolo.
Opis zadania: Napisz klase Kolo, ktora bedzie reprezentowala kolo. Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje jedna liczbe jako argument, reprezentujaca promien kola. Domyslna wartoscia promienia powinno byc 1.
2. Funkcje obwod, ktora zwraca obwod kola.
3. Funkcje pole, ktora zwraca pole kola.
4. Funkcje, ktora wypisuje informacje o kole na standardowe wyjscie.
Napisz program, ktory przetestuje twoja klase. Stworz kolo o promieniu 3 i uzyj funkcji wypisujacej informacje o kole.

*/
import java.text.MessageFormat;

public class Kolo {

  public Kolo() {
    this(1);
  }

  public Kolo(double r) {
    if (r <= 0) {
      System.out.print("Promien nie moze byc liczba ujemna.\n");
      System.out.print("Promien ustawiono na 1.\n");
      promien = 1.0;
    } else {
      promien = r;
    }
  }

  public final void setPromien(double r) {
    promien = r;
  }

  public final double getPromien() {
    return promien;
  }

  public final double pole() {
    return Math.PI * Math.pow(promien, 2);
  }

  public final double obwod() {
    return 2 * Math.PI * promien;
  }

  public final double srednica() {
    return 2 * promien;
  }

  @Override
  public String toString() {

    return MessageFormat.format(
        "Promien = {0}.\nSrednica = {1}.\nPole = {2}.\nObwod = {3}.",
        this.promien, this.srednica(), this.pole(), this.obwod());
  }

  private double promien;

  public static void main(String[] args) {

    Kolo kolo = new Kolo(3);
    System.out.print(kolo);
  }
}


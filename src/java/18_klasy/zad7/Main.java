/*
Tytul: Zlicz instancje klasy w programie.
Tresc: Opis zadania: Stworz klase Klasa, ktora bedzie zawierala funkcje statyczna, zwracajaca aktualna liczbe instancji tej klasy w programie. Nastepnie stworz kilka obiektow tej klasy i przetestuj dzialanie funkcji.
Dane wejsciowe: brak
Dane wyjsciowe: liczba naturalna, reprezentujaca liczbe instancji klasy w programie.

*/
import java.io.*;
import java.util.*;

public class Klasa implements Closeable {
  private static int licznik = 0;

  public Klasa() {
    licznik++;
  }

  public final void close() {
    licznik--;
  }

  public static int liczbaInstancji() {
    return licznik;
  }

  public static void wyswietl() {
    System.out.print("Aktualna liczba instancji: ");
    System.out.print(licznik);
    System.out.print("\n");
  }

  public static void test1() {
    int n = 5;
    ArrayList<Klasa> lista = new ArrayList<Klasa>(n);
    assert Klasa.liczbaInstancji() == n;
  }

  public static void test2() {
    assert Klasa.liczbaInstancji() == 0;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}


/*
Tytul: Samochody jadace w przeciwnych kierunkach.
Tresc: Otrzymujesz liste zlozona wylacznie z liter 'A' i 'B', ktore odpowiadaja samochodom jadacym odpowiednio na wschod ('A') i zachod ('B'). Policz, ile razy samochody jadace w przeciwnych kierunkach mijaja sie.
Dane wejsciowe: Lista znakow odpowiadajacych samochodom jadacym na wschod ('A') i zachod ('B').
Dane wyjsciowe: Liczba naturalna oznaczajaca liczbe mijajacych sie samochodow.
Przyklad:
Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostac zwrocona liczba 5.

*/
import java.util.*;

public class Main {
  // Dla liczby N, wczytaj N liczb do listy, a nastepnie:
  public static void wczytaj(ArrayList<Integer> lista, int n) {
    for (int i = 0; i < n; i++) {
      Scanner s = new Scanner(System.in);
      int liczba = Integer.parseInt(s.nextLine());
      lista.add(liczba);
    }
  }

  // a)dodaj do kazdego elementu 1;
  public static void zwieksz(ArrayList<Integer> lista) {
    for (var liczba : lista) {
      liczba += 1;
    }
  }

  // b)pomnoz kazdy element przez jego indeks;
  public static void pomnoz(ArrayList<Integer> lista) {
    for (int i = 0; i < lista.size(); i++) {
      lista.set(i, lista.get(i) * i);
    }
  }

  // c)zastap wszystkie elementy wartoscia pierwszego elementu listy.
  public static void zastap(ArrayList<Integer> lista) {
    if (lista.isEmpty()) {
      return;
    }

    for (int i = 1; i < lista.size(); i++) {
      lista.set(i, lista.get(0));
    }
  }

  // Dla kazdego podpunktu wypisz zmodyfikowana liste. Elementy listy powinny
  // byc oddzielone przecinkami i wypisane w jednym wierszu.
  public static void wypiszOdKonca(ArrayList<Integer> lista) {
    for (var liczba : lista) {
      System.out.print(liczba);
      System.out.print(", ");
    }
    System.out.print("\n");
  }

  public static void main(String[] args) {

    ArrayList<Integer> lista = new ArrayList<Integer>();
    int n;

    System.out.print("podaj liczbe n: ");
    Scanner s = new Scanner(System.in);
    n = Integer.parseInt(s.nextLine());
    wczytaj(lista, n);

    ArrayList<Integer> kopia = new ArrayList<Integer>(lista);
    zwieksz(kopia);
    wypiszOdKonca(kopia);

    kopia = new ArrayList<Integer>(lista);
    pomnoz(kopia);
    wypiszOdKonca(kopia);

    kopia = new ArrayList<Integer>(lista);
    zastap(kopia);
    wypiszOdKonca(kopia);
  }
}


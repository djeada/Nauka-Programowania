/*
Tytul: Wieza Hanoi.
Tresc: N krazkow o roznych srednicach ulozonych jest na jednym z trzech slupkow (A, B lub C). Na dole znajduje sie krazek o najwiekszej srednicy. Kazdy nastepny jest mniejszy od poprzedniego. Znajdz sposob na przelozenie wszystkich krazkow na inny slupek. Pamietaj, ze nie wolno klasc krazka o wiekszej srednicy na krazek o mniejszej srednicy, ani przekladac kilku krazkow jednoczesnie.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Lista par znakow.
Przyklad:
Dla N = 3, powinna zostac zwrocona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]

*/
import java.util.*;

public class Main {
  // Wieza Hanoi.
  private static class Pair<T1, T2> {
    public T1 first;
    public T2 second;

    public Pair(T1 firstValue, T2 secondValue) {
      first = firstValue;
      second = secondValue;
    }

    @Override
    public boolean equals(Object o) {
      return (o instanceof Pair)
          && (this.first == ((Pair) o).first)
          && (this.second == ((Pair) o).second);
    }
  }

  public static void hanoiWew(
      int n, char a, char b, char c, ArrayList<Pair<Character, Character>> wynik) {

    if (n == 1) {
      wynik.add(new Pair<Character, Character>(a, b));
      return;
    }

    hanoiWew(n - 1, a, c, b, wynik);
    wynik.add(new Pair<Character, Character>(a, b));
    hanoiWew(n - 1, c, b, a, wynik);
  }

  // Zlozonosc Czasowa: O(2^n)
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static ArrayList<Pair<Character, Character>> hanoi(int n) {
    ArrayList<Pair<Character, Character>> wynik = new ArrayList<Pair<Character, Character>>();
    hanoiWew(n, 'A', 'B', 'C', wynik);
    return new ArrayList<Pair<Character, Character>>(wynik);
  }

  public static void test1() {
    int n = 3;
    ArrayList<Pair<Character, Character>> wynik =
        new ArrayList<Pair<Character, Character>>(
            Arrays.asList(
                new Pair<Character, Character>('A', 'B'),
                new Pair<Character, Character>('A', 'C'),
                new Pair<Character, Character>('B', 'C'),
                new Pair<Character, Character>('A', 'B'),
                new Pair<Character, Character>('C', 'A'),
                new Pair<Character, Character>('C', 'B'),
                new Pair<Character, Character>('A', 'B')));

    assert wynik.equals(hanoi(n));
  }

  public static void main(String[] args) {

    test1();
  }
}


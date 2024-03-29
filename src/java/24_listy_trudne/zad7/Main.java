/*
Tytul: Woda
Tresc: Otrzymujesz liste wysokosci slupkow. Wszystkie slupki maja jednakowa szerokosc, rowna jednej jednostce wysokosci, i ustawione sa obok siebie. Wysokosc rowna 0 oznacza brak slupka. Oblicz ile jednostek wody maksymalnie mozemy umiescic miedzy slupkami.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla wejsciowej listy [3, 0, 1, 0, 2], powinna zostac zwrocona liczba: 5.
Oto ilustracja dla powyzszego przykladu:
```
o
o      o
o  o   o  o  o
```
Mozemy umiescic 5 jednostek wody pomiedzy slupkami.

*/
import java.util.*;

public class Main {
  public static int ileWodyV1(ArrayList<Integer> slupki) {
    int n = slupki.size();
    int woda = 0;

    ArrayList<Integer> lewy = new ArrayList<Integer>();
    lewy.add(Integer.MIN_VALUE);

    for (int i = 0; i < n; i++) lewy.add(Math.max(lewy.get(i), slupki.get(i)));

    int prawy = Integer.MIN_VALUE;

    for (int i = n - 1; i >= 0; i--) {
      prawy = Math.max(prawy, slupki.get(i));

      if (Math.min(lewy.get(i), prawy) > slupki.get(i))
        woda += Math.min(lewy.get(i), prawy) - slupki.get(i);
    }

    return woda;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(3);
    lista.add(0);
    lista.add(1);
    lista.add(0);
    lista.add(2);
    int wynik = 5;

    assert (ileWodyV1(lista) == wynik);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(9);
    lista.add(2);
    lista.add(3);
    lista.add(9);
    lista.add(0);
    lista.add(2);
    int wynik = 15;

    assert (ileWodyV1(lista) == wynik);
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(1);
    int wynik = 0;

    assert (ileWodyV1(lista) == wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}


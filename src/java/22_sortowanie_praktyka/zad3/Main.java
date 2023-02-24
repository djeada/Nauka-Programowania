import java.util.*;

/*
Otrzymujesz liste par napisow i liczb. Posortuj pary w liscie wzgledem:
a) Liczb.
b) Dlugosci napisow.
*/

public class Main {
  
  private static class Para implements Comparable<Para> {
    private final String napis;
    private final int liczba;
    
    public Para(final String napis, final int liczba) {
      this.napis = napis;
      this.liczba = liczba;
    }
    
    public String getNapis() {
      return napis;
    }
    
    public int getLiczba() {
      return liczba;
    }
    
    @Override
    public int compareTo(final Para o) {
      if (liczba < o.liczba) {
        return -1;
      } else if (liczba > o.liczba) {
        return 1;
      } else {
        return napis.compareTo(o.napis);
      }
    }
  }
  
  public static void sortujWzgledemLiczb(ArrayList<Para> lista) {
    Collections.sort(lista, new Comparator<Para>() {
      @Override
      public int compare(final Para o1, final Para o2) {
        return o1.liczba - o2.liczba;
      }
    });
  }

  public static void sortujWzgledemDlugosci(ArrayList<Para> lista) {
    Collections.sort(lista, new Comparator<Para>() {
      @Override
      public int compare(final Para o1, final Para o2) {
        return o1.napis.length() - o2.napis.length();
      }
    });
  }

  public static void test1() {
    final ArrayList<Para> lista = new ArrayList<Para>(Arrays.asList(
        new Para("abc", 3), new Para("bca", 1), new Para("cab", 2)));
    final ArrayList<Para> oczekiwane = new ArrayList<Para>(Arrays.asList(
        new Para("bca", 1), new Para("cab", 2), new Para("abc", 3)));

    sortujWzgledemLiczb(lista);

    assert lista.equals(oczekiwane);
  }

  public static void test2() {
    final ArrayList<Para> lista = new ArrayList<Para>(Arrays.asList(
        new Para("ab", 3), new Para("abc", 1), new Para("a", 2)));
    final ArrayList<Para> oczekiwane = new ArrayList<Para>(Arrays.asList(
        new Para("a", 2), new Para("ab", 3), new Para("abc", 1)));

    sortujWzgledemDlugosci(lista);

    assert lista.equals(oczekiwane);
  }


  public static void main(String[] args) {

    test1();
    test2();

  }

}
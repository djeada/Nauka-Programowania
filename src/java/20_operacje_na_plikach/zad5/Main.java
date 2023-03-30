/*
Tytul: Znajdz i zmodyfikuj pliki spelniajace warunek.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu.
a) Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych sie w podanym folderze i jego podfolderach.
b) Usun srodkowy wiersz z kazdego pliku CSV znajdujacego sie w podanym folderze i jego podfolderach.
Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
Dane wyjsciowe: Brak.

*/
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

public class Main {

  public static List<String> wczytajPlik(String sciezka) {
    List<String> tresc = new ArrayList<>();
    try {
      String wiersz;
      BufferedReader plik = new BufferedReader(new FileReader(sciezka));

      while ((wiersz = plik.readLine()) != null) {
        tresc.add(wiersz);
      }

      plik.close();
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }

    return tresc;
  }

  public static void sortujAdresyIp(List<String> ip) {
    ip.sort(
        new Comparator<String>() {
          @Override
          public int compare(String lhs, String rhs) {
            int[] oktetA = Stream.of(lhs.split("\\.")).mapToInt(Integer::parseInt).toArray();
            int[] oktetB = Stream.of(rhs.split("\\.")).mapToInt(Integer::parseInt).toArray();

            for (int i = 0; i < oktetA.length; i++) {
              if (oktetA[i] < oktetB[i]) {
                return -1;
              } else if (oktetA[i] > oktetB[i]) {
                return 1;
              }
            }

            return 0;
          }
        });
  }

  public static void test1() throws IOException {
    Path sciezka = Paths.get("temp.txt");

    try (BufferedWriter ofs = new BufferedWriter(new FileWriter(sciezka.toString()))) {
      ofs.write("123.4.245.23\n");
      ofs.write("104.244.253.29\n");
      ofs.write("1.198.3.93\n");
      ofs.write("32.183.93.40\n");
      ofs.write("104.30.244.2\n");
      ofs.write("104.244.4.1\n");
    }

    List<String> adresyIp = wczytajPlik(sciezka.toString());
    sortujAdresyIp(adresyIp);

    List<String> posortowaneAdresy =
        List.of(
            "1.198.3.93",
            "32.183.93.40",
            "104.30.244.2",
            "104.244.4.1",
            "104.244.253.29",
            "123.4.245.23");

    assert adresyIp.equals(posortowaneAdresy);

    Files.deleteIfExists(sciezka);
  }

  public static void main(String[] args) throws IOException {
    test1();
  }
}


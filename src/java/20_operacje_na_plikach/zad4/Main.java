/*
Tytul: Dodaj wiersz do pliku.
Tresc zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke do pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany wiersz na poczatek pliku tekstowego.
Dane wejsciowe: Dwa napisy - sciezka do pliku oraz wiersz tekstu.
Dane wyjsciowe: Brak.

*/
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

  public static void wypiszPlik(String sciezka) {
    try {
      String wiersz;
      BufferedReader plik = new BufferedReader(new FileReader(sciezka));

      while ((wiersz = plik.readLine()) != null) {
        System.out.println(wiersz);
      }

      plik.close();
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static void main(String[] args) {
    String sciezka = "test.txt";

    try (BufferedWriter ofs = new BufferedWriter(new FileWriter(sciezka))) {
      ofs.write("przykladowy tekst.\n");
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }

    wypiszPlik(sciezka);

    try {
      Files.deleteIfExists(Paths.get(sciezka));
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }
}


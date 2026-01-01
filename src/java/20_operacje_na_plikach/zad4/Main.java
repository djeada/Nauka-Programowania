/*
ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.

### Wejście

* 1 linia: `file_path`

### Wyjście

* treść pliku (dokładnie taka jak w pliku)

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\wiadomość.txt
```

**Wyjście:**

```
Witaj! To jest przykładowa treść pliku tekstowego.
```

*/
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

  // Wczytuje i wypisuje zawartość pliku tekstowego linia po linii
  // Złożoność czasowa: O(n) gdzie n to liczba linii w pliku
  // Złożoność pamięciowa: O(1) - czyta linia po linii
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


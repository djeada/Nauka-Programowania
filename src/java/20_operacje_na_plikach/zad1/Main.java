/*
ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.

### Wejście

* 1 linia: `path` (napis — ścieżka)

### Wyjście

* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

**Wyjście:**

```
Prawda
```

*/
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {

  public static boolean czyPlik(String sciezka) {
    try {
      Path obiekt = Paths.get(sciezka);
      return Files.exists(obiekt) && Files.isRegularFile(obiekt);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    return false;
  }

  public static boolean czyFolder(String sciezka) {
    try {
      Path obiekt = Paths.get(sciezka);
      return Files.exists(obiekt) && Files.isDirectory(obiekt);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    return false;
  }

  public static void test1() throws IOException {
    String sciezkaPliku = "temp.txt";
    FileWriter writer = new FileWriter(sciezkaPliku);
    writer.write("przykladowy tekst.\n");
    writer.close();

    assert czyPlik(sciezkaPliku);
    assert !czyFolder(sciezkaPliku);

    Files.delete(Paths.get(sciezkaPliku));
  }

  public static void test2() throws IOException {
    String sciezkaFolderu = "temp_dir";
    try {
      Files.createDirectories(Paths.get(sciezkaFolderu));
    } catch (FileAlreadyExistsException ignored) {
    }

    assert !czyPlik(sciezkaFolderu);
    assert czyFolder(sciezkaFolderu);

    Files.delete(Paths.get(sciezkaFolderu));
  }

  public static void main(String[] args) throws IOException {
    test1();
    test2();
  }
}


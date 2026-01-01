/*
ZAD-11 — Zamień miejscami treści dwóch plików

**Poziom:** ★★☆
**Tagi:** `files`, `swap`, `read/write`

### Treść

Otrzymujesz ścieżki do dwóch plików. Zamień ich treści miejscami:

* plik A ma mieć dawną treść pliku B,
* plik B ma mieć dawną treść pliku A.

### Wejście

* 1 linia: `file_A`
* 2 linia: `file_B`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik1.txt
C:\Users\Username\Documents\plik2.txt
```

**Wyjście:**
*(brak)*

*/
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class Main {

  // Wczytuje wszystkie linie z pliku
  // Złożoność czasowa: O(n) gdzie n to liczba linii
  // Złożoność pamięciowa: O(n)
  public static List<String> readFile(String path) {
    List<String> content = new ArrayList<>();
    try {
      content = Files.readAllLines(Paths.get(path), StandardCharsets.UTF_8);
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
    return content;
  }

  // Kopiuje zawartość pliku źródłowego do docelowego
  // Złożoność czasowa: O(m) gdzie m to rozmiar pliku
  // Złożoność pamięciowa: O(1)
  public static void copyFile(String srcPath, String destPath) {
    try {
      Files.copy(Paths.get(srcPath), Paths.get(destPath), StandardCopyOption.REPLACE_EXISTING);
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  // Zamienia miejscami zawartość dwóch plików
  // Złożoność czasowa: O(m) gdzie m to rozmiar większego pliku
  // Złożoność pamięciowa: O(1)
  public static void swapFiles(String pathA, String pathB) {
    String tempPath = pathB;

    while (Files.exists(Paths.get(tempPath))) {
      tempPath =
          Paths.get(tempPath).getParent().toString() + "/x" + Paths.get(tempPath).getFileName();
    }

    copyFile(pathA, tempPath);
    copyFile(pathB, pathA);
    copyFile(tempPath, pathB);
    try {
      Files.delete(Paths.get(tempPath));
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static void testSwapFiles() throws IOException {
    String testFolderPath = "test";
    Files.createDirectory(Paths.get(testFolderPath));

    String pathA = testFolderPath + "/fileA.txt";
    String pathB = testFolderPath + "/fileB.txt";

    String textA = "Ala ma kota";
    String textB = "Kot ma Ale";

    Files.write(Paths.get(pathA), textA.getBytes(StandardCharsets.UTF_8));
    Files.write(Paths.get(pathB), textB.getBytes(StandardCharsets.UTF_8));

    swapFiles(pathA, pathB);

    assert readFile(pathA).get(0).equals(textB);
    assert readFile(pathB).get(0).equals(textA);

    Files.delete(Paths.get(testFolderPath));
  }

  public static void main(String[] args) throws IOException {
    String pathA = "folder/test.txt";
    String pathB = "folder2/test2.txt";
    swapFiles(pathA, pathB);
  }
}


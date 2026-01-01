/*
ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Otrzymujesz ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze **> 10240 bajtów** w tym folderze i jego podfolderach.

### Wejście

* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\DoUsunięcia
```

**Wyjście:**
*(brak)*

*/
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.*;

public class Main {
  public static long fileSize(String path) {
    try {
      return Files.size(Paths.get(path));
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
      return -1;
    }
  }

  public static void removeFiles(String folderPath) {
    try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(folderPath))) {
      for (Path file : directoryStream) {
        if (fileSize(file.toString()) > 10240) {
          Files.delete(file);
        }
      }
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static void testRemoveFiles() throws IOException {
    String folderPath = "test";
    Files.createDirectory(Paths.get(folderPath));

    String filePath = "test/file.txt";
    try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(filePath))) {
      for (int i = 0; i < 100000; i++) {
        writer.write("test\n");
      }
    }

    removeFiles(folderPath);

    assert Files.list(Paths.get(folderPath)).count() == 0;

    Files.delete(Paths.get(folderPath));
  }

  public static void main(String[] args) throws IOException {
    testRemoveFiles();
  }
}


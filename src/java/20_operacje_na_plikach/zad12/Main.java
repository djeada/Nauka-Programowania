/*
ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `move`, `csv`, `recursive`

### Treść

Otrzymujesz ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki `.csv` z folderu źródłowego **i wszystkich jego podfolderów** do folderu docelowego.

### Wejście

* 1 linia: `src_folder`
* 2 linia: `dst_folder`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Projekty
D:\Dane\CSV
```

**Wyjście:**
*(brak)*

### Uwagi

* Jeśli w folderze docelowym istnieje już plik o tej samej nazwie, zadanie wymaga zdefiniowania zachowania (np. zmiana nazwy / pominięcie) — jeśli sprawdzarka tego nie doprecyzowuje, przyjmij jedną spójną strategię w całym rozwiązaniu.

*/
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;

public class Main {

  public static String getFileName(String path) {
    return Paths.get(path).getFileName().toString();
  }

  public static void moveFile(String srcPath, String destPath) {
    try {
      Files.copy(
          Paths.get(srcPath),
          Paths.get(destPath).resolve(getFileName(srcPath)),
          StandardCopyOption.REPLACE_EXISTING);
      Files.delete(Paths.get(srcPath));
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static String getFileExtension(String path) {
    String fileName = getFileName(path);
    int lastDotIndex = fileName.lastIndexOf(".");
    if (lastDotIndex != -1 && lastDotIndex != 0) {
      return fileName.substring(lastDotIndex);
    } else {
      return "";
    }
  }

  public static void moveFiles(String srcPath, String destPath) throws IOException {
    Files.walk(Paths.get(srcPath))
        .filter(Files::isRegularFile)
        .forEach(
            file -> {
              if (getFileExtension(file.toString()).equals(".csv")) {
                moveFile(file.toString(), destPath);
              }
            });
  }

  public static void testMoveFiles() throws IOException {
    Files.createDirectory(Paths.get("test1"));
    Files.createDirectory(Paths.get("test2"));

    String path1 = "test1/file1.csv";
    String path2 = "test1/file2.csv";

    Files.write(Paths.get(path1), "test1; test2\n".getBytes(StandardCharsets.UTF_8));
    Files.write(Paths.get(path2), "test3; test4\n".getBytes(StandardCharsets.UTF_8));

    moveFiles("test1", "test2");

    assert Files.exists(Paths.get("test2/file1.csv"));
    assert Files.exists(Paths.get("test2/file2.csv"));
    assert !Files.exists(Paths.get("test1/file1.csv"));
    assert !Files.exists(Paths.get("test1/file2.csv"));

    Files.delete(Paths.get("test1"));
    Files.delete(Paths.get("test2"));
  }

  public static void main(String[] args) throws IOException {
    testMoveFiles();
  }
}


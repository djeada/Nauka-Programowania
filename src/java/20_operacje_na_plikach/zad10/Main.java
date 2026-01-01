/*
ZAD-10 — Skopiuj pliki PNG do innego folderu (bez podfolderów)

**Poziom:** ★☆☆
**Tagi:** `files`, `copy`, `png`, `shutil`

### Treść

Otrzymujesz ścieżkę folderu źródłowego i docelowego. Skopiuj wszystkie pliki `.png` znajdujące się **bezpośrednio** w folderze źródłowym do folderu docelowego.

### Wejście

* 1 linia: `src_folder`
* 2 linia: `dst_folder`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Obrazy
D:\Backup\Obrazy
```

**Wyjście:**
*(brak)*

*/
import java.io.IOException;
import java.nio.file.*;

public class Main {
  // Zwraca nazwę pliku ze ścieżki
  // Złożoność czasowa: O(1)
  // Złożoność pamięciowa: O(1)
  public static String fileName(String path) {
    return Paths.get(path).getFileName().toString();
  }

  // Kopiuje plik do folderu docelowego
  // Złożoność czasowa: O(m) gdzie m to rozmiar pliku
  // Złożoność pamięciowa: O(1)
  public static void copyFile(String srcPath, String destFolderPath) {
    String destFilePath = destFolderPath + "/" + fileName(srcPath);
    try {
      Files.copy(Paths.get(srcPath), Paths.get(destFilePath), StandardCopyOption.REPLACE_EXISTING);
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  // Zwraca rozszerzenie pliku
  // Złożoność czasowa: O(n) gdzie n to długość nazwy pliku
  // Złożoność pamięciowa: O(n)
  public static String findExtension(String path) {
    String ext = "";
    int i = path.lastIndexOf('.');
    if (i > 0) {
      ext = path.substring(i);
    }
    return ext;
  }

  // Kopiuje wszystkie pliki .png z folderu źródłowego do docelowego
  // Złożoność czasowa: O(n*m) gdzie n to liczba plików, m to średni rozmiar pliku
  // Złożoność pamięciowa: O(1)
  public static void copyFiles(String srcFolderPath, String destFolderPath) {
    try (DirectoryStream<Path> directoryStream =
        Files.newDirectoryStream(Paths.get(srcFolderPath))) {
      for (Path file : directoryStream) {
        if (findExtension(file.toString()).equals(".png")) {
          copyFile(file.toString(), destFolderPath);
        }
      }
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static void testCopyFiles() throws IOException {
    String folderPath1 = "test1";
    String folderPath2 = "test2";
    Files.createDirectory(Paths.get(folderPath1));
    Files.createDirectory(Paths.get(folderPath2));

    String filePath1 = folderPath1 + "/file1.png";
    String filePath2 = folderPath1 + "/file2.png";
    Files.createFile(Paths.get(filePath1));
    Files.createFile(Paths.get(filePath2));

    copyFiles(folderPath1, folderPath2);

    assert Files.exists(Paths.get(folderPath2 + "/file1.png"));
    assert Files.exists(Paths.get(folderPath2 + "/file2.png"));

    Files.delete(Paths.get(folderPath1));
    Files.delete(Paths.get(folderPath2));
  }

  public static void main(String[] args) throws IOException {
    testCopyFiles();
  }
}


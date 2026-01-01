/*
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

*/
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.List;

public class Main {
  private static class DeletingFileVisitor extends SimpleFileVisitor<Path> {

    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
      Files.delete(file);
      return FileVisitResult.CONTINUE;
    }

    @Override
    public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
      Files.delete(dir);
      return FileVisitResult.CONTINUE;
    }
  }

  public static String znajdzRozszerzenie(String sciezka) {
    Path obiekt = Paths.get(sciezka);

    if (obiekt.getFileName().toString().contains("."))
      return obiekt
          .getFileName()
          .toString()
          .substring(obiekt.getFileName().toString().lastIndexOf("."));

    return "";
  }

  public static List<String> plikiWFolderze(String sciezka, String rozszerzenie) {
    List<String> pliki = new ArrayList<>();

    try {
      Files.newDirectoryStream(Paths.get(sciezka))
          .forEach(
              plik -> {
                if (znajdzRozszerzenie(plik.toString()).equals(rozszerzenie))
                  pliki.add(plik.getFileName().toString());
              });
    } catch (IOException e) {
      e.printStackTrace();
    }

    return pliki;
  }

  public static void test1() throws IOException {
    String sciezka = "temp_dir";
    try {
      Files.createDirectories(Paths.get(sciezka));
    } catch (FileAlreadyExistsException ignored) {
    }

    List<String> nazwyPlikow = List.of("lista.txt", "test.txt");

    for (String nazwa : nazwyPlikow) {
      FileWriter writer = new FileWriter(Paths.get(sciezka, nazwa).toString());
      writer.write("przykladowy tekst.\n");
      writer.close();
    }

    String rozszerzenie = ".txt";
    assert plikiWFolderze(sciezka, rozszerzenie).equals(nazwyPlikow);

    Files.walkFileTree(Paths.get(sciezka), new DeletingFileVisitor());
  }

  public static void main(String[] args) throws IOException {
    test1();
  }
}


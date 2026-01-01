/*
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.

### Wejście

* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

**Wejście:**

```
raport.docx
```

**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

*/

import java.io.FileWriter;
import java.io.IOException;
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

  public static String katalogDomowy() {
    String homeDir = System.getProperty("user.home");
    return homeDir;
  }

  public static List<String> plikiWFolderze(String sciezkaFolderu, String szukanyPlik) {
    List<String> listaSciezek = new ArrayList<>();
    try {
      Files.walkFileTree(
          Paths.get(sciezkaFolderu),
          new SimpleFileVisitor<Path>() {
            @Override
            public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) {
              return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
              if (file.getFileName().toString().equals(szukanyPlik)) {
                listaSciezek.add(file.toString());
              }
              return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult visitFileFailed(Path file, IOException exc) {
              return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult postVisitDirectory(Path dir, IOException exc) {
              return FileVisitResult.CONTINUE;
            }
          });
    } catch (IOException e) {
      e.printStackTrace();
    }

    return listaSciezek;
  }

  public static List<String> sciezkiWSystemie(String szukanyPlik) {
    return plikiWFolderze(katalogDomowy(), szukanyPlik);
  }

  public static void test1() throws IOException {
    String szukanyPlik = "test.txt";

    Path sciezka = Paths.get("temp_dir");
    Files.createDirectories(sciezka);
    Files.createDirectories(sciezka.resolve(sciezka));

    List<String> nazwyPlikow = List.of("lista.txt", szukanyPlik);

    for (String nazwa : nazwyPlikow) {
      FileWriter writer = new FileWriter(sciezka.resolve(nazwa).toString());
      FileWriter writer2 = new FileWriter(sciezka.resolve(sciezka).resolve(nazwa).toString());
      writer.write("przykladowy tekst.\n");
      writer2.write("przykladowy tekst.\n");
      writer.close();
      writer2.close();
    }

    List<String> wynik = sciezkiWSystemie(szukanyPlik);

    assert wynik.contains(sciezka.resolve(szukanyPlik).toAbsolutePath().normalize().toString());
    assert wynik.contains(
        sciezka.resolve(sciezka).resolve(szukanyPlik).toAbsolutePath().normalize().toString());

    Files.walkFileTree(sciezka, new DeletingFileVisitor());
  }

  public static void main(String[] args) throws IOException {
    test1();
  }
}


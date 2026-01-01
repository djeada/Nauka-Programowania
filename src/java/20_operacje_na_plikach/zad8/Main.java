/*
ZAD-08 — Modyfikacja plików spełniających warunek (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `recursive`, `txt`, `csv`

### Treść

Otrzymujesz ścieżkę do folderu. Wykonaj:

a) dopisz swoje inicjały na końcu każdego pliku `.txt` w folderze i podfolderach,
b) usuń **środkowy wiersz** z każdego pliku `.csv` w folderze i podfolderach
(jeśli liczba wierszy jest parzysta — usuń **dolny z dwóch środkowych**).

### Wejście

* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\Projekt
```

**Wyjście:**
*(brak)*

*/

import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
  public static String findExtension(String path) {
    Path object = Paths.get(path);

    if (Files.isRegularFile(object) && object.getFileName().toString().contains("."))
      return object
          .getFileName()
          .toString()
          .substring(object.getFileName().toString().lastIndexOf('.'));

    return "";
  }

  public static List<String> filesInFolder(String folderPath, String extension) {
    List<String> files = new ArrayList<>();

    try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(folderPath))) {
      for (Path file : directoryStream) {
        if (findExtension(file.toString()).equals(extension)) files.add(file.toString());
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    return files;
  }

  public static void addInitials(String folderPath, String data) {
    List<String> paths = filesInFolder(folderPath, ".txt");

    for (String path : paths) {
      try (FileWriter fileWriter = new FileWriter(path, true);
          BufferedWriter bufferedWriter = new BufferedWriter(fileWriter)) {
        bufferedWriter.write("\n" + data);
      } catch (IOException e) {
        System.out.println("Error: " + e.getMessage());
      }
    }
  }

  public static List<String> readFile(String filePath) {
    List<String> content = new ArrayList<>();

    try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
      String line;
      while ((line = reader.readLine()) != null) {
        content.add(line);
      }
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }

    return content;
  }

  public static void removeMiddle(String folderPath) {
    List<String> paths = filesInFolder(folderPath, ".csv");

    for (String path : paths) {
      List<String> fileContent = readFile(path);

      if (fileContent.size() > 0) {
        fileContent.remove(fileContent.size() / 2);
      }

      try (BufferedWriter writer = new BufferedWriter(new FileWriter(path))) {
        for (String line : fileContent) {
          writer.write(line + "\n");
        }
      } catch (IOException e) {
        System.out.println("Error: " + e.getMessage());
      }
    }
  }

  public static void testAddInitials() throws IOException {
    Path folderPath = Paths.get("temp_dir");
    Files.createDirectories(folderPath);

    String txtFile = "temp.txt";
    try (BufferedWriter writer = Files.newBufferedWriter(folderPath.resolve(txtFile))) {
      writer.write("example text\n");
    }

    String data = "A.D.";
    addInitials(folderPath.toString(), data);

    List<String> expectedResult = new ArrayList<>();
    expectedResult.add("example text");
    expectedResult.add("A.D.");

    assert readFile(folderPath.resolve(txtFile).toString()).equals(expectedResult);

    Files.delete(folderPath.resolve(txtFile));
    Files.delete(folderPath);
  }

  public static void testRemoveMiddle() throws IOException {
    Path folderPath = Paths.get("temp_dir");
    Files.createDirectories(folderPath);

    String csvFile = "temp.csv";
    try (BufferedWriter writer = Files.newBufferedWriter(folderPath.resolve(csvFile))) {
      writer.write("test1; test2; test3\n");
      writer.write("test4; test5; test6\n");
      writer.write("test7; test8; test9\n");
    }

    removeMiddle(folderPath.toString());

    List<String> expectedResult = new ArrayList<>();
    expectedResult.add("test1; test2; test3");
    expectedResult.add("test7; test8; test9");

    assert readFile(folderPath.resolve(csvFile).toString()).equals(expectedResult);

    Files.delete(folderPath.resolve(csvFile));
    Files.delete(folderPath);
  }

  public static void main(String[] args) throws IOException {
    testAddInitials();
    testRemoveMiddle();
  }
}


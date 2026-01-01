/*
ZAD-07 — Dodaj wiersz na początku pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `write`, `prepend`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego i wiersz tekstu. Dodaj ten wiersz na **początku** pliku.

### Wejście

* 1 linia: `file_path`
* 2 linia: `line_to_add` (może zawierać spacje)

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

**Wyjście:**
*(brak)*

*/
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {

  // Wczytuje wszystkie linie z pliku
  // Złożoność czasowa: O(n) gdzie n to liczba linii
  // Złożoność pamięciowa: O(n)
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

  // Dodaje wiersz na początku pliku
  // Złożoność czasowa: O(n) gdzie n to liczba linii w pliku
  // Złożoność pamięciowa: O(n)
  public static void writeAtBeginning(String filePath, String data) {
    List<String> fileContent = readFile(filePath);

    try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
      writer.write(data);
      for (String line : fileContent) {
        writer.write(line + "\n");
      }
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static void test1() throws IOException {
    Path path = Paths.get("temp.txt");

    try (BufferedWriter writer = Files.newBufferedWriter(path)) {
      writer.write("example text\n");
    }

    writeAtBeginning(path.toString(), "Hey \n");
    List<String> expectedResult = new ArrayList<>();
    expectedResult.add("Hey ");
    expectedResult.add("example text");

    assert readFile(path.toString()).equals(expectedResult);

    Files.delete(path);
  }

  public static void main(String[] args) throws IOException {
    test1();
  }
}


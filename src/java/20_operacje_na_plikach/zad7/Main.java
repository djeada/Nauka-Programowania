/*
Tytul: Skopiuj pliki.
Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Skopiuj wszystkie pliki PNG z pierwszego folderu do drugiego folderu.
Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
Dane wyjsciowe: Brak.

*/
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {

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


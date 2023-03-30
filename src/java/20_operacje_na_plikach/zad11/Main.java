/*
Tytul: Znalezienie sciezki pliku o danej nazwie
Tresc: Otrzymujesz napis reprezentujacy nazwe pliku. Przeszukaj caly system i zapisz w liscie wszystkie sciezki plikow o podanej nazwie.
Dane wejsciowe: Napis
Dane wyjsciowe: Lista napisow

*/
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class Main {

  public static List<String> readFile(String path) {
    List<String> content = new ArrayList<>();
    try {
      content = Files.readAllLines(Paths.get(path), StandardCharsets.UTF_8);
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
    return content;
  }

  public static void copyFile(String srcPath, String destPath) {
    try {
      Files.copy(Paths.get(srcPath), Paths.get(destPath), StandardCopyOption.REPLACE_EXISTING);
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

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


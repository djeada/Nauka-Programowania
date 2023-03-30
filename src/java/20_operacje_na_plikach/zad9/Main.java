/*
Tytul: Przesun wszystkie pliki CSV do jednego folderu.
Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Przenies wszystkie pliki CSV z pierwszego folderu (oraz jego podfolderow) do drugiego folderu.
Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
Dane wyjsciowe: Brak.

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


/*
Tytul: Znalezienie w folderze wszystkich plikow z danym rozszerzeniem
Tresc: Otrzymujesz dwa napisy. Pierwszy napis to sciezka folderu, a drugi to rozszerzenie szukanych plikow. Znajdz w folderze wszystkie pliki o podanym rozszerzeniu i zapisz ich nazwy w liscie.
Dane wejsciowe: Dwa napisy
Dane wyjsciowe: Lista napisow

*/
import java.io.IOException;
import java.nio.file.*;

public class Main {
  public static String fileName(String path) {
    return Paths.get(path).getFileName().toString();
  }

  public static void copyFile(String srcPath, String destFolderPath) {
    String destFilePath = destFolderPath + "/" + fileName(srcPath);
    try {
      Files.copy(Paths.get(srcPath), Paths.get(destFilePath), StandardCopyOption.REPLACE_EXISTING);
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public static String findExtension(String path) {
    String ext = "";
    int i = path.lastIndexOf('.');
    if (i > 0) {
      ext = path.substring(i);
    }
    return ext;
  }

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


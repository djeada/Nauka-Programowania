/*
Tytul: Sprawdzenie, czy sciezka nalezy do pliku/folderu
Tresc: Otrzymujesz napis reprezentujacy sciezke. Sprawdz, czy jest to sciezka do pliku lub folderu.
Dane wejsciowe: Napis
Dane wyjsciowe: Wartosc logiczna

*/
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {

  public static boolean czyPlik(String sciezka) {
    try {
      Path obiekt = Paths.get(sciezka);
      return Files.exists(obiekt) && Files.isRegularFile(obiekt);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    return false;
  }

  public static boolean czyFolder(String sciezka) {
    try {
      Path obiekt = Paths.get(sciezka);
      return Files.exists(obiekt) && Files.isDirectory(obiekt);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    return false;
  }

  public static void test1() throws IOException {
    String sciezkaPliku = "temp.txt";
    FileWriter writer = new FileWriter(sciezkaPliku);
    writer.write("przykladowy tekst.\n");
    writer.close();

    assert czyPlik(sciezkaPliku);
    assert !czyFolder(sciezkaPliku);

    Files.delete(Paths.get(sciezkaPliku));
  }

  public static void test2() throws IOException {
    String sciezkaFolderu = "temp_dir";
    try {
      Files.createDirectories(Paths.get(sciezkaFolderu));
    } catch (FileAlreadyExistsException ignored) {
    }

    assert !czyPlik(sciezkaFolderu);
    assert czyFolder(sciezkaFolderu);

    Files.delete(Paths.get(sciezkaFolderu));
  }

  public static void main(String[] args) throws IOException {
    test1();
    test2();
  }
}


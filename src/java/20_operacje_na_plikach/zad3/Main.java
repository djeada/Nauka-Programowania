/*
Tytul: Statystyki dla pliku tekstowego.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Oblicz:
a) Liczbe wierszy w pliku.
b) Liczbe slow w pliku (slowa oddzielone sa spacjami i moga skladac sie wylacznie z liter).
c) Srednia dlugosc wiersza.
d) Srednia liczbe slow na wiersz.
e) Czestosc wystepowania kazdego ze slow w pliku.
Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
Dane wyjsciowe:
a) Liczba naturalna reprezentujaca liczbe wierszy.
b) Liczba naturalna reprezentujaca liczbe slow.
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza.
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz.
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa).
Przyklad:
Dla otrzymanego napisu: "C:\Users\Username\Documents\text_file.txt" powinno zostac zwrocone:
a) Liczba naturalna reprezentujaca liczbe wierszy, np. 6
b) Liczba naturalna reprezentujaca liczbe slow, np. 25
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza, np. 41.5
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz, np. 4.2
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa): {'The': 2, 'quick': 2, 'brown': 2, 'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1, 'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1, 'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1, 'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1, 'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1, 'ten': 1, 'lines': 1, 'and': 1, 'words.': 1}
Tekst pliku:
The quick brown fox jumped over the lazy dog.
The quick brown cat sat on the mat.
Foxes are known for their cunning and intelligence.
Dogs are known for their loyalty and kindness.
Cats are independent animals but can be affectionate.
This text file contains six lines and 25 words.

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


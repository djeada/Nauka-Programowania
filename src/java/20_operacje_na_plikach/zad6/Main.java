/*
ZAD-06 — Statystyki pliku tekstowego

**Poziom:** ★★☆
**Tagi:** `files`, `stats`, `dict`, `regex`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Oblicz:

a) liczbę wierszy,
b) łączną liczbę słów (słowa = ciągi liter),
c) średnią długość wiersza (w znakach),
d) średnią liczbę słów na wiersz,
e) częstość występowania słów (słownik).

### Wejście

* 1 linia: `file_path`

### Wyjście

5 elementów w tej kolejności:

1. liczba wierszy
2. liczba słów
3. średnia długość wiersza
4. średnia liczba słów na wiersz
5. słownik częstości słów

Każdy element wypisz w osobnej linii.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\tekst.txt
```

**Wyjście:**

```
4
12
17.75
3.0
{'ala': 2, 'ma': 2, 'kota': 1, 'kot': 1, 'na': 1, 'imię': 1, 'filemon': 1, 'filemona': 1, 'lubi': 2, 'mleko': 1}
```

### Uwagi o formatowaniu

* Jeżeli ujednolicisz wielkość liter — w słowniku używaj małych liter (jak w przykładzie).
* Interpunkcję traktuj jako separator (usuń ją przy wyznaczaniu słów).

*/

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

  // Wczytuje wszystkie linie z pliku do listy
  // Złożoność czasowa: O(n) gdzie n to liczba linii
  // Złożoność pamięciowa: O(n)
  static List<String> readFile(String path) {
    List<String> content = new ArrayList<>();
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
      String line;
      while ((line = br.readLine()) != null) {
        content.add(line);
      }
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
    return content;
  }

  // Usuwa znaki interpunkcyjne ze słowa
  // Złożoność czasowa: O(n) gdzie n to długość słowa
  // Złożoność pamięciowa: O(n)
  static String clean(String word) {
    return word.replaceAll("\\p{Punct}", "");
  }

  static String toLowerCase(String word) {
    return word.toLowerCase();
  }

  static List<String> splitWords(String line) {
    List<String> words = new ArrayList<>();
    for (String word : line.split("\\s+")) {
      String cleanedWord = clean(toLowerCase(word));
      if (!cleanedWord.isEmpty()) {
        words.add(cleanedWord);
      }
    }
    return words;
  }

  static int numberOfLines(List<String> content) {
    return content.size();
  }

  static int numberOfWords(List<String> content) {
    int result = 0;
    for (String line : content) {
      result += splitWords(line).size();
    }
    return result;
  }

  static double averageLineLength(List<String> content) {
    int totalLength = 0;
    for (String line : content) {
      totalLength += line.length();
    }
    return totalLength / (double) content.size();
  }

  static double averageWordsPerLine(List<String> content) {
    return numberOfWords(content) / (double) numberOfLines(content);
  }

  static String listToString(List<String> list) {
    return list.stream().collect(Collectors.joining());
  }

  static Map<String, Integer> wordHistogram(String content) {
    Map<String, Integer> wordFrequency = new HashMap<>();
    List<String> words = splitWords(content);

    for (String word : words) {
      wordFrequency.put(word, wordFrequency.getOrDefault(word, 0) + 1);
    }
    return wordFrequency;
  }

  static void test1() throws IOException {
    Path path = Files.createTempFile("temp", ".txt");
    try (BufferedWriter bw = Files.newBufferedWriter(path)) {
      bw.write("Hej \n");
      bw.write(
          "This is an example of a simple ASCII text file stored on a Web "
              + "server. Note that it has a file\n");
      bw.write("extension of \".txt\".\n\n");
      bw.write(
          "Although such files may contains some basic layout formatting, such "
              + "as paragraphs, there is no\n");
      bw.write("support for the text to have attributes, such as bolding.\n\n");
      bw.write(
          "Text files can contain Hypertext Mark-up codes but these will not be "
              + "interpreted by the \n");
      bw.write(
          "browser. For example, if the following characters "
              + "<strong>hello</strong> were typed into an\n");
      bw.write("\"html\" file then the word \"hello\" would be shown in bold.\n");
    }

    List<String> content = readFile(path.toString());
    String text = listToString(content);

    int expectedNumberOfLines = 10;
    assert numberOfLines(content) == expectedNumberOfLines;

    int expectedNumberOfWords = 88;
    assert numberOfWords(content) == expectedNumberOfWords;

    double expectedAverageLineLength = 60.0;
    assert averageLineLength(content) == expectedAverageLineLength;

    double expectedAverageWordsPerLine = 8.8;
    assert averageWordsPerLine(content) == expectedAverageWordsPerLine;

    Map<String, Integer> expectedWordHistogram = new HashMap<>();
    expectedWordHistogram.put("bold", 1);
    expectedWordHistogram.put("in", 1);
    expectedWordHistogram.put("shown", 1);
    expectedWordHistogram.put("word", 1);
    expectedWordHistogram.put("then", 1);
    expectedWordHistogram.put("anhtml", 1);
    expectedWordHistogram.put("simple", 1);
    expectedWordHistogram.put("basic", 1);
    expectedWordHistogram.put("contains", 1);
    expectedWordHistogram.put("layout", 1);
    expectedWordHistogram.put("were", 1);
    expectedWordHistogram.put("may", 1);
    expectedWordHistogram.put("such", 3);
    expectedWordHistogram.put("fileextension", 1);
    expectedWordHistogram.put("files", 2);
    expectedWordHistogram.put("it", 1);
    expectedWordHistogram.put("hypertext", 1);
    expectedWordHistogram.put("hello", 1);
    expectedWordHistogram.put("note", 1);
    expectedWordHistogram.put("file", 2);
    expectedWordHistogram.put("web", 1);
    expectedWordHistogram.put("ascii", 1);
    expectedWordHistogram.put("is", 2);
    expectedWordHistogram.put("an", 1);
    expectedWordHistogram.put("example", 2);
    expectedWordHistogram.put("hej", 1);
    expectedWordHistogram.put("following", 1);
    expectedWordHistogram.put("this", 1);
    expectedWordHistogram.put("of", 2);
    expectedWordHistogram.put("txtalthough", 1);
    expectedWordHistogram.put("text", 2);
    expectedWordHistogram.put("stored", 1);
    expectedWordHistogram.put("that", 1);
    expectedWordHistogram.put("by", 1);
    expectedWordHistogram.put("on", 1);
    expectedWordHistogram.put("formatting", 1);
    expectedWordHistogram.put("nosupport", 1);
    expectedWordHistogram.put("browser", 1);
    expectedWordHistogram.put("typed", 1);
    expectedWordHistogram.put("a", 3);
    expectedWordHistogram.put("server", 1);
    expectedWordHistogram.put("would", 1);
    expectedWordHistogram.put("contain", 1);
    expectedWordHistogram.put("as", 2);
    expectedWordHistogram.put("markup", 1);
    expectedWordHistogram.put("characters", 1);
    expectedWordHistogram.put("there", 1);
    expectedWordHistogram.put("for", 2);
    expectedWordHistogram.put("the", 4);
    expectedWordHistogram.put("to", 1);
    expectedWordHistogram.put("have", 1);
    expectedWordHistogram.put("these", 1);
    expectedWordHistogram.put("will", 1);
    expectedWordHistogram.put("paragraphs", 1);
    expectedWordHistogram.put("attributes", 1);
    expectedWordHistogram.put("boldingtext", 1);
    expectedWordHistogram.put("can", 1);
    expectedWordHistogram.put("has", 1);
    expectedWordHistogram.put("codes", 1);
    expectedWordHistogram.put("if", 1);
    expectedWordHistogram.put("some", 1);
    expectedWordHistogram.put("but", 1);
    expectedWordHistogram.put("not", 1);
    expectedWordHistogram.put("be", 2);
    expectedWordHistogram.put("interpreted", 1);
    expectedWordHistogram.put("stronghellostrong", 1);
    expectedWordHistogram.put("into", 1);

    Map<String, Integer> wordHistogram = wordHistogram(text);
    for (String word : expectedWordHistogram.keySet()) {
      assert wordHistogram.get(word) == expectedWordHistogram.get(word);
    }
  }

  public static void main(String[] args) throws IOException {
    test1();
  }
}


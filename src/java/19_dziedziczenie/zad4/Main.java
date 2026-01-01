/*
ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `konstruktory`, `super`

### Treść

Zaprojektuj hierarchię klas:

1. **Człowiek** — pola:

   * imię
   * nazwisko
   * miejsce urodzenia
   * zawód

2. **Student** (dziedziczy po `Człowiek`) — dodatkowo:

   * numer albumu
   * kierunek studiów

3. **StudentFizyki** (dziedziczy po `Student`) — dodatkowo:

   * średnia z laboratoriów
   * średnia z wykładów

Program:

* wczytuje dane dla trzech obiektów (Człowiek, Student, StudentFizyki),
* tworzy obiekty,
* wypisuje je w formacie jak w przykładzie.

**Uwaga do wejścia:** wszystko w osobnych liniach, w podanej kolejności.

### Wejście

**Dane dla Człowiek:**

1. imię
2. nazwisko
3. miejsce urodzenia
4. zawód

**Dane dla Student:**
5. imię
6. nazwisko
7. miejsce urodzenia
8. zawód
9. numer albumu (int)
10. kierunek studiów

**Dane dla StudentFizyki:**
11. imię
12. nazwisko
13. miejsce urodzenia
14. zawód
15. numer albumu (int)
16. kierunek studiów
17. średnia z laboratoriów (float)
18. średnia z wykładów (float)

### Wyjście

Trzy bloki jak w przykładzie, oddzielone pustą linią.

### Przykład

**Wejście:**

```
Jan
Kowalski
Kraków
Inżynier
Anna
Nowak
Warszawa
Student
12345
Informatyka
Piotr
Wiśniewski
Gdańsk
Student
54321
Fizyka
4.5
4.0
```

**Wyjście:**

```
Człowiek:
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Kraków
Zawód: Inżynier

Student:
Imię: Anna
Nazwisko: Nowak
Miejsce urodzenia: Warszawa
Zawód: Student
Numer albumu: 12345
Kierunek studiów: Informatyka

Student Fizyki:
Imię: Piotr
Nazwisko: Wiśniewski
Miejsce urodzenia: Gdańsk
Zawód: Student
Numer albumu: 54321
Kierunek studiów: Fizyka
Średnia z laboratoriów: 4.5
Średnia z wykładów: 4.0
```

*/
import java.util.Scanner;

public class Main {
  private static class Czlowiek {

    public String imie = "";
    public String nazwisko = "";
    public String miejsceUrodzenia = "";
    public String zawod = "";

    public Czlowiek(String imie, String nazwisko, String miejsceUrodzenia, String zawod) {
      this.imie = imie;
      this.nazwisko = nazwisko;
      this.miejsceUrodzenia = miejsceUrodzenia;
      this.zawod = zawod;
    }

    public void wypisz() {
      System.out.println("Człowiek:");
      System.out.println("Imię: " + imie);
      System.out.println("Nazwisko: " + nazwisko);
      System.out.println("Miejsce urodzenia: " + miejsceUrodzenia);
      System.out.println("Zawód: " + zawod);
    }
  }

  private static class Student extends Czlowiek {

    protected int numerAlbumu;
    protected String kierunekStudiow = "";

    public Student(
        String imie,
        String nazwisko,
        String miejsceUrodzenia,
        String zawod,
        int numerAlbumu,
        String kierunekStudiow) {
      super(imie, nazwisko, miejsceUrodzenia, zawod);
      this.numerAlbumu = numerAlbumu;
      this.kierunekStudiow = kierunekStudiow;
    }

    @Override
    public void wypisz() {
      System.out.println("Student:");
      System.out.println("Imię: " + imie);
      System.out.println("Nazwisko: " + nazwisko);
      System.out.println("Miejsce urodzenia: " + miejsceUrodzenia);
      System.out.println("Zawód: " + zawod);
      System.out.println("Numer albumu: " + numerAlbumu);
      System.out.println("Kierunek studiów: " + kierunekStudiow);
    }
  }

  private static class StudentFizyki extends Student {

    private double sredniaLaboratoria;
    private double sredniaWyklady;

    public StudentFizyki(
        String imie,
        String nazwisko,
        String miejsceUrodzenia,
        String zawod,
        int numerAlbumu,
        String kierunekStudiow,
        double sredniaLaboratoria,
        double sredniaWyklady) {
      super(imie, nazwisko, miejsceUrodzenia, zawod, numerAlbumu, kierunekStudiow);
      this.sredniaLaboratoria = sredniaLaboratoria;
      this.sredniaWyklady = sredniaWyklady;
    }

    @Override
    public void wypisz() {
      System.out.println("Student Fizyki:");
      System.out.println("Imię: " + imie);
      System.out.println("Nazwisko: " + nazwisko);
      System.out.println("Miejsce urodzenia: " + miejsceUrodzenia);
      System.out.println("Zawód: " + zawod);
      System.out.println("Numer albumu: " + numerAlbumu);
      System.out.println("Kierunek studiów: " + kierunekStudiow);
      System.out.println("Średnia z laboratoriów: " + sredniaLaboratoria);
      System.out.println("Średnia z wykładów: " + sredniaWyklady);
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    // Read data for Człowiek
    String imie1 = scanner.nextLine();
    String nazwisko1 = scanner.nextLine();
    String miejsceUrodzenia1 = scanner.nextLine();
    String zawod1 = scanner.nextLine();
    
    // Read data for Student
    String imie2 = scanner.nextLine();
    String nazwisko2 = scanner.nextLine();
    String miejsceUrodzenia2 = scanner.nextLine();
    String zawod2 = scanner.nextLine();
    int numerAlbumu2 = Integer.parseInt(scanner.nextLine());
    String kierunekStudiow2 = scanner.nextLine();
    
    // Read data for StudentFizyki
    String imie3 = scanner.nextLine();
    String nazwisko3 = scanner.nextLine();
    String miejsceUrodzenia3 = scanner.nextLine();
    String zawod3 = scanner.nextLine();
    int numerAlbumu3 = Integer.parseInt(scanner.nextLine());
    String kierunekStudiow3 = scanner.nextLine();
    double sredniaLaboratoria3 = Double.parseDouble(scanner.nextLine());
    double sredniaWyklady3 = Double.parseDouble(scanner.nextLine());
    
    // Create objects
    Czlowiek czlowiek = new Czlowiek(imie1, nazwisko1, miejsceUrodzenia1, zawod1);
    Student student = new Student(imie2, nazwisko2, miejsceUrodzenia2, zawod2, numerAlbumu2, kierunekStudiow2);
    StudentFizyki studentFizyki = new StudentFizyki(imie3, nazwisko3, miejsceUrodzenia3, zawod3, numerAlbumu3, kierunekStudiow3, sredniaLaboratoria3, sredniaWyklady3);
    
    // Print objects
    czlowiek.wypisz();
    System.out.println();
    student.wypisz();
    System.out.println();
    studentFizyki.wypisz();
    
    scanner.close();
  }
}


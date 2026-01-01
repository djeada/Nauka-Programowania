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

    public final String getImie() {
      return imie;
    }

    public final String getNazwisko() {
      return nazwisko;
    }

    public final String getMiejsceUrodzenia() {
      return miejsceUrodzenia;
    }

    public final String getZawod() {
      return zawod;
    }
  }

  private static class Student extends Czlowiek {

    protected int numerAlbumu;
    protected String kierunekStudiow = "";

    public Student(
        String imie,
        String nazwisko,
        String miejsceUrodzenia,
        int numerAlbumu,
        String kierunekStudiow) {
      super(imie, nazwisko, miejsceUrodzenia, "Student");
      this.numerAlbumu = numerAlbumu;
      this.kierunekStudiow = kierunekStudiow;
    }

    public final int getNumerAlbumu() {
      return numerAlbumu;
    }

    public final String getKierunekStudiow() {
      return kierunekStudiow;
    }
  }

  private static class StudentFizyki extends Student {

    private double sredniaLaboratoria;
    private double sredniaWyklady;

    public StudentFizyki(
        String imie,
        String nazwisko,
        String miejsceUrodzenia,
        int numerAlbumu,
        double sredniaLaboratoria,
        double sredniaWyklady) {
      super(imie, nazwisko, miejsceUrodzenia, numerAlbumu, "Fizyka");
      this.sredniaLaboratoria = sredniaLaboratoria;
      this.sredniaWyklady = sredniaWyklady;
    }

    public final double getSredniaLaboratoria() {
      return sredniaLaboratoria;
    }

    public final double getSredniaWyklady() {
      return sredniaWyklady;
    }
  }

  public static void test1() {
    final String imie = "Jan";
    final String nazwisko = "Kowalski";
    final String miejsceUrodzenia = "Warszawa";
    final String zawod = "Profesor";

    Czlowiek czlowiek = new Czlowiek(imie, nazwisko, miejsceUrodzenia, zawod);

    assert imie.equals(czlowiek.getImie());
    assert nazwisko.equals(czlowiek.getNazwisko());
    assert miejsceUrodzenia.equals(czlowiek.getMiejsceUrodzenia());
    assert zawod.equals(czlowiek.getZawod());
  }

  public static void test2() {
    final String imie = "Jan";
    final String nazwisko = "Kowalski";
    final String miejsceUrodzenia = "Warszawa";
    final String zawod = "Student";
    final int numerAlbumu = 271932;
    final String kierunekStudiow = "Fizyka";

    Student student = new Student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, kierunekStudiow);

    assert imie.equals(student.getImie());
    assert nazwisko.equals(student.getNazwisko());
    assert miejsceUrodzenia.equals(student.getMiejsceUrodzenia());
    assert zawod.equals(student.getZawod());
    assert student.getNumerAlbumu() == numerAlbumu;
    assert kierunekStudiow.equals(student.getKierunekStudiow());
  }

  public static void test3() {
    final String imie = "Jan";
    final String nazwisko = "Kowalski";
    final String miejsceUrodzenia = "Warszawa";
    final String zawod = "Student";
    final int numerAlbumu = 271932;
    final String kierunekStudiow = "Fizyka";
    final double sredniaLaboratoria = 3.82;
    final double sredniaWyklady = 4.56;

    StudentFizyki student =
        new StudentFizyki(
            imie, nazwisko, miejsceUrodzenia, numerAlbumu, sredniaLaboratoria, sredniaWyklady);

    assert imie.equals(student.getImie());
    assert nazwisko.equals(student.getNazwisko());
    assert miejsceUrodzenia.equals(student.getMiejsceUrodzenia());
    assert zawod.equals(student.getZawod());
    assert student.getNumerAlbumu() == numerAlbumu;
    assert kierunekStudiow.equals(student.getKierunekStudiow());
    assert student.getSredniaLaboratoria() == sredniaLaboratoria;
    assert student.getSredniaWyklady() == sredniaWyklady;
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}


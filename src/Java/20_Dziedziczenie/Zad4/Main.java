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

    public Student(String imie, String nazwisko, String miejsceUrodzenia, int numerAlbumu, String kierunekStudiow) {
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

    public StudentFizyki(String imie, String nazwisko, String miejsceUrodzenia, int numerAlbumu, double sredniaLaboratoria, double sredniaWyklady) {
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

    StudentFizyki student = new StudentFizyki(imie, nazwisko, miejsceUrodzenia, numerAlbumu, sredniaLaboratoria, sredniaWyklady);

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
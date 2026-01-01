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

#include <cassert>
#include <string>

class Czlowiek {
 public:
  std::string imie;
  std::string nazwisko;
  std::string miejsceUrodzenia;
  std::string zawod;

 public:
  Czlowiek(std::string imie, std::string nazwisko, std::string miejsceUrodzenia,
           std::string zawod)
      : imie(imie),
        nazwisko(nazwisko),
        miejsceUrodzenia(miejsceUrodzenia),
        zawod(zawod) {}

  std::string getImie() { return imie; }

  std::string getNazwisko() { return nazwisko; }

  std::string getMiejsceUrodzenia() { return miejsceUrodzenia; }

  std::string getZawod() { return zawod; }
};

class Student : public Czlowiek {
 protected:
  int numerAlbumu;
  std::string kierunekStudiow;

 public:
  Student(std::string imie, std::string nazwisko, std::string miejsceUrodzenia,
          int numerAlbumu, std::string kierunekStudiow)
      : Czlowiek(imie, nazwisko, miejsceUrodzenia, "Student"),
        numerAlbumu(numerAlbumu),
        kierunekStudiow(kierunekStudiow) {}

  int getNumerAlbumu() { return numerAlbumu; }

  std::string getKierunekStudiow() { return kierunekStudiow; }
};

class StudentFizyki : public Student {
 private:
  double sredniaLaboratoria;
  double sredniaWyklady;

 public:
  StudentFizyki(std::string imie, std::string nazwisko,
                std::string miejsceUrodzenia, int numerAlbumu,
                double sredniaLaboratoria, double sredniaWyklady)
      : Student(imie, nazwisko, miejsceUrodzenia, numerAlbumu, "Fizyka"),
        sredniaLaboratoria(sredniaLaboratoria),
        sredniaWyklady(sredniaWyklady) {}

  double getSredniaLaboratoria() { return sredniaLaboratoria; }

  double getSredniaWyklady() { return sredniaWyklady; }
};

void test1() {
  const std::string imie = "Jan";
  const std::string nazwisko = "Kowalski";
  const std::string miejsceUrodzenia = "Warszawa";
  const std::string zawod = "Profesor";

  Czlowiek czlowiek(imie, nazwisko, miejsceUrodzenia, zawod);

  assert(czlowiek.getImie() == imie);
  assert(czlowiek.getNazwisko() == nazwisko);
  assert(czlowiek.getMiejsceUrodzenia() == miejsceUrodzenia);
  assert(czlowiek.getZawod() == zawod);
}

void test2() {
  const std::string imie = "Jan";
  const std::string nazwisko = "Kowalski";
  const std::string miejsceUrodzenia = "Warszawa";
  const std::string zawod = "Student";
  const int numerAlbumu = 271932;
  const std::string kierunekStudiow = "Fizyka";

  Student student(imie, nazwisko, miejsceUrodzenia, numerAlbumu,
                  kierunekStudiow);

  assert(student.getImie() == imie);
  assert(student.getNazwisko() == nazwisko);
  assert(student.getMiejsceUrodzenia() == miejsceUrodzenia);
  assert(student.getZawod() == zawod);
  assert(student.getNumerAlbumu() == numerAlbumu);
  assert(student.getKierunekStudiow() == kierunekStudiow);
}

void test3() {
  const std::string imie = "Jan";
  const std::string nazwisko = "Kowalski";
  const std::string miejsceUrodzenia = "Warszawa";
  const std::string zawod = "Student";
  const int numerAlbumu = 271932;
  const std::string kierunekStudiow = "Fizyka";
  const double sredniaLaboratoria = 3.82;
  const double sredniaWyklady = 4.56;

  StudentFizyki student(imie, nazwisko, miejsceUrodzenia, numerAlbumu,
                        sredniaLaboratoria, sredniaWyklady);

  assert(student.getImie() == imie);
  assert(student.getNazwisko() == nazwisko);
  assert(student.getMiejsceUrodzenia() == miejsceUrodzenia);
  assert(student.getZawod() == zawod);
  assert(student.getNumerAlbumu() == numerAlbumu);
  assert(student.getKierunekStudiow() == kierunekStudiow);
  assert(student.getSredniaLaboratoria() == sredniaLaboratoria);
  assert(student.getSredniaWyklady() == sredniaWyklady);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}

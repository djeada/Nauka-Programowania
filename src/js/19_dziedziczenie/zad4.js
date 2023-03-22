/*
Tytuł: Dziedziczenie wielopoziomowe

Treść: Napisz klasę Człowiek oraz klasy pochodne Student i StudentFizyki. Człowiek powinien zawierać informacje o imieniu, nazwisku, miejscu urodzenia i zawodzie. Student powinien dodawać pola numeru albumu oraz kierunku studiów. StudentFizyki powinien dodawać pola średniej z laboratoriów oraz średniej z wykładów. Napisz program testujący te klasy.
*/

class Czlowiek {
  constructor(imie, nazwisko, miejsceUrodzenia, zawod) {
    this.imie = imie;
    this.nazwisko = nazwisko;
    this.miejsceUrodzenia = miejsceUrodzenia;
    this.zawod = zawod;
  }
}

class Student extends Czlowiek {
  constructor(
    imie,
    nazwisko,
    miejsceUrodzenia,
    zawod,
    numerAlbumu,
    kierunekStudiow
  ) {
    super(imie, nazwisko, miejsceUrodzenia, zawod);
    this.numerAlbumu = numerAlbumu;
    this.kierunekStudiow = kierunekStudiow;
  }
}

class StudentFizyki extends Student {
  constructor(
    imie,
    nazwisko,
    miejsceUrodzenia,
    zawod,
    numerAlbumu,
    kierunekStudiow,
    sredniaZLaboratoriow,
    sredniaZWykladow
  ) {
    super(
      imie,
      nazwisko,
      miejsceUrodzenia,
      zawod,
      numerAlbumu,
      kierunekStudiow
    );
    this.sredniaZLaboratoriow = sredniaZLaboratoriow;
    this.sredniaZWykladow = sredniaZWykladow;
  }
}

const main = function () {
  let czlowiek = new Czlowiek("Jan", "Kowalski", "Warszawa", "programista");
  let student = new Student(
    "Jan",
    "Kowalski",
    "Warszawa",
    "programista",
    "12345",
    "Informatyka"
  );
  let studentFizyki = new StudentFizyki(
    "Jan",
    "Kowalski",
    "Warszawa",
    "programista",
    "12345",
    "Informatyka",
    4.5,
    4.5
  );
  console.log(czlowiek);
  console.log(student);
  console.log(studentFizyki);
};

main();

/*
Napisz klase Czlowiek, klase pochodna Student oraz klase pochodna klasy pochodnej StudentFizyki.
a) Czlowiek powinien przechowywac informacje o imieniu, nazwisku, miejscu urodzenia i zawodzie.
b) Student powinien dodac pola numer albumu oraz kierunek studiow.
c) StudentFizykii powinien dodac pola srednia z laboratoriow oraz srednia z wykladow.
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
    constructor(imie, nazwisko, miejsceUrodzenia, zawod, numerAlbumu, kierunekStudiow) {
        super(imie, nazwisko, miejsceUrodzenia, zawod);
        this.numerAlbumu = numerAlbumu;
        this.kierunekStudiow = kierunekStudiow;
    }
}


class StudentFizyki extends Student {
    constructor(imie, nazwisko, miejsceUrodzenia, zawod, numerAlbumu, kierunekStudiow, sredniaZLaboratoriow, sredniaZWykladow) {
        super(imie, nazwisko, miejsceUrodzenia, zawod, numerAlbumu, kierunekStudiow);
        this.sredniaZLaboratoriow = sredniaZLaboratoriow;
        this.sredniaZWykladow = sredniaZWykladow;
    }
}


main = function() {
    let czlowiek = new Czlowiek("Jan", "Kowalski", "Warszawa", "programista");
    let student = new Student("Jan", "Kowalski", "Warszawa", "programista", "12345", "Informatyka");
    let studentFizyki = new StudentFizyki("Jan", "Kowalski", "Warszawa", "programista", "12345", "Informatyka", 4.5, 4.5);
    console.log(czlowiek);
    console.log(student);
    console.log(studentFizyki);
}

main()
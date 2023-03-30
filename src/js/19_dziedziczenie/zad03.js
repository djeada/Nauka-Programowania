/*
Tytul: Polimorfizm. 

Tresc: Zaprojektuj klase Zwierz oraz klasy potomne Pies i Kot. Obie klasy potomne powinny nadpisywac metode 'odglos()' zdefiniowana w klasie bazowej. Napisz program testujacy te klasy, w ktorym umiescisz obiekty wszystkich trzech klas w jednej liscie i przejdziesz przez wszystkie elementy tej listy, wywolujac dla kazdego z nich funkcje 'odglos()'."
*/ // Klasa Zwierz (klasa bazowa)
class Zwierz {
  odglos() {
    console.log("Nieznany dzwiek");
  }
}

// Klasy potomne Pies i Kot
class Pies extends Zwierz {
  odglos() {
    console.log("Hau!");
  }
}

class Kot extends Zwierz {
  odglos() {
    console.log("Miau!");
  }
}

// Tworzymy liste obiektow klas Pies i Kot
const listaZwierzat = [new Pies(), new Kot(), new Pies(), new Kot()];

// Wywolujemy metode odglos() dla kazdego obiektu w liscie
listaZwierzat.forEach((zwierze) => {
  zwierze.odglos();
});


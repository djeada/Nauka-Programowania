/*
Tytuł: Polimorfizm. 

Treść: Zaprojektuj klasę Zwierz oraz klasy potomne Pies i Kot. Obie klasy potomne powinny nadpisywać metodę 'odgłos()' zdefiniowaną w klasie bazowej. Napisz program testujący te klasy, w którym umieścisz obiekty wszystkich trzech klas w jednej liście i przejdziesz przez wszystkie elementy tej listy, wywołując dla każdego z nich funkcję 'odgłos()'."
*/ // Klasa Zwierz (klasa bazowa)
class Zwierz {
  odgłos() {
    console.log("Nieznany dźwięk");
  }
}

// Klasy potomne Pies i Kot
class Pies extends Zwierz {
  odgłos() {
    console.log("Hau!");
  }
}

class Kot extends Zwierz {
  odgłos() {
    console.log("Miau!");
  }
}

// Tworzymy listę obiektów klas Pies i Kot
const listaZwierzat = [new Pies(), new Kot(), new Pies(), new Kot()];

// Wywołujemy metodę odgłos() dla każdego obiektu w liście
listaZwierzat.forEach((zwierze) => {
  zwierze.odgłos();
});

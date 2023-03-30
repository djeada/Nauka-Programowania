/*
Tytul: Zlicz instancje klasy w programie.

Tresc: Opis zadania: Stworz klase Klasa, ktora bedzie zawierala funkcje statyczna, zwracajaca aktualna liczbe instancji tej klasy w programie. Nastepnie stworz kilka obiektow tej klasy i przetestuj dzialanie funkcji.

Dane wejsciowe: brak

Dane wyjsciowe: liczba naturalna, reprezentujaca liczbe instancji klasy w programie.
*/

class Klasa {
  constructor() {
    if (typeof Klasa.liczbaInstancji === "undefined") {
      Klasa.liczbaInstancji = 0;
    }
    Klasa.liczbaInstancji++;
  }

  static podajLiczbeInstancji() {
    return Klasa.liczbaInstancji;
  }
}

for (let i = 0; i < 3; i++) {
  new Klasa();
}

console.log(Klasa.podajLiczbeInstancji()); // wyswietli 3


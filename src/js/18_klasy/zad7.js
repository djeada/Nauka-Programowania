/*
Tytuł: Zlicz instancje klasy w programie.

Treść: Opis zadania: Stwórz klasę Klasa, która będzie zawierała funkcję statyczną, zwracającą aktualną liczbę instancji tej klasy w programie. Następnie stwórz kilka obiektów tej klasy i przetestuj działanie funkcji.

Dane wejściowe: brak

Dane wyjściowe: liczba naturalna, reprezentująca liczbę instancji klasy w programie.
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

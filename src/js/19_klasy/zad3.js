/*
Napisz klase Prostokat reprezentujaca prostokat w ukladzie kartezjanskim. 
Prostokat okreslony jest przez wspolrzedne jego czterech wierzcholkow. 
Boki prostokata sa prostopadle do osi ukladu wspolrzednych. 
Klasa powinna zawierac funkcje statyczna zwracajaca pole prostokata 
powstalego z nalozenia sie dwoch prostokatow. Jesli dwa prostokaty 
nie pokrywaja sie, funkcja powinna zwracac 0.
*/

class Prostokat {
  constructor(lewo, prawo, gora, dol) {
    this.lewo = lewo || 0;
    this.prawo = prawo || 0;
    this.gora = gora || 0;
    this.dol = dol || 0;
  }

  static poleCzesciWspolnej(p1, p2) {
    let poleX = Math.max(
      0.0,
      Math.min(p1.prawo, p2.prawo) - Math.max(p1.lewo, p2.lewo)
    );
    let poleY = Math.max(
      0.0,
      Math.min(p1.gora, p2.gora) - Math.max(p1.dol, p2.dol)
    );
    return poleX * poleY;
  }
}

test1 = function () {
  let prostokatA = new Prostokat(2, 5, 7, 2);
  let prostokatB = new Prostokat(3, 6, 9, 4);
  oczekiwane = 6.0;
  wynik = Prostokat.poleCzesciWspolnej(prostokatA, prostokatB);
  if (abs(wynik - oczekiwane) > 0.01) {
    throw new Error(
      `Assertion error line 63: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`
    );
  }
};

test2 = function () {
  let prostokatA = new Prostokat(-9.5, 10.5, 6, 2);
  let prostokatB = new Prostokat(-4.5, 2.3, 3.8, -3.3);
  oczekiwane = 12.24;
  wynik = Prostokat.poleCzesciWspolnej(prostokatA, prostokatB);
  if (abs(wynik - oczekiwane) > 0.01) {
    throw new Error(
      `Assertion error line 63: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`
    );
  }
};

main = function () {
  test1();
  test2();
};

main();

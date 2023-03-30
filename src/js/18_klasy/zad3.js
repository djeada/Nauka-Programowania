/*
Tytul: Prostokat powstaly z nalozenia sie dwoch prostokatow.

Opis zadania: Napisz klase Prostokat, ktora bedzie reprezentowala prostokat w ukladzie kartezjanskim. Prostokat jest okreslony przez wspolrzedne jego czterech wierzcholkow. Boki prostokata sa prostopadle do osi ukladu wspolrzednych. Klasa powinna zawierac funkcje statyczna, ktora zwraca pole prostokata powstalego z nalozenia sie dwoch prostokatow. Jesli dwa prostokaty nie pokrywaja sie, funkcja powinna zwracac 0.

Napisz program, ktory przetestuje twoja klase. Stworz prostokaty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjscie informacje o utworzonych prostokatach. Sprawdz, czy pole czesci wspolnej rowne jest 6.
*/

class Prostokat {
  constructor(x1, y1, x2, y2, x3, y3, x4, y4) {
    this.wierzcholki = [
      [x1, y1],
      [x2, y2],
      [x3, y3],
      [x4, y4],
    ];
  }

  static poleCzesciWspolnej(p1, p2) {
    const [left1, top1, right1, bottom1] = Prostokat.boundingRect(p1);
    const [left2, top2, right2, bottom2] = Prostokat.boundingRect(p2);

    const left = Math.max(left1, left2);
    const top = Math.max(top1, top2);
    const right = Math.min(right1, right2);
    const bottom = Math.min(bottom1, bottom2);

    if (left >= right || top >= bottom) {
      return 0;
    }

    const width = right - left;
    const height = bottom - top;

    return width * height;
  }

  static boundingRect(p) {
    let left = p.wierzcholki[0][0];
    let top = p.wierzcholki[0][1];
    let right = p.wierzcholki[0][0];
    let bottom = p.wierzcholki[0][1];

    for (const [x, y] of p.wierzcholki) {
      if (x < left) {
        left = x;
      }
      if (x > right) {
        right = x;
      }
      if (y < top) {
        top = y;
      }
      if (y > bottom) {
        bottom = y;
      }
    }

    return [left, top, right, bottom];
  }

  wypiszInfo() {
    console.log(
      `Prostokat o wierzcholkach: (${this.wierzcholki[0][0]}, ${this.wierzcholki[0][1]}), (${this.wierzcholki[1][0]}, ${this.wierzcholki[1][1]}), (${this.wierzcholki[2][0]}, ${this.wierzcholki[2][1]}), (${this.wierzcholki[3][0]}, ${this.wierzcholki[3][1]})`
    );
  }
}

const prostokatA = new Prostokat(3, 6, 9, 4, 9, 1, 3, 3);
const prostokatB = new Prostokat(2, 5, 7, 2, 8, 4, 4, 7);

prostokatA.wypiszInfo();
prostokatB.wypiszInfo();

const poleCzesciWspolnej = Prostokat.poleCzesciWspolnej(prostokatA, prostokatB);
console.log(`Pole czesci wspolnej prostokatow A i B: ${poleCzesciWspolnej}`);


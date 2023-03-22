/*
Tytuł: Prostokąt powstały z nałożenia się dwóch prostokątów.

Opis zadania: Napisz klasę Prostokąt, która będzie reprezentowała prostokąt w układzie kartezjańskim. Prostokąt jest określony przez współrzędne jego czterech wierzchołków. Boki prostokąta są prostopadłe do osi układu współrzędnych. Klasa powinna zawierać funkcję statyczną, która zwraca pole prostokąta powstałego z nałożenia się dwóch prostokątów. Jeśli dwa prostokąty nie pokrywają się, funkcja powinna zwracać 0.

Napisz program, który przetestuje twoją klasę. Stwórz prostokąty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjście informacje o utworzonych prostokątach. Sprawdź, czy pole części wspólnej równe jest 6.
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
      `Prostokąt o wierzchołkach: (${this.wierzcholki[0][0]}, ${this.wierzcholki[0][1]}), (${this.wierzcholki[1][0]}, ${this.wierzcholki[1][1]}), (${this.wierzcholki[2][0]}, ${this.wierzcholki[2][1]}), (${this.wierzcholki[3][0]}, ${this.wierzcholki[3][1]})`
    );
  }
}

const prostokatA = new Prostokat(3, 6, 9, 4, 9, 1, 3, 3);
const prostokatB = new Prostokat(2, 5, 7, 2, 8, 4, 4, 7);

prostokatA.wypiszInfo();
prostokatB.wypiszInfo();

const poleCzesciWspolnej = Prostokat.poleCzesciWspolnej(prostokatA, prostokatB);
console.log(`Pole części wspólnej prostokątów A i B: ${poleCzesciWspolnej}`);

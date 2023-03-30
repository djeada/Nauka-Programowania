/*

Tytul: Gra w statki

Tresc: Napisz program implementujacy gre w statki.

Stworz macierz o wymiarach 10x10. Wylosuj polozenia statkow i zapisz je w macierzy. Do dyspozycji masz nastepujace statki:

* 1 statek o dlugosci 4
* 2 statki o dlugosci 3
* 3 statki o dlugosci 2
* 5 statkow o dlugosci 1

Kazde pole moze zawierac tylko jeden statek.

Wypisz na standardowe wyjscie plansze zlozona z 10x10 kropek i popros uzytkownika o podanie wspolrzednych. Jesli na podanych przez uzytkownika wspolrzednych znajduje sie statek, zamien kropke na litere o na planszy. W przeciwnym razie, zamien kropke na litere x.

Powtarzaj krok 2, az wszystkie pozycje statkow zostana odkryte przez uzytkownika lub az na planszy pojawi sie 10 liter x. W obu przypadkach zakoncz gre i poinformuj uzytkownika o wyniku.

*/

// funkcja zwracajaca nowa, pusta plansze o wymiarach 10x10
function nowaPlansza() {
  const plansza = [];

  for (let i = 0; i < 10; i++) {
    plansza.push(Array(10).fill("."));
  }

  return plansza;
}

// funkcja losujaca polozenie statkow i zwracajaca plansze z umieszczonymi na niej statkami
function losujStatki() {
  const plansza = nowaPlansza();

  // tablica ze wszystkimi statkami do umieszczenia na planszy
  const statki = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1];

  // iterujemy po wszystkich statkach do umieszczenia na planszy
  for (const dlugosc of statki) {
    let pozycja;
    let orientacja;

    // losujemy pozycje i orientacje statku tak dlugo, az znajdziemy takie, ktore nie nachodza na inne statki
    do {
      pozycja = [
        Math.floor(Math.random() * 10),
        Math.floor(Math.random() * 10),
      ];
      orientacja = Math.random() < 0.5 ? "pozioma" : "pionowa";
    } while (!czyMoznaUmiescicStatek(plansza, pozycja, orientacja, dlugosc));

    // umieszczamy statek na planszy
    for (let i = 0; i < dlugosc; i++) {
      if (orientacja === "pozioma") {
        plansza[pozycja[0]][pozycja[1] + i] = "o";
      } else {
        plansza[pozycja[0] + i][pozycja[1]] = "o";
      }
    }
  }

  return plansza;
}

// funkcja sprawdzajaca, czy mozna umiescic statek o podanych parametrach na planszy
function czyMoznaUmiescicStatek(plansza, pozycja, orientacja, dlugosc) {
  const [x, y] = pozycja;

  if (orientacja === "pozioma") {
    if (y + dlugosc > 10) {
      return false;
    }

    for (let i = y; i < y + dlugosc; i++) {
      if (plansza[x][i] !== ".") {
        return false;
      }
    }
  } else {
    if (x + dlugosc > 10) {
      return false;
    }

    for (let i = x; i < x + dlugosc; i++) {
      if (plansza[i][y] !== ".") {
        return false;
      }
    }
  }

  return true;
}

// funkcja wypisujaca plansze na standardowe wyjscie
function wypiszPlansze(plansza) {
  console.log("  A B C D E F G H I J");
  for (let i = 0; i < 10; i++) {
    const wiersz = plansza[i].join(" ");
    console.log(`${i} ${wiersz}`);
  }
}

let remaining_ships = 15; // poczatkowo jest 15 statkow do zatopienia

while (remaining_ships > 0 && hits < 10) {
  // wypisanie planszy
  console.log(board.map((row) => row.join(" ")).join("\n"));

  // pyta uzytkownika o wspolrzedne
  let row = prompt("Podaj numer wiersza (1-10): ");
  let col = prompt("Podaj numer kolumny (1-10): ");

  // zamiana na numer
  row = parseInt(row) - 1;
  col = parseInt(col) - 1;

  // sprawdzenie, czy uzytkownik trafil w statek
  if (board[row][col] === "o") {
    console.log("TRAFIONY!");
    board[row][col] = "x"; // oznaczenie trafienia
    remaining_ships--; // zmniejszenie liczby pozostalych statkow
  } else if (board[row][col] === ".") {
    console.log("PUDLO!");
    board[row][col] = "x"; // oznaczenie pudla
    hits++; // zwiekszenie liczby trafien w puste pola
  } else {
    console.log("Juz tu strzelales!");
  }
}


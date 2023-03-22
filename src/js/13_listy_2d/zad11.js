/*

Tytuł: Gra w statki

Treść: Napisz program implementujący grę w statki.

Stwórz macierz o wymiarach 10x10. Wylosuj położenia statków i zapisz je w macierzy. Do dyspozycji masz następujące statki:

* 1 statek o długości 4
* 2 statki o długości 3
* 3 statki o długości 2
* 5 statków o długości 1

Każde pole może zawierać tylko jeden statek.

Wypisz na standardowe wyjście planszę złożoną z 10x10 kropek i poproś użytkownika o podanie współrzędnych. Jeśli na podanych przez użytkownika współrzędnych znajduje się statek, zamień kropkę na literę o na planszy. W przeciwnym razie, zamień kropkę na literę x.

Powtarzaj krok 2, aż wszystkie pozycje statków zostaną odkryte przez użytkownika lub aż na planszy pojawi się 10 liter x. W obu przypadkach zakończ grę i poinformuj użytkownika o wyniku.

*/

// funkcja zwracająca nową, pustą planszę o wymiarach 10x10
function nowaPlansza() {
  const plansza = [];

  for (let i = 0; i < 10; i++) {
    plansza.push(Array(10).fill("."));
  }

  return plansza;
}

// funkcja losująca położenie statków i zwracająca planszę z umieszczonymi na niej statkami
function losujStatki() {
  const plansza = nowaPlansza();

  // tablica ze wszystkimi statkami do umieszczenia na planszy
  const statki = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1];

  // iterujemy po wszystkich statkach do umieszczenia na planszy
  for (const dlugosc of statki) {
    let pozycja;
    let orientacja;

    // losujemy pozycję i orientację statku tak długo, aż znajdziemy takie, które nie nachodzą na inne statki
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

// funkcja sprawdzająca, czy można umieścić statek o podanych parametrach na planszy
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

// funkcja wypisująca planszę na standardowe wyjście
function wypiszPlansze(plansza) {
  console.log("  A B C D E F G H I J");
  for (let i = 0; i < 10; i++) {
    const wiersz = plansza[i].join(" ");
    console.log(`${i} ${wiersz}`);
  }
}

let remaining_ships = 15; // początkowo jest 15 statków do zatopienia

while (remaining_ships > 0 && hits < 10) {
  // wypisanie planszy
  console.log(board.map((row) => row.join(" ")).join("\n"));

  // pyta użytkownika o współrzędne
  let row = prompt("Podaj numer wiersza (1-10): ");
  let col = prompt("Podaj numer kolumny (1-10): ");

  // zamiana na numer
  row = parseInt(row) - 1;
  col = parseInt(col) - 1;

  // sprawdzenie, czy użytkownik trafił w statek
  if (board[row][col] === "o") {
    console.log("TRAFIONY!");
    board[row][col] = "x"; // oznaczenie trafienia
    remaining_ships--; // zmniejszenie liczby pozostałych statków
  } else if (board[row][col] === ".") {
    console.log("PUDŁO!");
    board[row][col] = "x"; // oznaczenie pudła
    hits++; // zwiększenie liczby trafień w puste pola
  } else {
    console.log("Już tu strzelałeś!");
  }
}

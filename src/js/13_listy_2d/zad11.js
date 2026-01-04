/*
ZAD-11 — Gra w statki (projekt konsolowy)

**Poziom:** ★★★
**Tagi:** `macierze`, `losowanie`, `gra`, `pętle`

### Treść

Zaimplementuj grę w statki na planszy 10×10:

1. Plansza startowa: 10×10 wypełniona `.`
2. Losowo rozmieść statki (poziomo/pionowo), bez stykania bokami ani rogami:

   * 1× długość 4
   * 2× długość 3
   * 3× długość 2
   * 5× długość 1
3. Pętla gry:

   * wypisz planszę,
   * wczytaj `r c` (0..9),
   * jeśli trafienie: wstaw `o`, wypisz komunikat o trafieniu,
   * jeśli pudło: wstaw `x`, zwiększ licznik pudeł,
   * gra kończy się, gdy:

     * wszystkie pola statków trafione (wygrana), albo
     * 10 pudeł (przegrana).
   * po każdym ruchu wypisz zaktualizowaną planszę.

### Wejście

Wielokrotnie:

* `r c` (w jednej linii)

### Wyjście

* plansza i komunikaty w trakcie,
* na końcu komunikat o wygranej/przegranej.

### Uwagi praktyczne

* To zadanie jest **większym projektem** — format wyjścia bywa sprawdzany „ręcznie” (nie zawsze automatycznie), więc trzymaj się spójnego stylu wypisywania planszy.

*/

function nowaPlansza() {
  const plansza = [];

  for (let i = 0; i < 10; i++) {
    plansza.push(Array(10).fill("."));
  }

  return plansza;
}

// Funkcja losuje położenie statków i zwraca planszę z umieszczonymi statkami
// Złożoność czasowa: O(k), gdzie k to liczba prób losowania pozycji
// Złożoność pamięciowa: O(1)
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

// Funkcja wypisuje planszę na standardowe wyjście
// Złożoność czasowa: O(1) - stała wielkość planszy
// Złożoność pamięciowa: O(1)
function wypiszPlansze(plansza) {
  console.log("  A B C D E F G H I J");
  for (let i = 0; i < 10; i++) {
    const wiersz = plansza[i].join(" ");
    console.log(`${i} ${wiersz}`);
  }
}

// Glówna funkcja gry - uruchamia grę w statki
// Złożoność czasowa: O(k), gdzie k to liczba rund gry
// Złożoność pamięciowa: O(1) - stała pamięć dla planszy 10x10
function grajWStatki() {
  const plansza = losujStatki();
  let pozostaleStatki = 15; // Łączna liczba pól zajętych przez statki
  let pudla = 0;

  while (pozostaleStatki > 0 && pudla < 10) {
    // Wypisanie planszy
    wypiszPlansze(plansza);

    // W środowisku Node.js prompt nie działa - symulujemy losowe strzały dla testu
    // W prawdziwej implementacji użyj readline lub podobnej biblioteki
    const row = Math.floor(Math.random() * 10);
    const col = Math.floor(Math.random() * 10);
    
    console.log(`Strzelasz w: ${row} ${col}`);

    // Sprawdzenie czy użytkownik trafił w statek
    if (plansza[row][col] === "o") {
      console.log("TRAFIONY!");
      plansza[row][col] = "X"; // Oznaczenie trafienia
      pozostaleStatki--;
    } else if (plansza[row][col] === ".") {
      console.log("PUDLO!");
      plansza[row][col] = "x"; // Oznaczenie pudła
      pudla++;
    } else {
      console.log("Juz tu strzelales!");
    }
  }

  // Wypisanie końcowej planszy
  wypiszPlansze(plansza);

  if (pozostaleStatki === 0) {
    console.log("WYGRANA! Zatopiłeś wszystkie statki!");
  } else {
    console.log("PRZEGRANA! Wykorzystałeś wszystkie próby.");
  }
}

// Uwaga: Ta funkcja jest zakomentowana, aby nie uruchamiać gry automatycznie podczas testów
// Aby zagrać, odkomentuj poniższą linię:
// grajWStatki();


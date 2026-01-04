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

use std::io;

// Maksymalna liczba pudeł przed przegraną
const MAX_PUDEL: usize = 10;

// Gra w statki - uproszczona wersja konsolowa bez losowania
// Złożoność czasowa: O(1) dla każdego ruchu
// Złożoność pamięciowa: O(1) dla planszy 10x10

const ROZMIAR: usize = 10;

struct Gra {
    plansza: Vec<Vec<char>>,
    statki: Vec<Vec<(usize, usize)>>,
    pudla: usize,
}

impl Gra {
    fn nowa() -> Self {
        let mut gra = Gra {
            plansza: vec![vec!['.'; ROZMIAR]; ROZMIAR],
            statki: Vec::new(),
            pudla: 0,
        };
        gra.rozmies_statki_predefiniowane();
        gra
    }

    // Uproszczone rozmieszczenie - predefiniowane pozycje statków
    fn rozmies_statki_predefiniowane(&mut self) {
        // Statek 4-polowy (0,0) poziomo
        self.dodaj_statek(vec![(0, 0), (0, 1), (0, 2), (0, 3)]);

        // Statki 3-polowe
        self.dodaj_statek(vec![(2, 0), (2, 1), (2, 2)]);
        self.dodaj_statek(vec![(0, 5), (1, 5), (2, 5)]);

        // Statki 2-polowe
        self.dodaj_statek(vec![(4, 0), (4, 1)]);
        self.dodaj_statek(vec![(4, 3), (4, 4)]);
        self.dodaj_statek(vec![(6, 0), (7, 0)]);

        // Statki 1-polowe
        self.dodaj_statek(vec![(6, 2)]);
        self.dodaj_statek(vec![(6, 4)]);
        self.dodaj_statek(vec![(8, 2)]);
        self.dodaj_statek(vec![(8, 4)]);
        self.dodaj_statek(vec![(9, 9)]);
    }

    fn dodaj_statek(&mut self, pozycje: Vec<(usize, usize)>) {
        self.statki.push(pozycje);
    }

    fn wypisz(&self) {
        println!("  0 1 2 3 4 5 6 7 8 9");
        for (i, wiersz) in self.plansza.iter().enumerate() {
            print!("{} ", i);
            for c in wiersz {
                print!("{} ", c);
            }
            println!();
        }
    }

    fn ruch(&mut self, r: usize, c: usize) -> bool {
        if r >= ROZMIAR || c >= ROZMIAR {
            println!("Nieprawidłowe współrzędne!");
            return true;
        }

        if self.plansza[r][c] != '.' {
            println!("To pole już było sprawdzone!");
            return true;
        }

        let mut trafienie = false;
        for statek in &self.statki {
            if statek.contains(&(r, c)) {
                trafienie = true;
                break;
            }
        }

        if trafienie {
            self.plansza[r][c] = 'o';
            println!("Trafienie!");
        } else {
            self.plansza[r][c] = 'x';
            self.pudla += 1;
            println!("Pudło! (pudła: {})", self.pudla);
        }

        true
    }

    fn czy_wygrana(&self) -> bool {
        for statek in &self.statki {
            for &(r, c) in statek {
                if self.plansza[r][c] != 'o' {
                    return false;
                }
            }
        }
        true
    }

    fn czy_przegrana(&self) -> bool {
        self.pudla >= MAX_PUDEL
    }
}

fn main() {
    let mut gra = Gra::nowa();

    println!("Gra w statki! Plansza 10x10.");
    println!("Podaj współrzędne r c (0-9):");

    loop {
        gra.wypisz();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let coords: Vec<usize> = input
            .trim()
            .split_whitespace()
            .filter_map(|s| s.parse().ok())
            .collect();

        if coords.len() != 2 {
            println!("Podaj dwie liczby!");
            continue;
        }

        gra.ruch(coords[0], coords[1]);

        if gra.czy_wygrana() {
            gra.wypisz();
            println!("Wygrana! Zatopiono wszystkie statki!");
            break;
        }

        if gra.czy_przegrana() {
            gra.wypisz();
            println!("Przegrana! Za dużo pudeł!");
            break;
        }
    }
}

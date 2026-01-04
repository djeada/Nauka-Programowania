/*
ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

* A = [[1, 3], [4, 2]]
* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

*/

#[derive(Debug, Clone, PartialEq)]
struct Macierz {
    dane: Vec<Vec<i32>>,
}

impl Macierz {
    // Konstruktor
    fn new(dane: Vec<Vec<i32>>) -> Self {
        Macierz { dane }
    }

    // Dodawanie macierzy
    // Złożoność czasowa: O(n*m)
    fn dodaj(&self, other: &Macierz) -> Macierz {
        let mut wynik = Vec::new();
        for i in 0..self.dane.len() {
            let mut wiersz = Vec::new();
            for j in 0..self.dane[i].len() {
                wiersz.push(self.dane[i][j] + other.dane[i][j]);
            }
            wynik.push(wiersz);
        }
        Macierz::new(wynik)
    }

    // Odejmowanie macierzy
    // Złożoność czasowa: O(n*m)
    fn odejmij(&self, other: &Macierz) -> Macierz {
        let mut wynik = Vec::new();
        for i in 0..self.dane.len() {
            let mut wiersz = Vec::new();
            for j in 0..self.dane[i].len() {
                wiersz.push(self.dane[i][j] - other.dane[i][j]);
            }
            wynik.push(wiersz);
        }
        Macierz::new(wynik)
    }

    // Mnożenie macierzy
    // Złożoność czasowa: O(n*m*p)
    fn mnoz(&self, other: &Macierz) -> Macierz {
        let n = self.dane.len();
        let m = other.dane[0].len();
        let p = self.dane[0].len();

        let mut wynik = vec![vec![0; m]; n];

        for i in 0..n {
            for j in 0..m {
                for k in 0..p {
                    wynik[i][j] += self.dane[i][k] * other.dane[k][j];
                }
            }
        }

        Macierz::new(wynik)
    }

    // Metoda wypisująca macierz
    fn wypisz(&self, nazwa: &str) {
        if !nazwa.is_empty() {
            println!("Macierz {}:", nazwa);
        }
        for wiersz in &self.dane {
            print!("[");
            for (i, &val) in wiersz.iter().enumerate() {
                if i > 0 {
                    print!(", ");
                }
                print!("{}", val);
            }
            println!("]");
        }
        println!();
    }
}

fn main() {
    let a = Macierz::new(vec![vec![1, 3], vec![4, 2]]);
    let b = Macierz::new(vec![vec![5, 0], vec![1, 3]]);

    a.wypisz("A");
    b.wypisz("B");

    let suma = a.dodaj(&b);
    println!("Suma macierzy:");
    suma.wypisz("");

    let roznica = a.odejmij(&b);
    println!("Różnica macierzy A - B:");
    roznica.wypisz("");

    let iloczyn = a.mnoz(&b);
    println!("Iloczyn macierzy A * B:");
    iloczyn.wypisz("");
}

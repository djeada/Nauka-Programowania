/*
ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

**Wyjście:**

```
7
```

### Uwagi

* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).

*/

use std::io;

// Funkcja znajdująca indeks zera do zamiany na 1 dla najdłuższego ciągu jedynek
// Złożoność czasowa: O(n), gdzie n to długość listy
// Złożoność pamięciowa: O(1)
fn znajdz_zero_do_zamiany(lista: &[i32]) -> i32 {
    let mut max_dlugosc = 0;
    let mut najlepszy_indeks = -1;

    // Sprawdź czy lista zawiera przynajmniej jedno zero i przynajmniej jedną jedynkę
    let ma_zero = lista.iter().any(|&x| x == 0);
    let ma_jedynke = lista.iter().any(|&x| x == 1);

    if !ma_zero || !ma_jedynke {
        return -1;
    }

    // Dla każdego zera sprawdź długość ciągu po zamianie
    for (i, &val) in lista.iter().enumerate() {
        if val == 0 {
            // Policz jedynki przed zerem
            let mut lewo = 0;
            for j in (0..i).rev() {
                if lista[j] == 1 {
                    lewo += 1;
                } else {
                    break;
                }
            }

            // Policz jedynki po zerze
            let mut prawo = 0;
            for j in (i + 1)..lista.len() {
                if lista[j] == 1 {
                    prawo += 1;
                } else {
                    break;
                }
            }

            let dlugosc = lewo + prawo + 1;
            if dlugosc > max_dlugosc {
                max_dlugosc = dlugosc;
                najlepszy_indeks = i as i32;
            }
        }
    }

    najlepszy_indeks
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");

    // Parsuj listę z formatu [0, 0, 1, 0, ...]
    let lista_str = input.trim().trim_start_matches('[').trim_end_matches(']');

    let lista: Vec<i32> = lista_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();

    println!("{}", znajdz_zero_do_zamiany(&lista));
}

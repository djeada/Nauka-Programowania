/*
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

* Najprościej użyć schematu Hornera.

*/

fn wartosc_wielomianu(wspolczynniki: &[i32], x: i32) -> i32 {
    if wspolczynniki.is_empty() {
        return 0;
    }

    let mut wynik = wspolczynniki[0];

    for i in 1..wspolczynniki.len() {
        wynik = wynik * x + wspolczynniki[i];
    }

    wynik
}

fn main() {
    // Przykład: [3, 2, 1] oznacza 3x^2 + 2x + 1
    let a = vec![3, 2, 1];
    let x = 1;

    println!("{}", wartosc_wielomianu(&a, x));
}

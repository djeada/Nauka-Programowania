/*
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` i zwraca listę współczynników wielomianu będącego ich iloczynem.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)

### Przykład

Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
`[5, 10, 30, 26, 52, 24]`

*/

fn mnoz_wielomiany(a: &[i32], b: &[i32]) -> Vec<i32> {
    if a.is_empty() || b.is_empty() {
        return vec![0];
    }

    let mut wynik = vec![0; a.len() + b.len() - 1];

    for (i, &a_val) in a.iter().enumerate() {
        for (j, &b_val) in b.iter().enumerate() {
            wynik[i + j] += a_val * b_val;
        }
    }

    wynik
}

fn main() {
    // Przykład: [5, 0, 10, 6] * [1, 2, 4]
    let a = vec![5, 0, 10, 6];
    let b = vec![1, 2, 4];

    let wynik = mnoz_wielomiany(&a, &b);
    println!("{:?}", wynik);
}

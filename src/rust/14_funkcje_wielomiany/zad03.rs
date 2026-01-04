/*
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` (mogą mieć różne stopnie) i zwraca współczynniki wielomianu będącego ich sumą.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników `a + b` w tej samej konwencji

### Przykład

Dla `a = [3, 5, 2]` i `b = [2, -8, 1]` funkcja zwraca:
`[5, -3, 3]`

### Uwagi

* Jeśli listy mają różne długości, wyrównaj je od końca (od wyrazu wolnego).

*/

fn dodaj_wielomiany(a: &[i32], b: &[i32]) -> Vec<i32> {
    let max_len = a.len().max(b.len());
    let mut wynik = vec![0; max_len];

    // Dodaj współczynniki z a (od najstarszego do najmłodszego)
    let offset_a = max_len - a.len();
    for (i, &val) in a.iter().enumerate() {
        wynik[offset_a + i] += val;
    }

    // Dodaj współczynniki z b
    let offset_b = max_len - b.len();
    for (i, &val) in b.iter().enumerate() {
        wynik[offset_b + i] += val;
    }

    // Usuń wiodące zera
    while wynik.len() > 1 && wynik[0] == 0 {
        wynik.remove(0);
    }

    wynik
}

fn main() {
    // Przykład: [3, 5, 2] + [2, -8, 1]
    let a = vec![3, 5, 2];
    let b = vec![2, -8, 1];

    let wynik = dodaj_wielomiany(&a, &b);
    println!("{:?}", wynik);
}

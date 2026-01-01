/*
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `k` — liczba (całkowita)

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `k * P(x)`

### Przykład

Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
`[-8, 6, -4]`

*/

// Funkcja mnożąca wielomian przez skalar
// Złożoność czasowa: O(n), gdzie n to stopień wielomianu
// Złożoność pamięciowa: O(n)
fn mnoz_przez_skalar(wspolczynniki: &[i32], k: i32) -> Vec<i32> {
    wspolczynniki.iter().map(|&w| w * k).collect()
}

fn main() {
    // Przykład: [4, -3, 2] * (-2)
    let a = vec![4, -3, 2];
    let k = -2;
    
    let wynik = mnoz_przez_skalar(&a, k);
    println!("{:?}", wynik);
}

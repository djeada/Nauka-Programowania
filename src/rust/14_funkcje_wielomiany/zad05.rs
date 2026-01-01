/*
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `k` — liczba naturalna

### Wyjście (zwracana wartość)

* lista współczynników wielomianu po zróżniczkowaniu `k` razy

### Przykład

Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
`[8, -3]`

### Uwagi

* Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

*/

// Funkcja obliczająca k-tą pochodną wielomianu
// Złożoność czasowa: O(n * k), gdzie n to stopień wielomianu
// Złożoność pamięciowa: O(n)
fn pochodna_wielomianu(wspolczynniki: &[i32], k: usize) -> Vec<i32> {
    if k == 0 {
        return wspolczynniki.to_vec();
    }
    
    if wspolczynniki.len() <= k {
        return vec![0];
    }
    
    let mut wynik = wspolczynniki.to_vec();
    
    for _ in 0..k {
        if wynik.len() <= 1 {
            return vec![0];
        }
        
        let mut nowa = Vec::new();
        let stopien = wynik.len() - 1;
        
        for (i, &w) in wynik.iter().enumerate() {
            if i < wynik.len() - 1 {
                nowa.push(w * (stopien - i) as i32);
            }
        }
        
        wynik = nowa;
    }
    
    if wynik.is_empty() {
        vec![0]
    } else {
        wynik
    }
}

fn main() {
    // Przykład: [4, -3, 2], k=1
    // 4x^2 - 3x + 2 -> 8x - 3
    let a = vec![4, -3, 2];
    let k = 1;
    
    let wynik = pochodna_wielomianu(&a, k);
    println!("{:?}", wynik);
}

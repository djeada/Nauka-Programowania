/*
ZAD-05 — Sortowanie szybkie

**Poziom:** ★★☆
**Tagi:** `sorting`, `quick-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **Quick Sort**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Wybierz **pivot** (np. pierwszy element).
3. Podziel elementy na trzy grupy:

   * mniejsze od pivota,
   * równe pivotowi,
   * większe od pivota.
4. Rekurencyjnie posortuj część mniejszych i większych.
5. Sklej wynik: `mniejsze + równe + większe`.

### Wejście

* 1 linia: lista liczb całkowitych

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Średnio: `O(n log n)`, w pesymistycznym przypadku: `O(n^2)`.
* Wybór pivota ma wpływ na wydajność.

*/

use std::io;

// Sortowanie szybkie (Quick Sort)
// Złożoność czasowa: O(n log n) średnio, O(n^2) w pesymistycznym przypadku
// Złożoność pamięciowa: O(log n) dla rekursji
fn sort_v1(lista: &mut [i32]) {
    if lista.len() > 1 {
        szybkie(lista, 0, lista.len() - 1);
    }
}

fn szybkie(lista: &mut [i32], dol: usize, gora: usize) {
    if dol < gora {
        let piwot = podziel(lista, dol, gora);
        if piwot > 0 {
            szybkie(lista, dol, piwot - 1);
        }
        szybkie(lista, piwot + 1, gora);
    }
}

fn podziel(lista: &mut [i32], dol: usize, gora: usize) -> usize {
    let indeks = (dol + gora) / 2;
    let piwot = lista[indeks];
    let mut i = dol;
    let mut j = gora;
    
    loop {
        while lista[i] < piwot {
            i += 1;
        }
        while lista[j] > piwot {
            if j == 0 {
                break;
            }
            j -= 1;
        }
        
        if i >= j {
            return j;
        }
        
        lista.swap(i, j);
        i += 1;
        if j > 0 {
            j -= 1;
        }
    }
}

fn parsuj_liste(input: &str) -> Vec<i32> {
    input
        .trim()
        .trim_start_matches('[')
        .trim_end_matches(']')
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect()
}

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    
    let mut lista = parsuj_liste(&input);
    sort_v1(&mut lista);
    
    print!("[");
    for (i, &val) in lista.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", val);
    }
    println!("]");
}

fn main() {
    test_1();
}

/*
ZAD-01 — Sortowanie bąbelkowe

**Poziom:** ★☆☆
**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania bąbelkowego**.
Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów i zamianie ich miejscami, jeśli są w złej kolejności. Powtarzaj przebiegi, aż w całym przebiegu nie zajdzie żadna zamiana.

### Wejście

* 1 linia: lista liczb całkowitych, np. `[6, 2, 1, 4, 27]`

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

* Po każdym pełnym przebiegu największy element „wypływa” na koniec.
* W kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1.

*/
fn sort_v1(lista: &mut [i32]) {
    for i in 0..lista.len() {
        for j in (i + 1)..lista.len() {
            if lista[i] > lista[j] {
                lista.swap(i, j);
            }
        }
    }
}

fn sort_v2(lista: &mut [i32]) {
    let mut nowa_dl: usize;
    let mut dl = lista.len();
    loop {
        nowa_dl = 0;
        for i in 1..dl {
            if lista[i - 1] > lista[i] {
                lista.swap(i - 1, i);
                nowa_dl = i;
            }
        }
        if nowa_dl == 0 {
            break;
        }
        dl = nowa_dl;
    }
}

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn test_2() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v2(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
    test_1();
    test_2();
}

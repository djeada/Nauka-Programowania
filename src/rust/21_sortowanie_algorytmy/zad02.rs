/*
ZAD-02 — Sortowanie przez wybieranie

**Poziom:** ★★☆
**Tagi:** `sorting`, `selection-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wybieranie**.
Dla każdej pozycji `i` znajdź najmniejszy element w zakresie `i..koniec` i zamień go z elementem na pozycji `i`.

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

* Złożoność czasowa: `O(n^2)`.

*/
fn sort_v1(lista: &mut [i32]) {
    for i in 0..lista.len() {
        let mut pom = i;
        for j in (i + 1)..lista.len() {
            if lista[pom] > lista[j] {
                pom = j;
            }
        }
        lista.swap(i, pom);
    }
}

fn sort_v2(lista: &mut [i32]) {
    for x in 0..lista.len() {
        let min = lista[x..]
            .iter()
            .enumerate()
            .min_by_key(|&(_, v)| v)
            .map(|(i, _)| x + i)
            .expect("lista is non-empty");

        if x != min {
            lista.swap(x, min);
        }
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

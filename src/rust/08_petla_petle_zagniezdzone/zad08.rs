/*
ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `listy`, `kombinatoryka`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt Pascala o wysokości `n`.

Wiersz 1: `1`
Wiersz 2: `1 1`
Wiersz 3: `1 2 1`
itd.

Liczby w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w `i`-tej linii jest `i` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    for i in 1..=n {
        let mut row = vec![1];

        if i > 1 {
            // Oblicz wartości dla wiersza i na podstawie poprzedniego
            let mut prev_row = vec![1];
            for k in 2..=i {
                let mut new_row = vec![1];
                for j in 1..prev_row.len() {
                    new_row.push(prev_row[j - 1] + prev_row[j]);
                }
                new_row.push(1);
                prev_row = new_row;
            }
            row = prev_row;
        }

        for (j, val) in row.iter().enumerate() {
            if j > 0 {
                print!(" ");
            }
            print!("{}", val);
        }
        println!();
    }
}

/*
ZAD-04 — Podstawowe operacje arytmetyczne

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `I/O`

### Treść

Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:

1. `a + b`
2. `a - b`
3. `a * b`
4. `a // b` (dzielenie całkowite)
5. `a % b`
6. `a^b`

### Wejście

* 1. linia: `a` (liczba całkowita)
* 2. linia: `b` (liczba całkowita)

### Wyjście

6 linii — wyniki działań w kolejności 1–6.

### Ograniczenia / gwarancje

* `a ≥ 0`
* `b > 0` (żeby dzielenie i modulo były poprawne)

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
5
1
6
1
1
9
```

*/

use ::std::*;

fn main() {
    println!("Podaj dwie liczby oddzielone spacjami.");
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    let numbers: Vec<i32> = line
        .trim()
        .split(' ')
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    println!("{} {}", numbers[0], numbers[1]);

    println!("Suma liczb: {}", numbers[0] + numbers[1]);
    println!(
        "Roznica pierwszej i drugiej liczby: {}",
        numbers[0] - numbers[1]
    );
    println!("Iloczyn liczb: {}", numbers[0] * numbers[1]);
    println!(
        "Iloraz pierwszej liczby przez druga: {}",
        numbers[0] / numbers[1]
    );
    println!(
        "Reszta z dzielenia pierwszej liczby przez druga: {}",
        numbers[0] % numbers[1]
    );
    println!(
        "Pierwsza liczba podniesiona do potegi rownej drugiej liczbie: {}",
        numbers[0].pow(numbers[1])
    );
}

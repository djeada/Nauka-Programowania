/*
ZAD-08 — Czy można zbudować trójkąt?

**Poziom:** ★☆☆
**Tagi:** `if`, `geometria`, `warunek trójkąta`

### Treść

Wczytaj trzy dodatnie długości odcinków `a`, `b`, `c`.
Sprawdź, czy można z nich zbudować trójkąt.

Wypisz:

* jeśli tak: `Trójkąt można zbudować z podanych boków.`
* jeśli nie: `Trójkąta nie można zbudować z podanych boków.`

### Wejście

* 1 linia: `a` (całkowita, `a > 0`)
* 2 linia: `b` (całkowita, `b > 0`)
* 3 linia: `c` (całkowita, `c > 0`)

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Ograniczenia / warunek

Trójkąt istnieje wtedy i tylko wtedy, gdy spełnione są wszystkie:

* `a + b > c`
* `a + c > b`
* `b + c > a`

### Przykład

**Wejście:**

```
3
4
5
```

**Wyjście:**

```
Trójkąt można zbudować z podanych boków.
```

*/

use ::std::*;

fn main() {
    println!("Podaj trzy boki trojkata oddzielone spacjami: ");
    let mut wiersz = String::new();
    std::io::stdin()
        .read_line(&mut wiersz)
        .expect("Blad odczytu");
    let liczby: Vec<i32> = wiersz
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let bok_a = liczby[0];
    let bok_b = liczby[1];
    let bok_c = liczby[2];

    if bok_a + bok_b > bok_c && bok_a + bok_c > bok_b && bok_b + bok_c > bok_a {
        println!("Mozna zbudowac trojkat z podanych bokow.");
    } else {
        println!("Nie mozna zbudowac trojkata z podanych bokow.");
    }
}

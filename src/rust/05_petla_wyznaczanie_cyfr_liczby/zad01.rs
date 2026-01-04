/*
ZAD-01 — Liczenie cyfr w liczbie

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — liczba cyfr w `n`.

### Przykład

**Wejście:**

```
342
```

**Wyjście:**

```
3
```

### Ograniczenia / gwarancje

* `n` mieści się w typowym zakresie liczb całkowitych.

### Uwagi o formatowaniu

* Dla `n = 0` poprawna odpowiedź to `1` (liczba „0” ma jedną cyfrę).

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let mut n: i32 = n.trim().parse().unwrap();

    if n == 0 {
        println!("1");
        return;
    }

    let mut count = 0;
    while n > 0 {
        count += 1;
        n /= 10;
    }

    println!("{}", count);
}

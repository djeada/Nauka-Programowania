/*
ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

### Uwagi o formatowaniu

* Dla `n = 0` suma cyfr wynosi `0`.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let mut n: i32 = n.trim().parse().unwrap();

    let mut suma = 0;
    while n > 0 {
        suma += n % 10;
        n /= 10;
    }

    println!("{}", suma);
}

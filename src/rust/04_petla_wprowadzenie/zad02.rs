/*
ZAD-02 — Wypisywanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `for`, `while`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n > 0`) i wypisz wszystkie liczby naturalne mniejsze od `n`, zaczynając od `n - 1` i kończąc na `1`.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

Kolejne liczby naturalne mniejsze od `n`, każda w nowej linii, w kolejności malejącej.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
1
```

### Uwagi o formatowaniu

* Jeśli `n = 1`, nie wypisuj nic.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();

    for i in (1..n).rev() {
        println!("{}", i);
    }
}

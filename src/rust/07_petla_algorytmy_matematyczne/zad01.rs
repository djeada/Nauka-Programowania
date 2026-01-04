/*
ZAD-01 — Obliczanie średniej z n liczb

**Poziom:** ★☆☆
**Tagi:** `pętle`, `suma`, `średnia`, `float`

### Treść

Napisz funkcję `oblicz_srednia()`, która:

1. Wczytuje liczbę naturalną `n` (`n ≥ 1`).
2. Wczytuje następnie `n` liczb (całkowitych lub zmiennoprzecinkowych).
3. Zwraca ich średnią arytmetyczną.

### Wejście

* 1. linia: `n` (`n ≥ 1`)
* kolejne `n` linii: liczby (int lub float)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — średnią arytmetyczną.

### Przykład

**Wejście:**

```
2
4
6
```

**Wywołanie funkcji:**

```python
wynik = oblicz_srednia()
print(wynik)
```

**Wyjście:**

```
5.0
```

### Uwagi o formatowaniu

* Nie narzucamy liczby miejsc po przecinku — wypisz wynik w domyślnym formacie języka (lub jako `float`).

*/

fn oblicz_srednia() -> f64 {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();

    let mut suma = 0.0;
    for _ in 0..n {
        let mut liczba = String::new();
        std::io::stdin().read_line(&mut liczba).unwrap();
        let liczba: f64 = liczba.trim().parse().unwrap();
        suma += liczba;
    }

    suma / (n as f64)
}

fn main() {
    let wynik = oblicz_srednia();
    println!("{}", wynik);
}

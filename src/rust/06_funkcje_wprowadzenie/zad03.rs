/*
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

*/

fn sprawdz_warunki(a: i32, b: i32) -> (bool, bool, bool, bool) {
    let cond_a = a > b;
    let cond_b = a + b < 10;
    let cond_c = a % 2 != 0 && b % 2 != 0;
    let max_val = if a > b { a } else { b };
    let cond_d = max_val < a * a;

    (cond_a, cond_b, cond_c, cond_d)
}

fn main() {
    let (a, b, c, d) = sprawdz_warunki(3, 2);
    println!("{}", a);
    println!("{}", b);
    println!("{}", c);
    println!("{}", d);
}

/*
ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `string`, `pętle`, `odwracanie`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jeden komunikat tekstowy (dokładnie jeden z powyższych).

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Uwagi o formatowaniu

* `0` jest palindromem.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();

    // Odwróć liczbę
    let mut temp = n;
    let mut odwrocona = 0;

    while temp > 0 {
        odwrocona = odwrocona * 10 + temp % 10;
        temp /= 10;
    }

    if n == odwrocona {
        println!("Liczba jest palindromem.");
    } else {
        println!("Liczba nie jest palindromem.");
    }
}

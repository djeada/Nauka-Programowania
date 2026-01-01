/*
ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `wydajność`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w **jednej linii**, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych spacjami.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu linii.
* Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();
    
    fn czy_pierwsza(num: i32) -> bool {
        if num < 2 {
            return false;
        }
        if num == 2 {
            return true;
        }
        if num % 2 == 0 {
            return false;
        }
        let mut i = 3;
        while i * i <= num {
            if num % i == 0 {
                return false;
            }
            i += 2;
        }
        true
    }
    
    let mut count = 0;
    let mut candidate = 2;
    let mut pierwsze = Vec::new();
    
    while count < n {
        if czy_pierwsza(candidate) {
            pierwsze.push(candidate);
            count += 1;
        }
        candidate += 1;
    }
    
    for (i, p) in pierwsze.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", p);
    }
    println!();
}

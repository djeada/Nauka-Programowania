/*
ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

**Poziom:** ★★☆
**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów `A(xA, yA)`, `B(xB, yB)`, `C(xC, yC)`.
Wypisz `Tak`, jeśli punkty **nie są współliniowe** (mogą tworzyć trójkąt), w przeciwnym razie `Nie`.

### Wejście

Sześć liczb całkowitych (każda w osobnej linii):

1. `xA`
2. `yA`
3. `xB`
4. `yB`
5. `xC`
6. `yC`

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
-3
-2
-3
1
-3
0
```

**Wyjście:**

```
Nie
```

### Uwagi

* Sprawdź pole trójkąta: jeśli równe `0`, punkty są współliniowe.

*/
fn main() {
    let mut coords = Vec::new();
    for _ in 0..6 {
        let mut line = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let coord: i32 = line.trim().parse().unwrap();
        coords.push(coord);
    }
    
    let xa = coords[0];
    let ya = coords[1];
    let xb = coords[2];
    let yb = coords[3];
    let xc = coords[4];
    let yc = coords[5];
    
    // Punkty są współliniowe jeśli wyznacznik jest 0
    // det = (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)
    let det = (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya);
    
    if det != 0 {
        println!("Tak");
    } else {
        println!("Nie");
    }
}

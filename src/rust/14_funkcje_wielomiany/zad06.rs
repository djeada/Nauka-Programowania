/*
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję, która otrzymuje listę współczynników równania kwadratowego `[a, b, c]` dla `a x^2 + b x + c` i zwraca listę **rzeczywistych** miejsc zerowych.

### Wejście (argumenty funkcji)

* `coef` — lista trzech liczb `[a, b, c]`

### Wyjście (zwracana wartość)

* lista liczb zmiennoprzecinkowych:

  * jeśli `Δ < 0` → pusta lista `[]`
  * jeśli `Δ = 0` → dwa jednakowe pierwiastki `[x, x]`
  * jeśli `Δ > 0` → dwa pierwiastki `[x1, x2]` (kolejność dowolna)

### Przykład

Dla `[1, 2, 1]` funkcja zwraca:
`[-1.0, -1.0]`

### Ograniczenia / gwarancje

* Zakładamy `a ≠ 0` (to naprawdę równanie kwadratowe).

### Uwagi

* Licz `Δ = b^2 - 4ac`.
* Pierwiastki: `(-b ± sqrt(Δ)) / (2a)`.

*/

fn miejsca_zerowe_kwadratowe(coef: &[f64; 3]) -> Vec<f64> {
    let a = coef[0];
    let b = coef[1];
    let c = coef[2];

    let delta = b * b - 4.0 * a * c;

    if delta < 0.0 {
        // Brak rzeczywistych pierwiastków
        Vec::new()
    } else if delta == 0.0 {
        // Jeden pierwiastek (podwójny)
        let x = -b / (2.0 * a);
        vec![x, x]
    } else {
        // Dwa różne pierwiastki
        let sqrt_delta = delta.sqrt();
        let x1 = (-b + sqrt_delta) / (2.0 * a);
        let x2 = (-b - sqrt_delta) / (2.0 * a);
        vec![x1, x2]
    }
}

fn main() {
    // Przykład: [1, 2, 1] -> x^2 + 2x + 1 = 0
    let coef = [1.0, 2.0, 1.0];

    let wynik = miejsca_zerowe_kwadratowe(&coef);
    println!("{:?}", wynik);
}

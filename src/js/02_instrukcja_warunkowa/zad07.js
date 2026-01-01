/*
ZAD-07 — Prawa logiki (p i q)

**Poziom:** ★★☆
**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Dla wszystkich kombinacji wartości logicznych `p` i `q` (True/False) sprawdź poprawność praw:

1. Wyłączony środek: `p OR (NOT p)`
2. Niesprzeczność: `NOT (p AND (NOT p))`
3. Przemienność AND: `p AND q` vs `q AND p`
4. Przemienność OR: `p OR q` vs `q OR p`
5. De Morgana 1: `NOT (p AND q)` vs `(NOT p) OR (NOT q)`
6. De Morgana 2: `NOT (p OR q)` vs `(NOT p) AND (NOT q)`

### Wejście

Brak.

### Wyjście

Żeby wynik był **jednoznaczny i łatwy do sprawdzenia**, zastosuj dokładnie ten format:

Dla każdego z 6 praw wypisz:

* nazwę prawa w jednej linii,
* następnie w osobnych liniach wynik dla każdej kombinacji `p, q` w kolejności:

  1. `p=False, q=False`
  2. `p=False, q=True`
  3. `p=True, q=False`
  4. `p=True, q=True`

Każda linia kombinacji ma mieć format:
`p=<...> q=<...> L=<...> R=<...> EQ=<...>`

Gdzie `<...>` to dosłownie `True` albo `False`.

### Przykład fragmentu (dla jednego prawa)

```
Przemienność alternatywy:
p=False q=False L=False R=False EQ=True
p=False q=True L=True R=True EQ=True
p=True q=False L=True R=True EQ=True
p=True q=True L=True R=True EQ=True
```

### Uwagi o formatowaniu

* Dokładne nazwy praw (nagłówki) użyj jak poniżej:

  1. `Prawo wyłączonego środka:`
  2. `Prawo niesprzeczności:`
  3. `Przemienność koniunkcji:`
  4. `Przemienność alternatywy:`
  5. `Pierwsze prawo de Morgana:`
  6. `Drugie prawo de Morgana:`
* Między blokami praw możesz wstawić **jedną pustą linię** (zalecane), ale nie więcej.

*/

// Helper function to convert boolean to string
function boolToStr(val) {
  return val ? "True" : "False";
}

// All combinations of p and q
const combinations = [
  [false, false],
  [false, true],
  [true, false],
  [true, true]
];

// 1. Prawo wylaczonego srodka: p OR (NOT p)
console.log("Prawo wyłączonego środka:");
for (const [p, q] of combinations) {
  const L = p || !p;
  const R = true; // always true
  const EQ = L === R;
  console.log(`p=${boolToStr(p)} q=${boolToStr(q)} L=${boolToStr(L)} R=${boolToStr(R)} EQ=${boolToStr(EQ)}`);
}
console.log("");

// 2. Prawo niesprzecznosci: NOT (p AND (NOT p))
console.log("Prawo niesprzeczności:");
for (const [p, q] of combinations) {
  const L = !(p && !p);
  const R = true; // always true
  const EQ = L === R;
  console.log(`p=${boolToStr(p)} q=${boolToStr(q)} L=${boolToStr(L)} R=${boolToStr(R)} EQ=${boolToStr(EQ)}`);
}
console.log("");

// 3. Przemiennosc koniunkcji: (p AND q) === (q AND p)
console.log("Przemienność koniunkcji:");
for (const [p, q] of combinations) {
  const L = p && q;
  const R = q && p;
  const EQ = L === R;
  console.log(`p=${boolToStr(p)} q=${boolToStr(q)} L=${boolToStr(L)} R=${boolToStr(R)} EQ=${boolToStr(EQ)}`);
}
console.log("");

// 4. Przemiennosc alternatywy: (p OR q) === (q OR p)
console.log("Przemienność alternatywy:");
for (const [p, q] of combinations) {
  const L = p || q;
  const R = q || p;
  const EQ = L === R;
  console.log(`p=${boolToStr(p)} q=${boolToStr(q)} L=${boolToStr(L)} R=${boolToStr(R)} EQ=${boolToStr(EQ)}`);
}
console.log("");

// 5. Pierwsze prawo de Morgana: NOT(p AND q) === (NOT p) OR (NOT q)
console.log("Pierwsze prawo de Morgana:");
for (const [p, q] of combinations) {
  const L = !(p && q);
  const R = !p || !q;
  const EQ = L === R;
  console.log(`p=${boolToStr(p)} q=${boolToStr(q)} L=${boolToStr(L)} R=${boolToStr(R)} EQ=${boolToStr(EQ)}`);
}
console.log("");

// 6. Drugie prawo de Morgana: NOT(p OR q) === (NOT p) AND (NOT q)
console.log("Drugie prawo de Morgana:");
for (const [p, q] of combinations) {
  const L = !(p || q);
  const R = !p && !q;
  const EQ = L === R;
  console.log(`p=${boolToStr(p)} q=${boolToStr(q)} L=${boolToStr(L)} R=${boolToStr(R)} EQ=${boolToStr(EQ)}`);
}


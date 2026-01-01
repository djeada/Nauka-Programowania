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

// Funkcja sprawdzajaca, czy punkty moga stanowic wierzcholki trojkata
function czyTrojkat(punkty) {
  var xA = punkty[0];
  var yA = punkty[1];
  var xB = punkty[2];
  var yB = punkty[3];
  var xC = punkty[4];
  var yC = punkty[5];

  var AB = Math.sqrt(Math.pow(xB - xA, 2) + Math.pow(yB - yA, 2));
  var BC = Math.sqrt(Math.pow(xC - xB, 2) + Math.pow(yC - yB, 2));
  var AC = Math.sqrt(Math.pow(xC - xA, 2) + Math.pow(yC - yA, 2));

  return AB + BC > AC && AB + AC > BC && BC + AC > AB;
}

// Testy

function testCzyTrojkat() {
  console.assert(czyTrojkat([-3, -2, -3, 1, -3, 0]) === false);
  console.assert(czyTrojkat([0, 0, 3, 0, 0, 4]) === true);
  console.assert(czyTrojkat([0, 0, 0, 0, 0, 0]) === false);
  console.assert(czyTrojkat([1, 2, 2, 2, 3, 2]) === false);
  console.assert(czyTrojkat([0, 0, 5, 0, 0, 5]) === true);
}

testCzyTrojkat();


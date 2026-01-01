/*
ZAD-07A — Pole trójkąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole trójkąta ze wzoru:
( P = \frac{1}{2} a h )

### Wejście

* 1 linia: `a`
* 2 linia: `h`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
6
4
```

**Wyjście:**

```
12.000
```

ZAD-07B — Pole prostokąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole prostokąta:
( P = ab )

### Wejście

* 1 linia: `a`
* 2 linia: `b`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2.5
4
```

**Wyjście:**

```
10.000
```

ZAD-07C — Pole rombu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole rombu z przekątnych:
( P = \frac{1}{2} d_1 d_2 )

### Wejście

* 1 linia: `d1`
* 2 linia: `d2`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
10
6
```

**Wyjście:**

```
30.000
```

ZAD-07D — Objętość kuli

**Poziom:** ★★☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Oblicz objętość kuli:
( V = \frac{4}{3}\pi r^3 )

### Wejście

* 1 linia: `r`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
1
```

**Wyjście:**

```
4.189
```

ZAD-07E — Objętość stożka

**Poziom:** ★★☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Oblicz objętość stożka:
( V = \frac{1}{3}\pi r^2 h )

### Wejście

* 1 linia: `r`
* 2 linia: `h`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
12.566
```

ZAD-07F — Objętość prostopadłościanu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz objętość prostopadłościanu:
( V = abc )

### Wejście

* 1 linia: `a`
* 2 linia: `b`
* 3 linia: `c`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2
3
4
```

**Wyjście:**

```
24.000
```

*/

// a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz jego pole.
const base = parseInt(prompt("Podaj dlugosc podstawy trojkata:"));
const wysokosc_trojkata = parseInt(prompt("Podaj wysokosc trojkata:"));
console.log((base * wysokosc_trojkata) / 2);

// b) Pobierz dlugosci bokow prostokata i wypisz jego pole.
const side_a = parseInt(prompt("Podaj dlugosc boku a prostokata:"));
const side_b = parseInt(prompt("Podaj dlugosc boku b prostokata:"));
console.log(side_a * side_b);

// c) Pobierz dlugosci przekatnych rombu i wypisz jego pole.
const diagonal_a = parseInt(prompt("Podaj dlugosc przekatnej a rombu:"));
const diagonal_b = parseInt(prompt("Podaj dlugosc przekatnej b rombu:"));
console.log((diagonal_a * diagonal_b) / 2);

// d) Pobierz promien kuli i wypisz jej objetosc.
const radius = parseInt(prompt("Podaj promien kuli:"));
console.log((4 / 3) * Math.PI * radius ** 3);

// e) Pobierz promien podstawy i wysokosc stozka i wypisz jego objetosc.
const base_radius = parseInt(prompt("Podaj promien podstawy stozka:"));
const wysokosc_stozka = parseInt(prompt("Podaj wysokosc stozka:"));
console.log((Math.PI * base_radius ** 2 * wysokosc_stozka) / 3);

// f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz jego objetosc.
const length = parseInt(prompt("Podaj dlugosc graniastoslupa:"));
const width = parseInt(prompt("Podaj szerokosc graniastoslupa:"));
const wysokosc_graniastoslupa = parseInt(
  prompt("Podaj wysokosc graniastoslupa:")
);
console.log(length * width * wysokosc_graniastoslupa);


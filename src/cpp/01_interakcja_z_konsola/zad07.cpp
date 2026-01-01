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
#include <iostream>

int main() {
  std::cout << "podaj podstawe i wysokosc trojkata:" << std::endl;

  float a;
  float b;

  std::cin >> a;
  std::cin >> b;

  std::cout << "pole trojkata o podstawie " << a << " i wysokosci " << b
            << " jest rowne " << a * b / 2 << std::endl;

  std::cout << "podaj dlugosci bokow prostokata:" << std::endl;

  std::cin >> a;
  std::cin >> b;

  std::cout << "pole prostokata o bokach " << a << " i " << b << " jest rowne "
            << a * b << std::endl;

  std::cout << "podaj dlugosci przekatnych rombu:" << std::endl;
  std::cin >> a;
  std::cin >> b;
  std::cout << "pole rombu o przekotnych " << a << " i " << b << " jest rowne "
            << a * b / 2 << std::endl;

  std::cout << "podaj promien kuli:" << std::endl;
  std::cin >> a;
  std::cout << "objetosc kuli o promieniu " << a << " jest rowna "
            << 4 / 3 * 3.14 * a * a * a << std::endl;

  std::cout << "podaj promien podstawy i wysokosc stozka:" << std::endl;
  std::cin >> a;
  std::cin >> b;
  std::cout << "objetosc stozka o promieniu podstawy " << a << " i wysokosci "
            << b << " jest rowna " << 1 / 3 * 3.14 * a * a * b << std::endl;

  std::cout << "podaj dlugosc, szerokosc i wysokosc graniastoslupa:"
            << std::endl;
  std::cin >> a;
  std::cin >> b;
  float c;
  std::cin >> c;
  std::cout << "objetosc graniastoslupa o dlugosci " << a << " szerokosci " << b
            << " i wysokosci " << c << " jest rowna " << a * b * c << std::endl;

  return 0;
}

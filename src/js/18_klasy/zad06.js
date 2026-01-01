/*
ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operacje`, `math`

### Treść

Zaprojektuj klasę **LiczbaZespolona**:

* konstruktor `(re=0, im=0)`,
* dodawanie, odejmowanie, mnożenie, dzielenie,
* porównania,
* moduł,
* wypisywanie w formacie `a + bi` lub `a - bi` (z zachowaniem znaku).

Program tworzy:

* A = 9 + 12i
* B = -3 - 3i

Wypisuje A, B oraz: sumę, różnicę A-B, iloczyn i iloraz A/B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Liczba A: 9 + 12i
Liczba B: -3 - 3i

Suma: 6 + 9i
Różnica A - B: 12 + 15i
Iloczyn: 27 + 63i
Iloraz A / B: -3.5 + 0.5i
```

*/

class Zespolona {
  constructor(real = 0, imag = 0) {
    this.real = real;
    this.imag = imag;
  }

  dodaj(innaLiczba) {
    return new Zespolona(
      this.real + innaLiczba.real,
      this.imag + innaLiczba.imag
    );
  }

  odejmij(innaLiczba) {
    return new Zespolona(
      this.real - innaLiczba.real,
      this.imag - innaLiczba.imag
    );
  }

  pomnoz(innaLiczba) {
    return new Zespolona(
      this.real * innaLiczba.real - this.imag * innaLiczba.imag,
      this.real * innaLiczba.imag + this.imag * innaLiczba.real
    );
  }

  podziel(innaLiczba) {
    const mianownik = innaLiczba.real ** 2 + innaLiczba.imag ** 2;
    return new Zespolona(
      (this.real * innaLiczba.real + this.imag * innaLiczba.imag) / mianownik,
      (this.imag * innaLiczba.real - this.real * innaLiczba.imag) / mianownik
    );
  }

  modul() {
    return Math.sqrt(this.real ** 2 + this.imag ** 2);
  }

  wypiszInfo() {
    console.log(`Liczba zespolona: ${this.real} + ${this.imag}i`);
  }
}

const A = new Zespolona(9, 12);
const B = new Zespolona(-3, -3);

A.wypiszInfo();
B.wypiszInfo();

const suma = A.dodaj(B);
suma.wypiszInfo();

const roznica = A.odejmij(B);
roznica.wypiszInfo();

const iloraz = A.podziel(B);
iloraz.wypiszInfo();

const iloczyn = A.pomnoz(B);
iloczyn.wypiszInfo();


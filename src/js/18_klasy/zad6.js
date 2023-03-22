/*
Tytuł: Zaprojektuj klasę Zespolona.

Treść: Napisz klasę Zespolona, która będzie reprezentowała liczbę zespoloną. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje jako argument dwie liczby. Pierwsza liczba reprezentuje część rzeczywistą, a druga część urojoną liczby zespolonej. Domyślne wartości dla obu argumentów to 0.
2. Funkcje, które zwracają wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnożenie, dzielenie). Jeśli jest to możliwe, należy przeciążyć operatory: +, -, *, /.
3. Funkcję, która wypisuje informacje o liczbie zespolonej na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Zespolona. Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.
5. Funkcję moduł, która zwraca moduł liczby zespolonej.

Napisz program, który przetestuje twoją klasę. Stwórz liczby zespolone: A (9, 12) oraz B (-3, -3). Wypisz na standardowe wyjście informacje o utworzonych liczbach zespolonych oraz ich sumę, różnicę pierwszej i drugiej, iloraz pierwszej przez drugą oraz iloczyn liczb zespolonych.
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

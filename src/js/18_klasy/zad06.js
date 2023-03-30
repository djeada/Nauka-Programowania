/*
Tytul: Zaprojektuj klase Zespolona.

Tresc: Napisz klase Zespolona, ktora bedzie reprezentowala liczbe zespolona. Klasa powinna zawierac nastepujace funkcje:

1. Konstruktor, ktory przyjmuje jako argument dwie liczby. Pierwsza liczba reprezentuje czesc rzeczywista, a druga czesc urojona liczby zespolonej. Domyslne wartosci dla obu argumentow to 0.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie, dzielenie). Jesli jest to mozliwe, nalezy przeciazyc operatory: +, -, *, /.
3. Funkcje, ktora wypisuje informacje o liczbie zespolonej na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Zespolona. Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.
5. Funkcje modul, ktora zwraca modul liczby zespolonej.

Napisz program, ktory przetestuje twoja klase. Stworz liczby zespolone: A (9, 12) oraz B (-3, -3). Wypisz na standardowe wyjscie informacje o utworzonych liczbach zespolonych oraz ich sume, roznice pierwszej i drugiej, iloraz pierwszej przez druga oraz iloczyn liczb zespolonych.
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


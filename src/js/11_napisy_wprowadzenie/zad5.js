/*
Tytul: Wypisz co k-ty znak napisu poziomo i pionowo.

Tresc: Otrzymasz napis oraz liczbe k.

a) Wypisz co k-ty znak napisu poziomo, rozdzielajac znaki spacjami.

b) Wypisz co k-ty znak napisu pionowo, rozdzielajac znaki enterami.

Dane wejsciowe: Napis oraz liczba.

Dane wyjsciowe: Napis.

Przyklad:

a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis: "z h n".

b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis:
    
    z
    h
    n
*/

function coKtyPoziomo(napis, k) {
  let wynik = "";
  for (let i = k - 1; i < napis.length; i += k) {
    wynik += napis[i] + " ";
  }
  return wynik.trim();
}

function coKtyPionowo(napis, k) {
  let wynik = "";
  for (let i = k - 1; i < napis.length; i += k) {
    wynik += napis[i] + "\n";
  }
  return wynik.trim();
}

// Testy

function test() {
  let input1 = "Grzechotnik";
  let input2 = 3;
  let expectedOutput1 = "z h n";
  let expectedOutput2 = "z\nh\nn";
  let output1 = coKtyPoziomo(input1, input2);
  let output2 = coKtyPionowo(input1, input2);

  console.assert(output1 === expectedOutput1, "Test nie powiodl sie");
  console.assert(output2 === expectedOutput2, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();


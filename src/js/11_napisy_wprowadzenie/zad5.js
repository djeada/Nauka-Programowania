/*
Tytuł: Wypisz co k-ty znak napisu poziomo i pionowo.

Treść: Otrzymasz napis oraz liczbę k.

a) Wypisz co k-ty znak napisu poziomo, rozdzielając znaki spacjami.

b) Wypisz co k-ty znak napisu pionowo, rozdzielając znaki enterami.

Dane wejściowe: Napis oraz liczba.

Dane wyjściowe: Napis.

Przykład:

a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostać zwrócony napis: "z h n".

b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostać zwrócony napis:
    
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

  assert(output1 === expectedOutput1, "Test nie powiódł się");
  assert(output2 === expectedOutput2, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();

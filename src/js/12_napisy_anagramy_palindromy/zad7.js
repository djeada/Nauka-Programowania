/*
Tytuł: Minimalna ilość usuniętych znaków, aby uzyskać anagramy.

Treść: Napisz program, który dla dwóch słów zwróci minimalną ilość znaków, które trzeba usunąć, aby uzyskać anagramy. Jeśli słowa są różnej długości, zwróć -1.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych napisów: “grazyna” oraz “razynax”, powinna zostać zwrócona liczba: 2.
*/

function minUsunieciaDoAnagramow(napis1, napis2) {
  if (napis1.length !== napis2.length) {
    return -1;
  }

  const licznikZnakow = {};

  for (const znak of napis1) {
    if (licznikZnakow[znak]) {
      licznikZnakow[znak]++;
    } else {
      licznikZnakow[znak] = 1;
    }
  }

  let usuniecia = 0;
  for (const znak of napis2) {
    if (licznikZnakow[znak]) {
      licznikZnakow[znak]--;
    } else {
      usuniecia++;
    }
  }

  return usuniecia;
}

// Test

function test() {
  const input1 = "grazyna";
  const input2 = "razynax";
  const expectedOutput = 2;
  const output = minUsunieciaDoAnagramow(input1, input2);

  assert(
    output === expectedOutput,
    'Test nie powiódł się dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();

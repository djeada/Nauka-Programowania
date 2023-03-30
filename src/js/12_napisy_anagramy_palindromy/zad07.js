/*
Tytul: Minimalna ilosc usunietych znakow, aby uzyskac anagramy.

Tresc: Napisz program, ktory dla dwoch slow zwroci minimalna ilosc znakow, ktore trzeba usunac, aby uzyskac anagramy. Jesli slowa sa roznej dlugosci, zwroc -1.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanych napisow: “grazyna” oraz “razynax”, powinna zostac zwrocona liczba: 2.
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

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();


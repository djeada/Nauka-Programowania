/*
Tytul: Lista pracownikow z najwiekszymi zyskami.

Tresc: Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwisko pracownika, drugim zysk z transakcji, jaka dany pracownik przeprowadzil. Znajdz pracownika, ktory przyniosl firmie najwiecej zysku.

Dane wejsciowe: Lista par napisow i liczb naturalnych.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanej listy:

[["Barnaba Barabash", 120],
["Jon Snow", 100],
["Kira Summer", 300],
["Barnaba Barabash", 200],
["Bob Marley", 110]]

zostanie zwrocony napis: “Barnaba Barabash”.


*/
function najwiekszyZysk(lista) {
  const pracownicy = {};
  let najlepszyPracownik = "";
  let najlepszyZysk = -Infinity;
  for (let i = 0; i < lista.length; i++) {
    const [pracownik, zysk] = lista[i];
    if (!pracownicy[pracownik]) {
      pracownicy[pracownik] = 0;
    }
    pracownicy[pracownik] += zysk;
    if (pracownicy[pracownik] > najlepszyZysk) {
      najlepszyZysk = pracownicy[pracownik];
      najlepszyPracownik = pracownik;
    }
  }
  return najlepszyPracownik;
}

function testNajwiekszyZysk() {
  const lista1 = [
    ["Barnaba Barabash", 120],
    ["Jon Snow", 100],
    ["Kira Summer", 300],
    ["Barnaba Barabash", 200],
    ["Bob Marley", 110],
  ];
  const wynik1 = najwiekszyZysk(lista1);
  console.assert(wynik1 === "Barnaba Barabash", "Test 1 nie powiodl sie");

  const lista2 = [
    ["Anna Nowak", 200],
    ["Piotr Kowalski", 50],
    ["Anna Nowak", 300],
    ["Jan Kowalski", 100],
  ];
  const wynik2 = najwiekszyZysk(lista2);
  console.assert(wynik2 === "Anna Nowak", "Test 2 nie powiodl sie");
}

testNajwiekszyZysk();


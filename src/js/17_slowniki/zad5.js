/*
Tytuł: Lista pracowników z największymi zyskami.

Treść: Otrzymujesz listę par. Pierwszym elementem pary jest napis reprezentujący imię i nazwisko pracownika, drugim zysk z transakcji, jaką dany pracownik przeprowadził. Znajdź pracownika, który przyniósł firmie najwięcej zysku.

Dane wejściowe: Lista par napisów i liczb naturalnych.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanej listy:

[["Barnaba Barabash", 120],
["Jon Snow", 100],
["Kira Summer", 300],
["Barnaba Barabash", 200],
["Bob Marley", 110]]

zostanie zwrócony napis: “Barnaba Barabash”.


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
  console.assert(wynik1 === "Barnaba Barabash", "Test 1 nie powiódł się");

  const lista2 = [
    ["Anna Nowak", 200],
    ["Piotr Kowalski", 50],
    ["Anna Nowak", 300],
    ["Jan Kowalski", 100],
  ];
  const wynik2 = najwiekszyZysk(lista2);
  console.assert(wynik2 === "Anna Nowak", "Test 2 nie powiódł się");
}

testNajwiekszyZysk();

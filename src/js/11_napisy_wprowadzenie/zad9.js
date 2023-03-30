/*
Tytul: Wczytaj i rozdziel informacje o pracowniku.

Tresc: Otrzymasz rekord z bazy danych reprezentujacy dane pracownika. Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje sa rozdzielone srednikami. Zapisz je w osobnych zmiennych i wypisz je razem z odpowiednimi komunikatami.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanego napisu:
"Jan; Kowalski; Warszawa; Programista; 1000;",

powinna zostac zwrocona lista:
["Imie: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawod: Programista", "Zarobki: 1000"].
*/

function rozdzielRekord(rekord) {
  let dane = rekord.split(";");
  let imie = dane[0].trim();
  let nazwisko = dane[1].trim();
  let miejsceUrodzenia = dane[2].trim();
  let zawod = dane[3].trim();
  let zarobki = dane[4].trim();

  let lista = [
    "Imie: " + imie,
    "Nazwisko: " + nazwisko,
    "Miejsce urodzenia: " + miejsceUrodzenia,
    "Zawod: " + zawod,
    "Zarobki: " + zarobki,
  ];
  return lista;
}

// Test

function test() {
  let input = "Jan; Kowalski; Warszawa; Programista; 1000;";
  let expectedOutput = [
    "Imie: Jan",
    "Nazwisko: Kowalski",
    "Miejsce urodzenia: Warszawa",
    "Zawod: Programista",
    "Zarobki: 1000",
  ];
  let output = rozdzielRekord(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiodl sie"
  );
  console.log("Test przeszedl pomyslnie");
}

test();


/*
Tytuł: Wczytaj i rozdziel informacje o pracowniku.

Treść: Otrzymasz rekord z bazy danych reprezentujący dane pracownika. Są to kolejno: imię, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje są rozdzielone średnikami. Zapisz je w osobnych zmiennych i wypisz je razem z odpowiednimi komunikatami.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu:
"Jan; Kowalski; Warszawa; Programista; 1000;",

powinna zostać zwrócona lista:
["Imię: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawód: Programista", "Zarobki: 1000"].
*/

function rozdzielRekord(rekord) {
  let dane = rekord.split(";");
  let imie = dane[0].trim();
  let nazwisko = dane[1].trim();
  let miejsceUrodzenia = dane[2].trim();
  let zawod = dane[3].trim();
  let zarobki = dane[4].trim();

  let lista = [
    "Imię: " + imie,
    "Nazwisko: " + nazwisko,
    "Miejsce urodzenia: " + miejsceUrodzenia,
    "Zawód: " + zawod,
    "Zarobki: " + zarobki,
  ];
  return lista;
}

// Test

function test() {
  let input = "Jan; Kowalski; Warszawa; Programista; 1000;";
  let expectedOutput = [
    "Imię: Jan",
    "Nazwisko: Kowalski",
    "Miejsce urodzenia: Warszawa",
    "Zawód: Programista",
    "Zarobki: 1000",
  ];
  let output = rozdzielRekord(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiódł się"
  );
  console.log("Test przeszedł pomyślnie");
}

test();

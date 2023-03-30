/*

Tytul: Nazwa pliku bez rozszerzenia.

Tresc: Otrzymujesz napis reprezentujacy sciezke pliku. Odfiltruj z niego nazwe pliku wraz z rozszerzeniem. Zwroc sama nazwe pliku bez rozszerzenia.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu "C:\my-long\path_directory\file.html", powinna zostac zwrocona nazwa pliku bez rozszerzenia "file".

*/

function nazwa_pliku(napis) {
  const nazwa = /[^\\/]+(?=\.\w+$)/;
  const wynik = napis.match(nazwa);

  return wynik ? wynik[0] : "";
}

function test_nazwa_pliku() {
  console.assert(
    nazwa_pliku("C:\\my-long\\path_directory\\file.html") === "file"
  );
  console.assert(nazwa_pliku("file.html") === "file");
  console.assert(nazwa_pliku("/root/home/adam/file.html") === "file");
}

test_nazwa_pliku();


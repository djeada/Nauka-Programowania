/*

Tytuł: Nazwa pliku bez rozszerzenia.

Treść: Otrzymujesz napis reprezentujący ścieżkę pliku. Odfiltruj z niego nazwę pliku wraz z rozszerzeniem. Zwróć samą nazwę pliku bez rozszerzenia.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu "C:\my-long\path_directory\file.html", powinna zostać zwrócona nazwa pliku bez rozszerzenia "file".

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

/*
Tytuł: Znalezienie w folderze wszystkich plików z danym rozszerzeniem

Treść: Otrzymujesz dwa napisy. Pierwszy napis to ścieżka folderu, a drugi to rozszerzenie szukanych plików. Znajdź w folderze wszystkie pliki o podanym rozszerzeniu i zapisz ich nazwy w liście.

Dane wejściowe: Dwa napisy

Dane wyjściowe: Lista napisów
*/

const fs = require("fs").promises;
const path = require("path");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

const znajdzPliki = async (sciezka, rozszerzenie) => {
  const pliki = [];
  const dane = await fs.readdir(sciezka);
  for (const danePliku of dane) {
    const sciezkaPliku = path.join(sciezka, danePliku);
    const stat = await fs.lstat(sciezkaPliku);
    if (stat.isFile() && path.extname(danePliku) === rozszerzenie) {
      pliki.push(danePliku);
    }
  }
  return pliki;
};

const testZnajdzPliki = async () => {
  const sciezkaFolderu = "temp_dir";
  const sciezkiPlikow = ["lista.txt", "test.txt"];
  const tekst = "przykladowy tekst.\n";

  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  const oczekiwane = sciezkiPlikow;
  const wynik = await znajdzPliki(sciezkaFolderu, ".txt");

  assert(
    wynik.length === oczekiwane.length,
    `Błąd testu znajdzPliki: ${wynik.length} !== ${oczekiwane.length}`
  );

  for (const nazwaPliku of oczekiwane) {
    assert(
      wynik.includes(nazwaPliku),
      `Błąd testu znajdzPliki: ${wynik} nie zawiera ${nazwaPliku}`
    );
  }

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await testZnajdzPliki();
};

main();

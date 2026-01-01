/*
ZAD-11 — Nazwa pliku bez rozszerzenia

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Otrzymujesz napis reprezentujący pełną ścieżkę do pliku. Wyodrębnij nazwę pliku (bez katalogów) i usuń rozszerzenie (część po ostatniej kropce). Zwróć samą nazwę bez rozszerzenia.

Ścieżka może zawierać separator `\` lub `/`.

### Wejście

Jedna linia:

* `sciezka`

### Wyjście

Jedna linia:

* `nazwa_pliku_bez_rozszerzenia`

### Przykład

**Wejście:**

```
C:\my-long\path_directory\file.html
```

**Wyjście:**

```
file
```

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


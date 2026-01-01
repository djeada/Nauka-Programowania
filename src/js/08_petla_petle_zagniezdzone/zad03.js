/*
ZAD-03 — Trójkąt prostokątny (malejący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz odwrócony trójkąt o wysokości `n`, zaczynając od `n` gwiazdek i kończąc na `1`.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `n` gwiazdek
* 2. linia: `n-1` gwiazdek
* …
* ostatnia linia: `*`

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
****
***
**
*
```

*/
function main() {
  const n = parseInt(prompt("Podaj liczbe:"));
  
  for (let i = n; i >= 1; i--) {
    let wiersz = "";
    for (let j = 0; j < i; j++) {
      wiersz += "*";
    }
    console.log(wiersz);
  }
}

main();

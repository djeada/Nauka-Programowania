/*
ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `listy`, `kombinatoryka`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt Pascala o wysokości `n`.

Wiersz 1: `1`
Wiersz 2: `1 1`
Wiersz 3: `1 2 1`
itd.

Liczby w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w `i`-tej linii jest `i` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

*/
function main() {
  const n = parseInt(prompt("Podaj liczbe:"));
  
  for (let i = 0; i < n; i++) {
    let wiersz = [];
    for (let j = 0; j <= i; j++) {
      if (j === 0 || j === i) {
        wiersz.push(1);
      } else {
        // Calculate binomial coefficient C(i,j) = i! / (j! * (i-j)!)
        let val = 1;
        for (let k = 0; k < j; k++) {
          val = val * (i - k) / (k + 1);
        }
        wiersz.push(Math.round(val));
      }
    }
    console.log(wiersz.join(" "));
  }
}

main();

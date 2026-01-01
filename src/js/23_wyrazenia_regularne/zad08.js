/*
ZAD-08 — Cyfry w słowach

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz zdanie. Wyodrębnij wszystkie ciągi cyfr, które są częścią słów (czyli są bezpośrednio połączone z literami). Nie uwzględniaj cyfr oddzielonych od liter spacjami.

### Wejście

Jedna linia:

* `zdanie`

### Wyjście

Każdy znaleziony ciąg cyfr w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

**Wyjście:**

```
29
37
3
91
```

*/

function cyfry_w_slowach(napis) {
  const cyfry = /\d+/g;

  return napis.match(cyfry);
}

function test_cyfry_w_slowach() {
  console.assert(
    cyfry_w_slowach(
      "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego"
    ).join("") === "293793389122"
  );
  console.assert(
    cyfry_w_slowach(
      "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego"
    ).join(" ") === "29 37 3891 22"
  );
}

test_cyfry_w_slowach();


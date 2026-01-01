/*
ZAD-05 — Pracownik z największym sumarycznym zyskiem

**Poziom:** ★☆☆
**Tagi:** `dict`, `sumowanie`

### Treść

Wczytaj `n` wpisów: `pracownik zysk`. Zsumuj zyski per pracownik i wypisz nazwę pracownika z największą sumą.
(Jeśli remis, wybierz tego, który pierwszy osiągnął tę maksymalną sumę podczas przetwarzania.)

### Wejście

* 1 linia: `n`
* następnie `n` linii: `imie_i_nazwisko zysk`

### Wyjście

* Jedna linia: `imie_i_nazwisko`

### Przykład

**Wejście:**

```
5
Barnaba_Barabash 120
Jon_Snow 100
Kira_Summer 300
Barnaba_Barabash 200
Bob_Marley 110
```

**Wyjście:**

```
Barnaba_Barabash
```

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
  console.assert(wynik1 === "Barnaba Barabash", "Test 1 nie powiodl sie");

  const lista2 = [
    ["Anna Nowak", 200],
    ["Piotr Kowalski", 50],
    ["Anna Nowak", 300],
    ["Jan Kowalski", 100],
  ];
  const wynik2 = najwiekszyZysk(lista2);
  console.assert(wynik2 === "Anna Nowak", "Test 2 nie powiodl sie");
}

testNajwiekszyZysk();


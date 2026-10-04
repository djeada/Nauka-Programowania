/*
ZAD-09 — Słowa elfickie

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `napisy`

### Treść

**Słowem elfickim** nazywamy napis, w którym każda z liter słowa `elf` (czyli `e`, `l` i `f`) występuje co najmniej raz, w dowolnej kolejności i na dowolnych pozycjach.

Napisz rekurencyjną funkcję `czy_elfickie(slowo, litery="elf")`, która sprawdza, czy każda litera z napisu `litery` występuje w napisie `slowo`. Program wczytuje słowo i wypisuje wynik sprawdzenia.

### Wejście

Jedna linia: słowo złożone z małych liter alfabetu łacińskiego (`a`–`z`).

### Wyjście

`Prawda`, jeśli słowo jest elfickie, w przeciwnym razie `Fałsz`.

### Ograniczenia

* długość słowa: od 1 do 100 znaków

### Przykład

**Wejście:**

```
reflektor
```

**Wyjście:**

```
Prawda
```

W słowie `reflektor` występują litery `e`, `l` i `f`.

### Uwagi

* Sprawdź, czy w słowie występuje pierwsza litera z `litery`, i wywołaj funkcję dla pozostałych liter (`litery[1:]`). Gdy `litery` jest pusty, wszystkie litery zostały znalezione.
* Samo szukanie litery w słowie też możesz zapisać rekurencyjnie: litera występuje w słowie, jeśli jest jego pierwszym znakiem albo występuje w reszcie słowa.

### Kod startowy

```python
def czy_elfickie(slowo, litery="elf"):
    pass


slowo = input().strip()
print("Prawda" if czy_elfickie(slowo) else "Fałsz")
```

*/

function czyElfickie(slowo, elf = "elf", idx = 0) {
  // Funkcja sprawdza czy słowo zawiera wszystkie litery z "elf"
  // Złożoność czasowa: O(n*m), gdzie n to długość słowa, m to liczba liter do znalezienia
  // Złożoność pamięciowa: O(m) dla rekurencji
  if (idx === elf.length) {
    return true;
  }
  // Sprawdź czy aktualna litera elf[idx] występuje w słowie
  if (slowo.indexOf(elf[idx]) === -1) {
    return false;
  }
  // Przejdź do sprawdzania następnej litery
  return czyElfickie(slowo, elf, idx + 1);
}

// Testy
function testCzyElfickie() {
  let slowo;
  let wynik;

  slowo = "reflektor";
  wynik = czyElfickie(slowo);
  console.assert(wynik === true, "Test 1 nieudany");

  slowo = "elefant";
  wynik = czyElfickie(slowo);
  console.assert(wynik === true, "Test 2 nieudany"); // "elefant" ma e, l, f

  slowo = "efektywnelekcje";
  wynik = czyElfickie(slowo);
  console.assert(wynik === true, "Test 3 nieudany");

  slowo = "wiolinistka";
  wynik = czyElfickie(slowo);
  console.assert(wynik === false, "Test 4 nieudany");
}

testCzyElfickie();
console.log("Wszystkie testy zakończone sukcesem");


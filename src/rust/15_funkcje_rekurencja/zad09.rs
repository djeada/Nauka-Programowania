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

fn zawiera(slowo: &[u8], litera: u8) -> bool {
    // Sprawdza rekurencyjnie, czy litera występuje w słowie.
    // Złożoność czasowa: O(n)
    // Złożoność pamięciowa: O(n) - przez stos rekurencji
    match slowo.split_first() {
        None => false,
        Some((&pierwsza, reszta)) => pierwsza == litera || zawiera(reszta, litera),
    }
}

fn czy_elfickie(slowo: &str, litery: &str) -> bool {
    // Sprawdza, czy każda litera z napisu litery występuje w słowie.
    // Złożoność czasowa: O(n * m), gdzie m to liczba liter do znalezienia
    // Złożoność pamięciowa: O(n + m) - przez stos rekurencji
    match litery.as_bytes().split_first() {
        None => true,
        Some((&litera, _)) => {
            zawiera(slowo.as_bytes(), litera) && czy_elfickie(slowo, &litery[1..])
        }
    }
}

fn test_czy_elfickie() {
    assert!(czy_elfickie("reflektor", "elf"));
    assert!(czy_elfickie("flet", "elf"));
    assert!(!czy_elfickie("elzbieta", "elf"));
    assert!(!czy_elfickie("a", "elf"));
}

fn main() {
    test_czy_elfickie();
}

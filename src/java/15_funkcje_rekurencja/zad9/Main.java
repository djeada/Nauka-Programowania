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

public class Main {

  // Zlozonosc Czasowa: O(n) gdzie n to dlugosc slowa
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static boolean zawiera(String slowo, char litera, int pozycja) {
    // Sprawdza, czy litera wystepuje w slowie od pozycji pozycja.
    if (pozycja >= slowo.length()) {
      return false;
    }

    if (slowo.charAt(pozycja) == litera) {
      return true;
    }

    return zawiera(slowo, litera, pozycja + 1);
  }

  public static boolean czySlowoElfickie(String slowo) {
    return czySlowoElfickie(slowo, "elf");
  }

  // Zlozonosc Czasowa: O(n * m) gdzie m to liczba liter do znalezienia
  // Zlozonosc Pamieciowa: O(n + m) - rekurencja uzywa stosu
  public static boolean czySlowoElfickie(String slowo, String litery) {
    // Sprawdza, czy kazda litera z napisu litery wystepuje w slowie.
    if (litery.isEmpty()) {
      return true;
    }

    if (!zawiera(slowo, litery.charAt(0), 0)) {
      return false;
    }

    return czySlowoElfickie(slowo, litery.substring(1));
  }

  public static void test1() {
    assert czySlowoElfickie("reflektor");
    assert czySlowoElfickie("flet");
  }

  public static void test2() {
    assert !czySlowoElfickie("elzbieta");
    assert !czySlowoElfickie("a");
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

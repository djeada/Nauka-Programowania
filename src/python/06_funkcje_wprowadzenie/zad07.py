r"""
ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — wczytuje nazwę użytkownika (login) i hasło, po czym zwraca je jako parę `(login, haslo)`.
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje kolejne próby logowania (login i hasło), dopóki nie będą identyczne z przekazanymi danymi.
   Po każdej nieudanej próbie wypisuje `Błędne dane. Spróbuj ponownie.`, a po udanej — `Dane poprawne. Dostęp przyznany.` i kończy działanie.

Program najpierw wywołuje `pobierz_dane()`, aby ustalić poprawne dane, a potem przekazuje je do `sprawdz_dane(...)`.

W tym zadaniu funkcje same wczytują dane (`input()`), a `sprawdz_dane` sama wypisuje komunikaty.

### Wejście

* 1. linia: poprawny login
* 2. linia: poprawne hasło
* kolejne linie: próby logowania — po dwie linie na próbę (login, potem hasło)

### Wyjście

Dla każdej nieudanej próby linia:

```
Błędne dane. Spróbuj ponownie.
```

a na końcu (po pierwszej udanej próbie) linia:

```
Dane poprawne. Dostęp przyznany.
```

### Ograniczenia

* Jedna z prób jest poprawna — program nie musi obsługiwać końca danych bez udanej próby.

### Przykład

**Wejście:**

```
admin
1234
root
pass
admin
1234
```

**Wyjście:**

```
Błędne dane. Spróbuj ponownie.
Dane poprawne. Dostęp przyznany.
```

Poprawne dane to `admin` / `1234`. Pierwsza próba (`root` / `pass`) jest błędna, druga — poprawna.

### Uwagi

* Próba jest udana tylko wtedy, gdy zgadzają się **oba** pola: login i hasło.
* Porównanie uwzględnia wielkość liter (`Admin` to nie to samo co `admin`).

### Kod startowy

```python
def pobierz_dane():
    pass


def sprawdz_dane(poprawny_login, poprawne_haslo):
    pass


login, haslo = pobierz_dane()
sprawdz_dane(login, haslo)
```

"""


def pobierz_dane():
    """Wczytuje login i hasło, zwraca je jako parę."""
    login = input()
    haslo = input()
    return login, haslo


def sprawdz_dane(poprawny_login, poprawne_haslo):
    """Wczytuje kolejne próby logowania, dopóki dane nie będą poprawne."""
    login, haslo = pobierz_dane()
    while login != poprawny_login or haslo != poprawne_haslo:
        print("Błędne dane. Spróbuj ponownie.")
        login, haslo = pobierz_dane()
    print("Dane poprawne. Dostęp przyznany.")


if __name__ == "__main__":
    login, haslo = pobierz_dane()
    sprawdz_dane(login, haslo)

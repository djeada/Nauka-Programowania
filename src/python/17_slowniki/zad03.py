r"""
ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Prowadź bazę wypożyczeń biblioteki jako słownik `imię → lista wypożyczonych tytułów`. Wczytuj komendy (każda w osobnej linii), aż do komendy `koniec`:

* `dodaj IMIĘ TYTUŁ` — czytelnik `IMIĘ` wypożycza książkę `TYTUŁ` (dopisz ją na koniec jego listy),
* `zwróć IMIĘ TYTUŁ` — czytelnik oddaje książkę (usuń ją z jego listy; jeśli jej tam nie ma, nic się nie dzieje),
* `lista IMIĘ` — wypisz książki wypożyczone przez czytelnika.

Po komendzie `lista IMIĘ` wypisz jedną linię:

* `Książki wypożyczone przez IMIĘ: t1, t2, …` — tytuły w kolejności wypożyczenia, oddzielone przecinkiem i spacją,
* `Książki wypożyczone przez IMIĘ: brak` — jeśli czytelnik nie ma żadnej książki albo nie występuje w bazie.

### Wejście

Kolejne linie z komendami; ostatnia linia to `koniec`.

* `IMIĘ` to jedno słowo (bez spacji).
* `TYTUŁ` to cała reszta linii po imieniu — może zawierać spacje (bez cudzysłowów).

### Wyjście

Po jednej linii dla każdej komendy `lista`; pozostałe komendy niczego nie wypisują.

### Ograniczenia

* co najwyżej 100 komend

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna Duma i uprzedzenie
dodaj Jan Władca Pierścieni
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

### Uwagi

* Linię komendy rozbij na co najwyżej trzy części: `linia.split(maxsplit=2)`.
* Czytelnik może wypożyczyć kilka egzemplarzy tego samego tytułu — wtedy tytuł występuje na liście kilka razy, a `zwróć` usuwa tylko jeden egzemplarz (pierwsze wystąpienie).

"""


def dodaj(baza, czytelnik, tytul):
    """Zapisuje wypożyczenie książki przez czytelnika."""
    if czytelnik not in baza:
        baza[czytelnik] = []
    baza[czytelnik].append(tytul)


def zwroc(baza, czytelnik, tytul):
    """Usuwa jeden egzemplarz książki z listy czytelnika (jeśli go ma)."""
    if czytelnik in baza and tytul in baza[czytelnik]:
        baza[czytelnik].remove(tytul)


def opis_wypozyczen(baza, czytelnik):
    ksiazki = baza.get(czytelnik, [])
    if ksiazki:
        lista = ", ".join(ksiazki)
    else:
        lista = "brak"
    return f"Książki wypożyczone przez {czytelnik}: {lista}"


if __name__ == "__main__":
    baza = {}
    while True:
        linia = input().strip()
        if linia == "koniec":
            break
        czesci = linia.split(maxsplit=2)
        komenda = czesci[0]
        if komenda == "dodaj":
            dodaj(baza, czesci[1], czesci[2])
        elif komenda == "zwróć":
            zwroc(baza, czesci[1], czesci[2])
        elif komenda == "lista":
            print(opis_wypozyczen(baza, czesci[1]))

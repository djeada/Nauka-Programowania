{-
ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

\**Poziom:** ★★☆
\**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

\* **Zwierz** — metoda `odglos()` zwraca/drukuje ogólny dźwięk.
\* **Pies** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
\* **Kot** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.

Program testowy:

\* tworzy obiekty: `Zwierz`, `Pies`, `Kot`,
\* umieszcza je w jednej kolekcji,
\* iteruje i dla każdego wypisuje linię w formacie:
  `NazwaKlasy wydaje odgłos: ...`

### Wejście

Brak.

### Wyjście

Trzy linie, po jednej dla każdego obiektu.

### Przykład

\**Wyjście:**

```
Zwierz wydaje odgłos: ...
Pies wydaje odgłos: Hau!
Kot wydaje odgłos: Miau!
```

-}
main :: IO ()
main = pure ()

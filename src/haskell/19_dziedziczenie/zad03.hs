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

-- Type class dla zwierząt
-- Złożoność pamięciowa: O(1)
class Zwierz a where
    odglos :: a -> String
    nazwaKlasy :: a -> String

data ZwierzOgolny = ZwierzOgolny
data Pies = Pies
data Kot = Kot

instance Zwierz ZwierzOgolny where
    odglos _ = "jakiś dźwięk"
    nazwaKlasy _ = "Zwierz"

instance Zwierz Pies where
    odglos _ = "Hau hau!"
    nazwaKlasy _ = "Pies"

instance Zwierz Kot where
    odglos _ = "Miau!"
    nazwaKlasy _ = "Kot"

wypiszOdglos :: Zwierz a => a -> IO ()
wypiszOdglos z = putStrLn $ nazwaKlasy z ++ " wydaje odgłos: " ++ odglos z

main :: IO ()
main = do
    wypiszOdglos ZwierzOgolny
    wypiszOdglos Pies
    wypiszOdglos Kot

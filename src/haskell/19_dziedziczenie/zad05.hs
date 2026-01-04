{-
ZAD-05 — Dziedziczenie wielokrotne: Ptak

\**Poziom:** ★★☆
\**Tagi:** `multiple inheritance`, `dziedziczenie`, `metody`

### Treść

Zaprojektuj klasy:

\* **Zwierz** — metody:

  * `jedz()` → wypisuje `Ptak je.`
  * `spij()` → wypisuje `Ptak śpi.`
  * `wydaj_dzwiek()` → wypisuje `Ptak wydaje dźwięk.`

\* **ObiektLatajacy** — metody:

  * `lec()` → wypisuje `Ptak leci.`
  * `wyladuj()` → wypisuje `Ptak ląduje.`

\* **Ptak** — dziedziczy po `Zwierz` oraz `ObiektLatajacy`.

Program testowy:

\* tworzy obiekt `Ptak`,
\* wywołuje metody w kolejności: `jedz`, `spij`, `wydaj_dzwiek`, `lec`, `wyladuj`.

### Wejście

Brak.

### Wyjście

Pięć linii jak w przykładzie.

### Przykład

\**Wyjście:**

```
Ptak je.
Ptak śpi.
Ptak wydaje dźwięk.
Ptak leci.
Ptak ląduje.
```

-}

class Zwierz a where
  jedz :: a -> IO ()
  spij :: a -> IO ()
  wydajDzwiek :: a -> IO ()

class ObiektLatajacy a where
  lec :: a -> IO ()
  wyladuj :: a -> IO ()

data Ptak = Ptak

instance Zwierz Ptak where
  jedz _ = putStrLn "Ptak je."
  spij _ = putStrLn "Ptak śpi."
  wydajDzwiek _ = putStrLn "Ptak wydaje dźwięk."

instance ObiektLatajacy Ptak where
  lec _ = putStrLn "Ptak leci."
  wyladuj _ = putStrLn "Ptak ląduje."

main :: IO ()
main = do
  let ptak = Ptak
  jedz ptak
  wydajDzwiek ptak
  lec ptak
  wyladuj ptak
  spij ptak

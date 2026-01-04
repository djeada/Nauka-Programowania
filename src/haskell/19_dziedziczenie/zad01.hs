{-
ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

\**Poziom:** ★☆☆
\**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. **Bazowa** — posiada metodę `przedstaw_sie()`, która wypisuje komunikat o klasie bazowej.
2. **Potomna** — dziedziczy po **Bazowej** i **nadpisuje** metodę `przedstaw_sie()`, ale w swojej implementacji:

   * najpierw **wywołuje** wersję metody z klasy bazowej,
   * potem dopisuje własny komunikat.

Program testowy:

\* tworzy obiekt klasy potomnej,
\* wywołuje metodę `przedstaw_sie()`.

### Wejście

Brak.

### Wyjście

Dwie linie, pokazujące najpierw komunikat klasy bazowej, a potem potomnej.

### Przykład

\**Wyjście:**

```
Jestem klasą bazową.
A ja jestem klasą potomną.
```

-}

class Bazowa a where
  przedstawSie :: a -> IO ()

data KlasaBazowa = KlasaBazowa

instance Bazowa KlasaBazowa where
  przedstawSie _ = putStrLn "Jestem klasą bazową."

data KlasaPotomna = KlasaPotomna

instance Bazowa KlasaPotomna where
  przedstawSie _ = do
    przedstawSie KlasaBazowa -- Wywołanie metody z klasy bazowej
    putStrLn "A ja jestem klasą potomną."

main :: IO ()
main = do
  let obj = KlasaPotomna
  przedstawSie obj

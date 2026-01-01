{-
ZAD-02 — Sprawdź poprawność hasła

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia wszystkie warunki:

1. Zawiera co najmniej jedną małą literę `[a–z]`.
2. Zawiera co najmniej jedną wielką literę `[A–Z]`.
3. Zawiera co najmniej jedną cyfrę `[0–9]`.
4. Zawiera co najmniej jeden znak specjalny spośród:
   `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
5. Ma długość co najmniej 8 znaków.
6. Ma długość nie większą niż 20 znaków.

### Wejście

Jedna linia:

\* `haslo`

### Wyjście

Jedna linia:

\* `Prawda` albo `Fałsz`

### Przykład

\**Wejście:**

```
abc1234
```

\**Wyjście:**

```
Fałsz
```

-}
main :: IO ()
main = pure ()

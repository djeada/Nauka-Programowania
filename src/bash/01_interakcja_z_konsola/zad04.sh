# ZAD-04 — Podstawowe operacje arytmetyczne
#
# **Poziom:** ★☆☆
# **Tagi:** `arytmetyka`, `I/O`
#
# ### Treść
#
# Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:
#
# 1. `a + b`
# 2. `a - b`
# 3. `a * b`
# 4. `a // b` (dzielenie całkowite)
# 5. `a % b`
# 6. `a^b`
#
# ### Wejście
#
# * 1. linia: `a` (liczba całkowita)
# * 2. linia: `b` (liczba całkowita)
#
# ### Wyjście
#
# 6 linii — wyniki działań w kolejności 1–6.
#
# ### Ograniczenia / gwarancje
#
# * `a ≥ 0`
# * `b > 0` (żeby dzielenie i modulo były poprawne)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 2
# ```
#
# **Wyjście:**
#
# ```
# 5
# 1
# 6
# 1
# 1
# 9
# ```

main() {

    echo "Podaj dwie liczby."
    read a
    read b

    echo "Suma pobranych liczb: $(($a + $b))"
    echo "Roznica pobranych liczb: $(($a - $b))"
    echo "Iloczyn pobranych liczb: $(($a * $b))"
    echo "Iloraz pierwszej przez druga: $(($a / $b))"
    echo "Reszta z dzielenia pierwszej przez druga: $(($a % $b))"
    echo "Pierwsza podniesiona do potegi rownej drugiej: $(($a ** $b))"

}

main "$@"

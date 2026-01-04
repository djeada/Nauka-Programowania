# ZAD-05 — Litera „X”
#
# **Poziom:** ★★☆
# **Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`
#
# ### Treść
#
# Wczytaj `n` (`n ≥ 3`) i wypisz literę `X` o wysokości `n`, zbudowaną z `*` na obu przekątnych.
#
# W wierszu `i` i kolumnie `j` (indeksy od 0):
#
# * wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`,
# * w przeciwnym razie wypisz spację.
#
# ### Wejście
#
# * 1. linia: `n` (`n ≥ 3`)
#
# ### Wyjście
#
# `n` linii po `n` znaków (`*` lub spacja).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# ```
#
# **Wyjście:**
#
# ```
# *   *
#  * *
#   *
#  * *
# *   *
# ```
main() {
    read n
    # Górna połowa (wraz ze środkiem)
    for ((i = 0; i < n; i++)); do
        # Spacje na początku
        for ((j = 0; j < n - i - 1; j++)); do
            echo -n " "
        done
        # Gwiazdki i spacje wewnętrzne
        for ((j = 0; j < 2 * i + 1; j++)); do
            if [[ $j -eq 0 || $j -eq $((2 * i)) ]]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done
    # Dolna połowa
    for ((i = n - 2; i >= 0; i--)); do
        for ((j = 0; j < n - i - 1; j++)); do
            echo -n " "
        done
        for ((j = 0; j < 2 * i + 1; j++)); do
            if [[ $j -eq 0 || $j -eq $((2 * i)) ]]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done
}
main "$@"

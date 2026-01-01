# ZAD-03 — Określanie znaku liczby
#
# **Poziom:** ★☆☆
# **Tagi:** `if-elif-else`, `porównania`, `string`
#
# ### Treść
#
# Wczytaj liczbę całkowitą `x` i wypisz jeden z komunikatów:
#
# * dla `x < 0`: `Liczba jest ujemna.`
# * dla `x > 0`: `Liczba jest dodatnia.`
# * dla `x = 0`: `Liczba jest zerem.`
#
# ### Wejście
#
# * 1 linia: `x` (liczba całkowita)
#
# ### Wyjście
#
# Jedna linia — dokładnie jeden komunikat.
#
# ### Przykłady
#
# **Wejście:**
#
# ```
# -5
# ```
#
# **Wyjście:**
#
# ```
# Liczba jest ujemna.
# ```
#
# **Wejście:**
#
# ```
# 0
# ```
#
# **Wyjście:**
#
# ```
# Liczba jest zerem.
# ```
#
# **Wejście:**
#
# ```
# 2
# ```
#
# **Wyjście:**
#
# ```
# Liczba jest dodatnia.
# ```

main() {
    read x

    if [[ $x -gt 0 ]]; then
        echo "Liczba jest dodatnia."
    elif [[ $x -lt 0 ]]; then
        echo "Liczba jest ujemna."
    else
        echo "Liczba jest zerem."
    fi
}

main "$@"

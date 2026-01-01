# ZAD-05C — Funkcja sześcienna: y = x³ + 2
#
# **Poziom:** ★★☆
# **Tagi:** `potęgi`, `float`
#
# ### Treść
#
# Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.
#
# ### Wejście
#
# 1 liczba: `x`
#
# ### Wyjście
#
# `y` do 3 miejsc po przecinku.
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
# 127.000
# ```

main() {
    read x
    result=$(echo "scale=3; $x^3 + 2" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

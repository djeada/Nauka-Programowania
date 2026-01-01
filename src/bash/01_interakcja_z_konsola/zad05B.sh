# ZAD-05B — Funkcja liniowa: y = ax + b
#
# **Poziom:** ★★☆
# **Tagi:** `arytmetyka`, `float`
#
# ### Wejście
#
# 3 liczby (każda w osobnej linii): `a`, `b`, `x`
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
# 1
# 2
# 3
# ```
#
# **Wyjście:**
#
# ```
# 5.000
# ```

main() {
    read a
    read b
    read x
    result=$(echo "scale=3; $a * $x + $b" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

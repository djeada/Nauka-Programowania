# ZAD-07B — Pole prostokąta
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz pole prostokąta:
# ( P = ab )
#
# ### Wejście
#
# * 1 linia: `a`
# * 2 linia: `b`
#
# ### Wyjście
#
# * 1 linia: `P` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2.5
# 4
# ```
#
# **Wyjście:**
#
# ```
# 10.000
# ```

main() {
    read a
    read b
    result=$(echo "scale=3; $a * $b" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

# ZAD-07F — Objętość prostopadłościanu
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz objętość prostopadłościanu:
# ( V = abc )
#
# ### Wejście
#
# * 1 linia: `a`
# * 2 linia: `b`
# * 3 linia: `c`
#
# ### Wyjście
#
# * 1 linia: `V` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 3
# 4
# ```
#
# **Wyjście:**
#
# ```
# 24.000
# ```

main() {
    read a
    read b
    read c
    result=$(echo "scale=3; $a * $b * $c" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

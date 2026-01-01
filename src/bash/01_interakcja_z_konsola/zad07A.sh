# ZAD-07A — Pole trójkąta
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz pole trójkąta ze wzoru:
# ( P = \frac{1}{2} a h )
#
# ### Wejście
#
# * 1 linia: `a`
# * 2 linia: `h`
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
# 6
# 4
# ```
#
# **Wyjście:**
#
# ```
# 12.000
# ```

main() {
    read a
    read h
    result=$(echo "scale=3; 0.5 * $a * $h" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

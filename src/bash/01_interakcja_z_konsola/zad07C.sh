# ZAD-07C — Pole rombu
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz pole rombu z przekątnych:
# ( P = \frac{1}{2} d_1 d_2 )
#
# ### Wejście
#
# * 1 linia: `d1`
# * 2 linia: `d2`
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
# 10
# 6
# ```
#
# **Wyjście:**
#
# ```
# 30.000
# ```

main() {
    read d1
    read d2
    result=$(echo "scale=3; 0.5 * $d1 * $d2" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

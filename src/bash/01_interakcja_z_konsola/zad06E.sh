# ZAD-06E — Stopnie → radiany
#
# **Poziom:** ★☆☆
# **Tagi:** `pi`, `float`
#
# ### Treść
#
# Wczytaj kąt w stopniach `deg` i przelicz na radiany.
#
# ### Wejście
#
# * 1 linia: `deg`
#
# ### Wyjście
#
# * 1 linia: `rad = deg * π / 180` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 180
# ```
#
# **Wyjście:**
#
# ```
# 3.142
# ```

main() {
    read deg
    result=$(echo "scale=10; $deg * 3.141592653589793 / 180" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

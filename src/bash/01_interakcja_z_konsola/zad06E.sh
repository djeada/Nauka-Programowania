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
    # Use bc's arctangent to compute pi: pi = 4 * atan(1)
    result=$(echo "scale=10; pi = 4 * a(1); $deg * pi / 180" | bc -l)
    printf "%.3f\n" "$result"
}

main "$@"

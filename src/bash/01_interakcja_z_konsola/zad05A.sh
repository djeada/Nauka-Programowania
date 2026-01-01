# ZAD-05A — Funkcja liniowa: y = 3x + 10
#
# **Poziom:** ★★☆
# **Tagi:** `arytmetyka`, `float`, `formatowanie`
#
# ### Wejście
#
# 1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)
#
# ### Wyjście
#
# 1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# ```
#
# **Wyjście:**
#
# ```
# 19.000
# ```

main() {
    read x
    result=$(echo "scale=3; 3 * $x + 10" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

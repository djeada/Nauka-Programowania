# ZAD-07D — Objętość kuli
#
# **Poziom:** ★★☆
# **Tagi:** `geometria`, `pi`, `float`
#
# ### Treść
#
# Oblicz objętość kuli:
# ( V = \frac{4}{3}\pi r^3 )
#
# ### Wejście
#
# * 1 linia: `r`
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
# 1
# ```
#
# **Wyjście:**
#
# ```
# 4.189
# ```

main() {
    read r
    # Use bc's arctangent to compute pi: pi = 4 * atan(1)
    result=$(echo "scale=10; pi = 4 * a(1); (4.0/3.0) * pi * $r^3" | bc -l)
    printf "%.3f\n" "$result"
}

main "$@"

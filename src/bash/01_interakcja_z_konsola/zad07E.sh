# ZAD-07E — Objętość stożka
#
# **Poziom:** ★★☆
# **Tagi:** `geometria`, `pi`, `float`
#
# ### Treść
#
# Oblicz objętość stożka:
# ( V = \frac{1}{3}\pi r^2 h )
#
# ### Wejście
#
# * 1 linia: `r`
# * 2 linia: `h`
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
# ```
#
# **Wyjście:**
#
# ```
# 12.566
# ```

main() {
    read r
    read h
    # Use bc's arctangent to compute pi: pi = 4 * atan(1)
    result=$(echo "scale=10; pi = 4 * a(1); (1.0/3.0) * pi * $r^2 * $h" | bc -l)
    printf "%.3f\n" "$result"
}

main "$@"

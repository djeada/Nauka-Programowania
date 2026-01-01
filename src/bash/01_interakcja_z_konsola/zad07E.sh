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
    result=$(echo "scale=10; (1.0/3.0) * 3.141592653589793 * $r^2 * $h" | bc)
    printf "%.3f\n" "$result"
}

main "$@"

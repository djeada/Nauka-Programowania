# ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem
#
# **Poziom:** ★★★☆
# **Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`
#
# ### Treść
#
# Dla `x` (w radianach) oblicz:
# [
# y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
# ]
#
# ### Wejście
#
# 1 liczba zmiennoprzecinkowa: `x` (w radianach)
#
# ### Wyjście
#
# `y` do 3 miejsc po przecinku.
#
# ### Ograniczenia / gwarancje
#
# * Dane testowe spełniają warunek dziedziny logarytmu:
#
#   * (x^3+2x^2-x-3 > 0)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# ```
#
# **Wyjście:**
#
# ```
# 57.179
# ```

main() {
    read x
    result=$(echo "scale=10; s_x=s($x); c_x=c($x); sin3=s_x*s_x*s_x; cos2=c_x*c_x; exp_part=e($x*$x); ln_arg=$x^3 + 2*$x^2 - $x - 3; ln_part=l(ln_arg); sin3*cos2 + exp_part + ln_part" | bc -l)
    printf "%.3f\n" "$result"
}

main "$@"

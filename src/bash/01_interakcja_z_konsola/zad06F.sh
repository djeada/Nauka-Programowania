# ZAD-06F — Fahrenheit → Celsius i Kelviny
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`, `float`
#
# ### Treść
#
# Wczytaj temperaturę w stopniach Fahrenheita `F`. Oblicz temperaturę w Celsjuszach oraz Kelvinach.
#
# ### Wejście
#
# * 1 linia: `F`
#
# ### Wyjście
#
# Dwie linie:
#
# 1. `C = (5/9) * (F - 32)` do **3 miejsc**
# 2. `K = C + 273.15` do **3 miejsc**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 32
# ```
#
# **Wyjście:**
#
# ```
# 0.000
# 273.150
# ```

main() {
    read F
    C=$(echo "scale=10; (5.0/9.0) * ($F - 32)" | bc)
    printf "%.3f\n" "$C"
    K=$(echo "scale=10; $C + 273.15" | bc)
    printf "%.3f\n" "$K"
}

main "$@"

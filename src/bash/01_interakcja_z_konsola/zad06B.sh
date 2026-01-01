# ZAD-06B — Cale → centymetry
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`, `float`
#
# ### Treść
#
# Wczytaj liczbę cali `inch` i przelicz na centymetry.
#
# ### Wejście
#
# * 1 linia: `inch`
#
# ### Wyjście
#
# * 1 linia: `cm = inch * 2.54` wypisane do **2 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 10
# ```
#
# **Wyjście:**
#
# ```
# 25.40
# ```

main() {
    read inch
    result=$(echo "scale=2; $inch * 2.54" | bc)
    printf "%.2f\n" "$result"
}

main "$@"

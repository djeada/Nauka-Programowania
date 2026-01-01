# ZAD-06D — Euro → złotówki (kurs stały)
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`, `float`
#
# ### Treść
#
# Wczytaj kwotę w euro `eur` i przelicz na złotówki przy stałym kursie.
#
# ### Wejście
#
# * 1 linia: `eur`
#
# ### Wyjście
#
# * 1 linia: `pln = eur * 4.4` do **2 miejsc po przecinku**
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
# 13.20
# ```

main() {
    read eur
    result=$(echo "scale=2; $eur * 4.4" | bc)
    printf "%.2f\n" "$result"
}

main "$@"

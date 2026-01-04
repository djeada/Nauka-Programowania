# ZAD-05 — Sortowanie trzech liczb
#
# **Poziom:** ★★☆
# **Tagi:** `sort`, `warunki`, `porządkowanie`
#
# ### Treść
#
# Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.
#
# ### Wejście
#
# * 1 linia: `a` (całkowita, `a ≥ 0`)
# * 2 linia: `b` (całkowita, `b ≥ 0`)
# * 3 linia: `c` (całkowita, `c ≥ 0`)
#
# ### Wyjście
#
# Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 1
# 4
# ```
#
# **Wyjście:**
#
# ```
# 1 2 4
# ```
#
# ### Uwagi
#
# * Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.
main() {
    read a
    read b
    read c

    # Sortuj trzy liczby używając warunków
    if [[ $a -le $b && $a -le $c ]]; then
        if [[ $b -le $c ]]; then
            echo "$a $b $c"
        else
            echo "$a $c $b"
        fi
    elif [[ $b -le $a && $b -le $c ]]; then
        if [[ $a -le $c ]]; then
            echo "$b $a $c"
        else
            echo "$b $c $a"
        fi
    else
        if [[ $a -le $b ]]; then
            echo "$c $a $b"
        else
            echo "$c $b $a"
        fi
    fi
}

main "$@"

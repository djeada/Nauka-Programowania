# ZAD-06 — Maksimum z czterech liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `max`, `if`, `porównania`
#
# ### Treść
#
# Wczytaj cztery liczby naturalne i wypisz największą z nich.
#
# ### Wejście
#
# 4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)
#
# ### Wyjście
#
# Jedna linia: największa liczba.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 5
# 1
# 4
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```
main() {
    read a
    read b
    read c
    read d

    # Znajdź maksimum z czterech liczb
    max=$a
    if [[ $b -gt $max ]]; then
        max=$b
    fi
    if [[ $c -gt $max ]]; then
        max=$c
    fi
    if [[ $d -gt $max ]]; then
        max=$d
    fi

    echo $max
}

main "$@"

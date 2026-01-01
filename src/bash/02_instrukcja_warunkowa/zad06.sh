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

    echo "Podaj cztery liczby."
    read a
    read b
    read c
    read d

    maxAB=$([ $a -gt $b ] && echo "$a" || echo "$b")
    maxCD=$([ $c -gt $d ] && echo "$c" || echo "$d")
    max=$([ $maxAB -gt $maxCD ] && echo "$maxAB" || echo "$maxCD")

    echo $max
}

main "$@"

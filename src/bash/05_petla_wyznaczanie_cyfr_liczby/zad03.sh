# ZAD-03 — Sumowanie cyfr liczby
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `modulo`, `dzielenie całkowite`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Jedna liczba naturalna — suma cyfr liczby `n`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 129
# ```
#
# **Wyjście:**
#
# ```
# 12
# ```
#
# ### Uwagi o formatowaniu
#
# * Dla `n = 0` suma cyfr wynosi `0`.
main() {
    read a

    suma=0

    # Przypadek specjalny: n = 0
    if [[ $a -eq 0 ]]; then
        echo "0"
        return
    fi

    while [ $a -gt 0 ]; do
        suma=$(($suma + $a % 10))
        a=$(($a / 10))
    done

    echo "$suma"
}

main "$@"

# ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `modulo`, `dzielenie całkowite`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n` i wypisz jej cyfry w kolejności od cyfry jedności (czyli w odwrotnej kolejności niż w zapisie liczby). Każdą cyfrę wypisz w osobnej linii.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Kolejne cyfry `n` w odwrotnej kolejności, każda w nowej linii.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 8214
# ```
#
# **Wyjście:**
#
# ```
# 4
# 1
# 2
# 8
# ```
#
# ### Uwagi o formatowaniu
#
# * Dla `n = 0` wypisz jedną linię z `0`.
main() {
    read a

    # Przypadek specjalny: n = 0
    if [[ $a -eq 0 ]]; then
        echo "0"
        return
    fi

    while [ $a -gt 0 ]; do
        echo $(($a % 10))
        a=$(($a / 10))
    done
}

main "$@"

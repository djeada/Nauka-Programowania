# ZAD-01 — Liczenie cyfr w liczbie
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `modulo`, `dzielenie całkowite`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Jedna liczba naturalna — liczba cyfr w `n`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 342
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```
#
# ### Ograniczenia / gwarancje
#
# * `n` mieści się w typowym zakresie liczb całkowitych.
#
# ### Uwagi o formatowaniu
#
# * Dla `n = 0` poprawna odpowiedź to `1` (liczba „0” ma jedną cyfrę).

main() {
    read a

    # Przypadek specjalny: n = 0 ma jedną cyfrę
    if [[ $a -eq 0 ]]; then
        echo "1"
        return
    fi

    licznik=0

    while [ $a -gt 0 ]; do
        a=$(($a / 10))
        licznik=$(($licznik + 1))
    done

    echo "$licznik"
}

main "$@"

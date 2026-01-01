# ZAD-06 — Suma cyfr liczby (funkcja)
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `pętle`, `modulo`
#
# ### Treść
#
# Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.
#
# ### Wejście
#
# Jeden argument: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Funkcja zwraca sumę cyfr.
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(suma_cyfr(13231))
# ```
#
# **Wyjście:**
#
# ```
# 10
# ```
#
# ### Uwagi
#
# * Dla `n = 0` suma cyfr to `0`.

sumaCyfr() {

    a=$1
    suma=0

    while [ $a -gt 0 ]; do
        suma=$(($suma + $a % 10))
        a=$(($a / 10))
    done

    return $suma
}

main() {
    read a

    sumaCyfr $a
    wynik=$?


}

main "$@"

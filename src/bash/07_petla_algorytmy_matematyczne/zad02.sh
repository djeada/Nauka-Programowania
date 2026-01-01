# ZAD-02 — Potęgowanie liczby przy pomocy pętli
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `potęgowanie`, `mnożenie`
#
# ### Treść
#
# Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez operatora potęgowania).
#
# ### Wejście
#
# Dwa argumenty funkcji:
#
# * `a` (liczba naturalna, `a ≥ 0`)
# * `b` (liczba naturalna, `b ≥ 0`)
#
# ### Wyjście
#
# Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(potega(3, 5))
# ```
#
# **Wyjście:**
#
# ```
# 243
# ```
#
# ### Uwagi o formatowaniu
#
# * Dla `b = 0` wynik ma wynosić `1`.

source ../assert.sh

potega() {

    a=$1
    b=$2
    wynik=1

    for ((i = 0; i < $b; i++)); do
        wynik=$(($wynik * $a))
    done

    echo $wynik
}

main() {
    a=2
    b=3
    wynik=8
    assert "$wynik -eq $(potega $a $b)" $LINENO
}

main "$@"

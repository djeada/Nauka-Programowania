# ZAD-08 — Iloraz w dół bez / i %
#
# **Poziom:** ★★☆
# **Tagi:** `funkcje`, `pętle`, `odejmowanie`
#
# ### Treść
#
# Napisz funkcję `zaokraglij_w_dol(a, b)`, która zwraca wartość `a // b`, ale **nie używa** operatorów `/` ani `%`.
#
# ### Wejście
#
# Dwa argumenty:
#
# * `a` (liczba naturalna, `a ≥ 0`)
# * `b` (liczba naturalna)
#
# ### Ograniczenia / gwarancje
#
# * `b > 0`
#
# ### Wyjście
#
# Funkcja zwraca liczbę naturalną — iloraz `a` przez `b` zaokrąglony w dół.
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(zaokraglij_w_dol(7, 2))
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```

podziel() {
    a=$1
    b=$2
    znak=1

    if [[ $b -eq 0 ]]; then
        echo "Error!"
        return
    fi

    if [[ $a -eq 0 ]]; then
        return 0
    fi

    if [[ $a -lt $b ]]; then
        znak=-1
        a=$(($a * -1))
    fi

    if [[ $b -lt 0 ]]; then
        znak=$(($znak * -1))
        b=$(($b * -1))
    fi

    if [[ $znak -eq 1 ]]; then
        licznik=0
        while [[ $a -ge $b ]]; do
            a=$(($a - $b))
            licznik=$(($licznik + 1))
        done
    else
        licznik=1
        while [[ $a -gt $b ]]; do
            a=$(($a - $b))
            licznik=$(($licznik + 1))
        done
    fi

    wynik=$(($licznik * $znak))

    return $wynik
}

main() {
    read a
    read b

    podziel $a $b
    wynik=$?

}

main "$@"

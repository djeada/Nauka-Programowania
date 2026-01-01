# ZAD-14 — Element bez pary
#
# **Poziom:** ★★☆
# **Tagi:** `XOR`, `listy`, `zliczanie`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.
#
# ### Wejście
#
# * 1. linia: `N` (nieparzyste, `N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
#
# ### Wyjście
#
# Jedna liczba całkowita — element bez pary.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 7
# 1
# 3
# 1
# 7
# 3
# 1
# 1
# ```
#
# **Wyjście:**
#
# ```
# 7
# ```

source ../assert.sh

element_bez_pary() {
    wynik=0

    for liczba in "${lista[@]}"; do
        wynik=$((wynik ^ liczba))
    done

    return $wynik
}

test1() {
    local lista=(1 3 1 7 3 1 1)
    local wynik=7
    element_bez_pary
    assertEqual "$?" "$wynik" $LINENO
}

test2() {
    local lista=(2 2 3 3 5 5 4)
    local wynik=4
    element_bez_pary
    assertEqual "$?" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

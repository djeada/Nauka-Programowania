# ZAD-18 — Indeks najmniejszego elementu w przesuniętej liście
#
# **Poziom:** ★★☆
# **Tagi:** `binarne`, `rotacja`, `minimum`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych, która była posortowana rosnąco i została przesunięta w prawo o nieznaną liczbę miejsc. Znajdź indeks najmniejszego elementu.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
#
# ### Wyjście
#
# Jedna liczba całkowita — indeks najmniejszego elementu (od `0`).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 7
# 8
# -1
# 4
# 5
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
source ../assert.sh

suma_dwoch() {
    local n=$((${#lista[@]} - 1))

    for ((i = 0; i < n; i++)); do
        if [ ${lista[$i]} -gt ${lista[$i + 1]} ]; then
            return $((i + 1))
        fi
    done

    return 0
}

test1() {
    local lista=(7 8 -1 4 5)
    local wynik=2
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

test2() {
    local lista=(2 3 4 5 6)
    local wynik=0
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

test3() {
    local lista=(8 9 10 11 1)
    local wynik=4
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

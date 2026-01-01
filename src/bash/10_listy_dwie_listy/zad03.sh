# ZAD-03 — Suma elementów dwóch list
#
# **Poziom:** ★☆☆
# **Tagi:** `list`, `iteracja`
#
# ### Treść
#
# Wczytaj dwie listy liczb całkowitych i zwróć listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
# Jeśli któraś lista jest krótsza, brakujące elementy traktuj jako `0`.
#
# ### Wejście
#
# * 1 linia: lista 1
# * 2 linia: lista 2
#
# ### Wyjście
#
# * 1 linia: lista sum
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [3, 1, 2, 5]
# [2, 8, 6, 5]
# ```
#
# **Wyjście:**
#
# ```
# [5, 9, 8, 10]
# ```

source ../assert.sh

suma() {

    local n=$((${#lista_a[@]}))
    local m=$((${#lista_b[@]}))
    local min_dlugosc=$((n < m ? n : m))
    wynik=("${lista_a[@]}")

    for ((i = 0; i < min_dlugosc; i++)); do
        wynik[$i]=$((wynik[i] + lista_b[i]))
    done

    for ((i = min_dlugosc; i < m; i++)); do
        wynik+=("{lista_b[$i]}")
    done

}

test1() {
    local lista_a=(3 1 2 5)
    local lista_b=(2 8 6 5)
    local oczekiwane=(5 9 8 10)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

test2() {
    local lista_a=(3 1 2 5)
    local lista_b=(2 8)
    local oczekiwane=(5 9 2 5)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

test3() {
    local lista_a=(3 1 0 0)
    local lista_b=(2 8 6 5)
    local oczekiwane=(5 9 6 5)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

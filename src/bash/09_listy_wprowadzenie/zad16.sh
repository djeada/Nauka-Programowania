# ZAD-16 — Indeksy pierwszej pary o sumie x
#
# **Poziom:** ★★☆
# **Tagi:** `hashmap`, `indeksy`, `2-sum`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej** pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.
#
# Jeśli nie istnieje taka para — wypisz `-1 -1`.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 2`)
# * kolejne `N` linii: liczby całkowite
# * ostatnia linia: `x` (liczba całkowita)
#
# ### Wyjście
#
# Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 1
# 3
# 4
# 5
# 2
# 5
# ```
#
# **Wyjście:**
#
# ```
# 0 2
# ```

source ../assert.sh

znajdz_pary() {

    local n=${#lista[@]}
    local suma=$1

    for ((i = 0; i < n; i++)); do
        for ((j = i + 1; j < n; j++)); do
            if [ $((lista[i] + lista[j])) -eq $suma ]; then
                wynik+=("${lista[$i]}, ${lista[$j]};")
            fi
        done
    done
}

test1() {
    local lista=(0 4 5 6 2 9 2 3)
    local suma=5
    local oczekiwane=('0, 5;' '2, 3;' '2, 3;')
    declare -a wynik
    znajdz_pary $suma
    assertArrayEqual wynik oczekiwane $LINENO
}

test2() {
    local lista=(1 -1 3 -3 4 5)
    local suma=0
    local oczekiwane=('1, -1;' '3, -3;')
    declare -a wynik
    znajdz_pary $suma
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test1
    test2
}

main "$@"

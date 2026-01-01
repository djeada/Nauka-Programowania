# ZAD-07 — Sortowanie listy 0/1/2
#
# **Poziom:** ★★☆
# **Tagi:** `sort`, `counting`
#
# ### Treść
#
# Otrzymujesz listę składającą się wyłącznie z `0`, `1` lub `2`. Posortuj ją rosnąco.
#
# ### Wejście
#
# * 1 linia: liczba naturalna `N`
# * 2 linia: `N` liczb (0/1/2) oddzielonych spacjami
#
# ### Wyjście
#
# * 1 linia: posortowana lista w formacie jak w przykładzie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 7
# 1 0 1 2 2 0 1
# ```
#
# **Wyjście:**
#
# ```
# [0, 0, 1, 1, 1, 2, 2]
# ```

source ../assert.sh

sortuj_liste() {
    local -n _lista_ref="$1"
    local -n _lista_ref="$1"

    local zera=()
    local jedynki=()
    local dwojki=()
    for i in "${_lista_ref[@]}"; do
        if [[ $i == 0 ]]; then
            zera+=("$i")
        elif [[ $i == 1 ]]; then
            jedynki+=("$i")
        else
            dwojki+=("$i")
        fi
    done

    _lista_ref=("${zera[@]}" "${jedynki[@]}" "${dwojki[@]}")
}

sortuj_liste() {
    local lista=(0 1 1 2 2 0 1 0 2)
    local oczekiwane=(0 0 0 1 1 1 2 2 2)
    sortuj_liste lista
    assertArrayEqual lista oczekiwane $LINENO
}

main() {
    test_sortuj_liste_binarna
}

main "$@"

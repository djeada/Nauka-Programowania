# ZAD-06 — Sortowanie listy binarnej (0/1)
#
# **Poziom:** ★★☆
# **Tagi:** `sort`, `counting`
#
# ### Treść
#
# Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Posortuj ją rosnąco.
#
# ### Wejście
#
# * 1 linia: liczba naturalna `N`
# * 2 linia: `N` liczb (0/1) oddzielonych spacjami
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
# 6
# 1 0 1 0 1 1
# ```
#
# **Wyjście:**
#
# ```
# [0, 0, 1, 1, 1, 1]
# ```

source ../assert.sh

# Sortuje listę binarną (0/1) metodą zliczania.
# Złożoność czasowa: O(n), gdzie n to liczba elementów
# Złożoność pamięciowa: O(n)
sortuj_liste_binarna() {
    local -n _lista_ref="$1"

    local zera=()
    local jedynki=()
    for i in "${_lista_ref[@]}"; do
        if [[ $i == 0 ]]; then
            zera+=("$i")
        else
            jedynki+=("$i")
        fi
    done

    _lista_ref=("${zera[@]}" "${jedynki[@]}")
}

test_sortuj_liste_binarna() {
    local lista=(0 1 1 0 1 0)
    local oczekiwane=(0 0 0 1 1 1)
    sortuj_liste_binarna lista
    assertArrayEqual lista oczekiwane $LINENO
}

main() {
    test_sortuj_liste_binarna
}

main "$@"

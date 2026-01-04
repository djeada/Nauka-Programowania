# ZAD-02 — Sortowanie przez wybieranie
#
# **Poziom:** ★★☆
# **Tagi:** `sorting`, `selection-sort`, `list`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wybieranie**.
# Dla każdej pozycji `i` znajdź najmniejszy element w zakresie `i..koniec` i zamień go z elementem na pozycji `i`.
#
# ### Wejście
#
# * 1 linia: lista liczb całkowitych
#
# ### Wyjście
#
# * 1 linia: posortowana lista rosnąco
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [6, 2, 1, 4, 27]
# ```
#
# **Wyjście:**
#
# ```
# [1, 2, 4, 6, 27]
# ```
#
# ### Uwagi o algorytmie
#
# * Złożoność czasowa: `O(n^2)`.
source ../assert.sh

sortuj() {
    local -n _tablica_ref=$1

    for ((i = 0; i < ${#_tablica_ref[@]} - 1; i++)); do
        min=$i
        for ((j = i + 1; j < ${#_tablica_ref[@]}; j++)); do
            if [[ ${_tablica_ref[j]} -lt ${_tablica_ref[min]} ]]; then
                min=$j
            fi
        done
        if [[ $min -ne $i ]]; then
            local tmp=${_tablica_ref[i]}
            _tablica_ref[i]=${_tablica_ref[min]}
            _tablica_ref[min]=$tmp
        fi
    done
}

test_sortuj() {
    local tablica=(4 2 5 3 1)
    local oczekiwane=(1 2 3 4 5)
    sortuj tablica
    assertArrayEqual tablica oczekiwane $LINENO
}

main() {
    test_sortuj
}

main "$@"

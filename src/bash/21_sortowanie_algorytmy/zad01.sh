# ZAD-01 — Sortowanie bąbelkowe
#
# **Poziom:** ★☆☆
# **Tagi:** `sorting`, `bubble-sort`, `list`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania bąbelkowego**.
# Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów i zamianie ich miejscami, jeśli są w złej kolejności. Powtarzaj przebiegi, aż w całym przebiegu nie zajdzie żadna zamiana.
#
# ### Wejście
#
# * 1 linia: lista liczb całkowitych, np. `[6, 2, 1, 4, 27]`
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
# * Po każdym pełnym przebiegu największy element „wypływa” na koniec.
# * W kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1.
source ../assert.sh

sortuj() {
    local -n _tablica_ref=$1
    local n=${#_tablica_ref[@]}
    local swapped=true

    while [ "$swapped" = true ]; do
        swapped=false
        for ((i = 0; i < n - 1; i++)); do
            if [[ ${_tablica_ref[i]} -gt ${_tablica_ref[i + 1]} ]]; then
                local tmp=${_tablica_ref[i]}
                _tablica_ref[i]=${_tablica_ref[i + 1]}
                _tablica_ref[i + 1]=$tmp
                swapped=true
            fi
        done
        ((n--))
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

# ZAD-03 — Sortowanie przez wstawianie
#
# **Poziom:** ★★☆
# **Tagi:** `sorting`, `insertion-sort`, `list`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wstawianie**.
# Buduj posortowany fragment od lewej strony: każdy kolejny element „wstaw” w odpowiednie miejsce, przesuwając większe elementy w prawo.
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
# * Działa bardzo dobrze dla danych prawie posortowanych.

source ../assert.sh

sortuj() {
    local -n _tablica_ref=$1

    for ((i = 1; i < ${#_tablica_ref[@]}; i++)); do
        local tmp=${_tablica_ref[$i]}
        local j=$((i - 1))
        while ((j >= 0 && _tablica_ref[j] > tmp)); do
            _tablica_ref[$((j + 1))]=${_tablica_ref[$j]}
            ((j--))
        done
        _tablica_ref[$((j + 1))]=$tmp
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

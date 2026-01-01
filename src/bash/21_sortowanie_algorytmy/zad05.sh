# ZAD-05 — Sortowanie szybkie
#
# **Poziom:** ★★☆
# **Tagi:** `sorting`, `quick-sort`, `recursion`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **Quick Sort**:
#
# 1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
# 2. Wybierz **pivot** (np. pierwszy element).
# 3. Podziel elementy na trzy grupy:
#
#    * mniejsze od pivota,
#    * równe pivotowi,
#    * większe od pivota.
# 4. Rekurencyjnie posortuj część mniejszych i większych.
# 5. Sklej wynik: `mniejsze + równe + większe`.
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
# * Średnio: `O(n log n)`, w pesymistycznym przypadku: `O(n^2)`.
# * Wybór pivota ma wpływ na wydajność.

source ../assert.sh

partycja() {
    local i=$1
    local j=$2
    j=$((j - 2))
    local klucz=${_tablica_ref[j + 1]}

    while [ $i -le $j ]; do
        if [ ${_tablica_ref[i]} -le $klucz ]; then
            i=$((i + 1))
        elif [ ${_tablica_ref[j]} -ge $klucz ]; then
            j=$((j - 1))
        else
            local tmp=${_tablica_ref[i]}
            _tablica_ref[i]=${_tablica_ref[j]}
            _tablica_ref[j]=$tmp
            i=$((i + 1))
            j=$((j - 1))
        fi
    done
    j=$2
    j=$((j - 1))

    local tmp=${_tablica_ref[i]}
    _tablica_ref[i]=${_tablica_ref[j]}
    _tablica_ref[j]=$tmp

    return $i
}

_sortuj() {
    local start=$1
    local stop=$2

    if [ $((stop - start)) -lt 2 ]; then
        return
    fi

    local i=$((start + RANDOM % (stop - start)))

    local tmp=${_tablica_ref[i]}
    _tablica_ref[i]=${_tablica_ref[stop - 1]}
    _tablica_ref[stop - 1]=$tmp
    partycja $start $stop
    i=$?

    _sortuj $start $i
    _sortuj $((i + 1)) $stop
}

sortuj() {
    local -n _tablica_ref=$1
    _sortuj 0 ${#_tablica_ref[@]}
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

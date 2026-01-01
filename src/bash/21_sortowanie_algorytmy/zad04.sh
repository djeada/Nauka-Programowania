# ZAD-04 — Sortowanie przez scalanie
#
# **Poziom:** ★★☆
# **Tagi:** `sorting`, `merge-sort`, `recursion`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez scalanie**:
#
# 1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
# 2. Podziel listę na dwie (w miarę) równe części.
# 3. Rekurencyjnie posortuj obie części.
# 4. **Scal** dwie posortowane listy w jedną posortowaną.
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
# * Złożoność czasowa: `O(n log n)`.

source ../assert.sh

scalaj() {
    local dane=("$@")
    local _tablica_a=(${dane[@]:0:${#dane[@]}/2})
    local _tablica_b=(${dane[@]:${#dane[@]}/2})
    local _tablica_c=()

    local i=0
    local j=0
    while [ $i -lt ${#_tablica_a[@]} ] && [ $j -lt ${#_tablica_b[@]} ]; do
        if [ ${_tablica_a[$i]} -lt ${_tablica_b[$j]} ]; then
            _tablica_c+=("${_tablica_a[$i]}")
            i=$((i + 1))
        else
            _tablica_c+=("${_tablica_b[$j]}")
            j=$((j + 1))
        fi
    done

    while [ $i -lt ${#_tablica_a[@]} ]; do
        _tablica_c+=("${_tablica_a[$i]}")
        i=$((i + 1))
    done

    while [ $j -lt ${#_tablica_b[@]} ]; do
        _tablica_c+=("${_tablica_b[$j]}")
        j=$((j + 1))
    done

    echo "${_tablica_c[@]}"
}

sortuj() {
    local _tablica_ref=("$@")

    if [ ${#_tablica_ref[@]} -gt 1 ]; then
        local _lewo=(${_tablica_ref[@]:0:${#_tablica_ref[@]}/2})
        local _prawo=(${_tablica_ref[@]:${#_tablica_ref[@]}/2})

        echo "$(scalaj "$(sortuj "${_lewo[@]}")" "$(sortuj "${_prawo[@]}")")"
        return
    fi

    echo "${_tablica_ref[@]}"
}

test_sortuj() {
    local tablica=(4 2 5 3 1)
    local wynik=($(sortuj ${tablica[@]}))
    local oczekiwane=(1 2 3 4 5)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_sortuj
}

main "$@"

# ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów
#
# **Poziom:** ★★☆
# **Tagi:** `list`, `merge`, `sort`
#
# ### Treść
#
# Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w jedną listę:
#
# * wynik ma być posortowany rosnąco,
# * wynik ma zawierać **unikalne** elementy (bez duplikatów).
#
# ### Wejście
#
# * 1 linia: lista 1 (posortowana rosnąco)
# * 2 linia: lista 2 (posortowana rosnąco)
#
# ### Wyjście
#
# * 1 linia: jedna posortowana lista bez duplikatów
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [2, 4, 7]
# [3, 5, 9]
# ```
#
# **Wyjście:**
#
# ```
# [2, 3, 4, 5, 7, 9]
# ```

source ../assert.sh

polacz_v1() {
    wynik=()

    local n=${#lista_a[@]}
    local m=${#lista_b[@]}

    if [ $n -eq 0 ] || [ $m -eq 0 ]; then
        return
    fi

    local i=0
    local j=0

    while [ $i -lt $n ] && [ $j -lt $m ]; do
        if [ ${lista_a[$i]} -lt ${lista_b[$j]} ]; then
            wynik+=("${lista_a[$i]}")
            i=$((i + 1))
        else
            wynik+=("${lista_b[$j]}")
            j=$((j + 1))
        fi
    done

    while [ $i -lt $n ]; do
        wynik+=("${lista_a[$i]}")
        i=$((i + 1))
    done

    while [ $j -lt $m ]; do
        wynik+=("${lista_b[$j]}")
        j=$((j + 1))
    done

}

test1() {
    local lista_a=(5 7 11)
    local lista_b=(1 3 8 14)
    local oczekiwane=(1 3 5 7 8 11 14)
    polacz_v1
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test1
}

main "$@"

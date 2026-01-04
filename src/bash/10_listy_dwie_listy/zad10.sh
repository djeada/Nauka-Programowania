# ZAD-10 — Mediana dwóch posortowanych list
#
# **Poziom:** ★★☆
# **Tagi:** `list`, `median`, `sort`
#
# ### Treść
#
# Wczytaj dwie listy liczb całkowitych:
#
# * obie są posortowane rosnąco,
# * obie mają tę samą, niezerową długość.
#
# Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po „złączeniu” obu list).
#
# ### Wejście
#
# * 1 linia: lista 1 (posortowana rosnąco)
# * 2 linia: lista 2 (posortowana rosnąco)
#
# ### Wyjście
#
# * 1 linia: mediana jako liczba zmiennoprzecinkowa
#   (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)
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
# 4.5
# ```
source ../assert.sh

mediana() {
    local n=${#lista_a[@]}
    local m=${#lista_b[@]}

    local i=0
    local j=0
    local m1=-1
    local m2=-1

    for ((licznik = 0; licznik <= (n + m) / 2; licznik++)); do

        if [ $(((m + n) % 2)) -eq 0 ]; then
            m2=$m1
        fi

        if [ $i -ne $n ] && [ $j -ne $m ]; then
            if [ ${lista_a[$i]} -gt ${lista_b[$j]} ]; then
                m1=${lista_b[$j]}
                j=$((j + 1))
            else
                m1=${lista_a[$i]}
                i=$((i + 1))
            fi
        elif [ $i -lt $n ]; then
            m1=${lista_a[$i]}
            i=$((i + 1))
        else
            m1=${lista_b[$j]}
            j=$((j + 1))
        fi
    done

    if [ $(((m + n) % 2)) -eq 1 ]; then
        echo $m1
    else
        echo $(bc -l <<<"scale=2; ($m1+$m2)/2")
    fi

}

test1() {
    local lista_a=(2 4 7)
    local lista_b=(3 5 9)
    local wynik=4.50
    assertEqual $(mediana) $wynik $LINENO
}

main() {
    test1
}

main "$@"

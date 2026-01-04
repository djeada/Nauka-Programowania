# ZAD-01 — Najdłuższy ciąg jedynek
#
# **Poziom:** ★★☆
# **Tagi:** `list`, `0/1`, `analiza`, `indeksy`
#
# ### Treść
#
# Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.
#
# Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.
#
# ### Wejście
#
# * 1 linia: lista `A` (tylko `0` i `1`)
#
# ### Wyjście
#
# * 1 linia: indeks (liczba całkowita) albo `-1`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
# ```
#
# **Wyjście:**
#
# ```
# 7
# ```
#
# ### Uwagi
#
# * Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).
source ../assert.sh

# Znajduje indeks zera, którego zamiana na 1 da najdłuższy ciąg jedynek.
# Złożoność czasowa: O(n^2), gdzie n to liczba elementów
# Złożoność pamięciowa: O(1)
znajdz_najlepsze_zero() {
    local -n _lista_ref=$1
    local n=${#_lista_ref[@]}

    # Sprawdź czy są zera i jedynki
    local ma_zero=0
    local ma_jeden=0
    for el in "${_lista_ref[@]}"; do
        [ $el -eq 0 ] && ma_zero=1
        [ $el -eq 1 ] && ma_jeden=1
    done

    if [ $ma_zero -eq 0 ] || [ $ma_jeden -eq 0 ]; then
        echo -1
        return
    fi

    local max_dlugosc=0
    local best_idx=-1

    # Dla każdego zera sprawdź długość ciągu po zamianie
    for ((i = 0; i < n; i++)); do
        if [ ${_lista_ref[$i]} -eq 0 ]; then
            # Policz ciągłe jedynki na lewo
            local lewo=0
            for ((j = i - 1; j >= 0; j--)); do
                if [ ${_lista_ref[$j]} -eq 1 ]; then
                    ((lewo++))
                else
                    break
                fi
            done

            # Policz ciągłe jedynki na prawo
            local prawo=0
            for ((j = i + 1; j < n; j++)); do
                if [ ${_lista_ref[$j]} -eq 1 ]; then
                    ((prawo++))
                else
                    break
                fi
            done

            local dlugosc=$((lewo + prawo + 1))
            if [ $dlugosc -gt $max_dlugosc ]; then
                max_dlugosc=$dlugosc
                best_idx=$i
            fi
        fi
    done

    echo $best_idx
}

test_znajdz_najlepsze_zero() {
    local lista=(0 0 1 0 1 1 1 0 1 1)
    local wynik=$(znajdz_najlepsze_zero lista)
    assertEqual "$wynik" "7" $LINENO

    local lista2=(1 1 1 1)
    local wynik2=$(znajdz_najlepsze_zero lista2)
    assertEqual "$wynik2" "-1" $LINENO

    local lista3=(0 0 0 0)
    local wynik3=$(znajdz_najlepsze_zero lista3)
    assertEqual "$wynik3" "-1" $LINENO
}

main() {
    test_znajdz_najlepsze_zero
}

main "$@"

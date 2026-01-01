# ZAD-04 — Wspólny podciąg o największej długości (równe sumy)
#
# **Poziom:** ★★★
# **Tagi:** `list`, `prefix`, `hashmap`, `podciąg`
#
# ### Treść
#
# Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości. Znajdź **maksymalną długość** podciągu (ciągłych elementów), dla którego suma elementów w podciągu z `A` jest równa sumie elementów w odpowiadającym podciągu z `B` (ten sam zakres indeksów).
#
# ### Wejście
#
# * 1 linia: lista binarna `A`
# * 2 linia: lista binarna `B` (tej samej długości)
#
# ### Wyjście
#
# * 1 linia: maksymalna długość (liczba naturalna)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [0, 0, 1, 1, 1, 1]
# [0, 1, 1, 0, 1, 0]
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```

source ../assert.sh

# Znajduje maksymalną długość podciągu z równymi sumami.
# Złożoność czasowa: O(n^2), gdzie n to liczba elementów
# Złożoność pamięciowa: O(1)
max_dlugosc_rowne_sumy() {
    local -n _lista_a_ref=$1
    local -n _lista_b_ref=$2
    local n=${#_lista_a_ref[@]}
    local max_len=0
    
    # Sprawdź wszystkie podciągi
    for ((i=0; i<n; i++)); do
        local suma_a=0
        local suma_b=0
        for ((j=i; j<n; j++)); do
            suma_a=$((suma_a + ${_lista_a_ref[$j]}))
            suma_b=$((suma_b + ${_lista_b_ref[$j]}))
            
            if [ $suma_a -eq $suma_b ]; then
                local len=$((j - i + 1))
                [ $len -gt $max_len ] && max_len=$len
            fi
        done
    done
    
    echo $max_len
}

test_max_dlugosc_rowne_sumy() {
    local lista_a=(0 0 1 1 1 1)
    local lista_b=(0 1 1 0 1 0)
    local wynik=$(max_dlugosc_rowne_sumy lista_a lista_b)
    assertEqual "$wynik" "5" $LINENO
}

main() {
    test_max_dlugosc_rowne_sumy
}

main "$@"

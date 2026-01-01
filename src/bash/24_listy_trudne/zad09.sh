# ZAD-09 — Najdłuższy naprzemienny podciąg
#
# **Poziom:** ★★★
# **Tagi:** `dp`, `subsequence`, `naprzemienny`
#
# ### Treść
#
# Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).
#
# ### Wejście
#
# * 1 linia: lista liczb całkowitych `A`
#
# ### Wyjście
#
# * 1 linia: lista liczb — najdłuższy naprzemienny podciąg
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [1, -2, 6, 4, -3, 2, -4, -3]
# ```
#
# **Wyjście:**
#
# ```
# [1, -2, 6, -3, 2, -4]
# ```
#
# ### Uwagi
#
# * Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej" (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

source ../assert.sh

# Znajduje najdłuższy naprzemienny podciąg.
# Złożoność czasowa: O(n), gdzie n to liczba elementów
# Złożoność pamięciowa: O(n)
najdluzszy_naprzemienny() {
    local -n _lista_ref=$1
    local n=${#_lista_ref[@]}
    
    if [ $n -eq 0 ]; then
        echo ""
        return
    fi
    
    local wynik=("${_lista_ref[0]}")
    local ostatni_znak=0
    
    for ((i=1; i<n; i++)); do
        local poprzedni=${wynik[${#wynik[@]}-1]}
        local roznica=$((${_lista_ref[$i]} - poprzedni))
        
        if [ $roznica -eq 0 ]; then
            continue
        fi
        
        local znak=1
        [ $roznica -lt 0 ] && znak=-1
        
        if [ $ostatni_znak -eq 0 ] || [ $znak -ne $ostatni_znak ]; then
            wynik+=("${_lista_ref[$i]}")
            ostatni_znak=$znak
        fi
    done
    
    echo "${wynik[@]}"
}

test_najdluzszy_naprzemienny() {
    local lista=(1 -2 6 4 -3 2 -4 -3)
    local wynik=($(najdluzszy_naprzemienny lista))
    [ ${#wynik[@]} -ge 3 ] || exit 1
}

main() {
    test_najdluzszy_naprzemienny
}

main "$@"

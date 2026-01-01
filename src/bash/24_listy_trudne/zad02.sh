# ZAD-02 — Przesuń zera na koniec listy
#
# **Poziom:** ★★☆
# **Tagi:** `list`, `stabilność`, `przekształcenie`
#
# ### Treść
#
# Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.
#
# ### Wejście
#
# * 1 linia: lista liczb całkowitych `A`
#
# ### Wyjście
#
# * 1 linia: lista po przekształceniu
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
# ```
#
# **Wyjście:**
#
# ```
# [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
# ```

source ../assert.sh

# Przenosi wszystkie zera na koniec listy, zachowując kolejność pozostałych.
# Złożoność czasowa: O(n), gdzie n to liczba elementów
# Złożoność pamięciowa: O(n)
przesun_zera() {
    local -n _lista_ref=$1
    local nie_zera=()
    local zera=()
    
    for el in "${_lista_ref[@]}"; do
        if [ $el -eq 0 ]; then
            zera+=("$el")
        else
            nie_zera+=("$el")
        fi
    done
    
    _lista_ref=("${nie_zera[@]}" "${zera[@]}")
}

test_przesun_zera() {
    local lista=(0 1 3 0 8 12 0 4 0 7 0)
    local oczekiwane=(1 3 8 12 4 7 0 0 0 0 0)
    przesun_zera lista
    assertArrayEqual lista oczekiwane $LINENO
    
    local lista2=(1 2 3 4 5)
    local oczekiwane2=(1 2 3 4 5)
    przesun_zera lista2
    assertArrayEqual lista2 oczekiwane2 $LINENO
}

main() {
    test_przesun_zera
}

main "$@"

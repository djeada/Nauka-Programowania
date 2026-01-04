# ZAD-06 — Połączenie posortowanych list (unikalne)
#
# **Poziom:** ★★★
# **Tagi:** `merge`, `heap`, `unique`, `sorted`
#
# ### Treść
#
# Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez powtórzeń**.
#
# ### Wejście
#
# * 1 linia: lista list (każda wewnętrzna lista jest posortowana)
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
# [[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
# ```
#
# **Wyjście:**
#
# ```
# [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
# ```
source ../assert.sh

# Łączy posortowane listy w jedną posortowaną bez duplikatów.
# Złożoność czasowa: O(n log n), gdzie n to całkowita liczba elementów
# Złożoność pamięciowa: O(n)
polacz_posortowane_listy() {
    local wszystkie=()

    # Zbierz wszystkie elementy
    for arg in "$@"; do
        wszystkie+=($arg)
    done

    # Sortuj i usuń duplikaty
    local posortowane=($(printf '%s\n' "${wszystkie[@]}" | sort -n | uniq))

    echo "${posortowane[@]}"
}

test_polacz_posortowane_listy() {
    local wynik=($(polacz_posortowane_listy "-6 23 29 33" "6 22 35 71" "5 19 21 37" "-12 -7 -3 28"))
    # Sprawdź czy są wszystkie unikalne posortowane
    assertEqual "${wynik[0]}" "-12" $LINENO
    assertEqual "${wynik[${#wynik[@]} - 1]}" "71" $LINENO
}

main() {
    test_polacz_posortowane_listy
}

main "$@"

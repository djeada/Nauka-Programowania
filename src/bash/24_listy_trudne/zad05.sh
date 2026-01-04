# ZAD-05 — Zbiór potęgowy listy
#
# **Poziom:** ★★★
# **Tagi:** `list`, `subsets`, `combinatorics`
#
# ### Treść
#
# Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.
#
# Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).
#
# ### Wejście
#
# * 1 linia: lista liczb naturalnych `A`
#
# ### Wyjście
#
# * 1 linia: lista list (wszystkie podzbiory)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [1, 2, 1]
# ```
#
# **Wyjście:**
#
# ```
# [[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
# ```
#
# ### Uwagi
#
# * Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)
source ../assert.sh

# Generuje wszystkie podzbiory listy.
# Złożoność czasowa: O(2^n * n), gdzie n to liczba elementów
# Złożoność pamięciowa: O(2^n * n)
zbior_potegowy() {
    local -n _lista_ref=$1
    local n=${#_lista_ref[@]}
    local wynik=()

    # Dla każdej maski bitowej od 0 do 2^n-1
    for ((mask = 0; mask < (1 << n); mask++)); do
        local podzbior=()
        for ((i = 0; i < n; i++)); do
            # Sprawdź czy i-ty bit jest ustawiony
            if (((mask >> i) & 1)); then
                podzbior+=("${_lista_ref[$i]}")
            fi
        done

        # Dodaj podzbior do wyniku
        if [ ${#podzbior[@]} -eq 0 ]; then
            wynik+=("[]")
        else
            wynik+=("[${podzbior[*]}]")
        fi
    done

    echo "${wynik[@]}"
}

test_zbior_potegowy() {
    local lista=(1 2)
    local wynik=$(zbior_potegowy lista)
    # Sprawdź czy wynik zawiera puste i pełne podzbiory
    [[ "$wynik" == *"[]"* ]] && [[ "$wynik" == *"[1 2]"* ]] || exit 1
}

main() {
    test_zbior_potegowy
}

main "$@"

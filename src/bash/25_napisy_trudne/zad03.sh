# ZAD-03 — Czy napis A jest początkiem napisu B?
#
# **Poziom:** ★★☆
# **Tagi:** `string`, `prefix`
#
# ### Treść
#
# Otrzymujesz dwa napisy:
#
# 1. Napis `A` — potencjalny przedrostek,
# 2. Napis `B` — napis testowany.
#
# Sprawdź, czy `B` **zaczyna się** od `A`.
#
# ### Wejście
#
# * 1 linia: `A`
# * 2 linia: `B`
#
# ### Wyjście
#
# * 1 linia: `Prawda` albo `Fałsz`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Dino
# Dinozaur jest zly
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```

source ../assert.sh

# Sprawdza, czy napis B zaczyna się od napisu A.
# Złożoność czasowa: O(m), gdzie m to długość A
# Złożoność pamięciowa: O(1)
czy_prefix() {
    local napis_a="$1"
    local napis_b="$2"
    
    if [[ "$napis_b" == "$napis_a"* ]]; then
        echo "Prawda"
    else
        echo "Fałsz"
    fi
}

test_czy_prefix() {
    local wynik=$(czy_prefix "Dino" "Dinozaur jest zly")
    assertEqual "$wynik" "Prawda" $LINENO
    
    local wynik2=$(czy_prefix "ABC" "XYZ")
    assertEqual "$wynik2" "Fałsz" $LINENO
}

main() {
    test_czy_prefix
}

main "$@"

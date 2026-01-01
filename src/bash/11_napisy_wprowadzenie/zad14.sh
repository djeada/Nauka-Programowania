# ZAD-14 — Napis z liczb od 1 do n
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `string`
#
# ### Treść
#
# Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.
#
# ### Wejście
#
# * 1. linia: liczba naturalna `n` (n ≥ 1)
#
# ### Wyjście
#
# * 1. linia: ciąg `1..n` bez spacji
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# ```
#
# **Wyjście:**
#
# ```
# 123
# ```

source ../assert.sh

# Funkcja tworzaca napis z liczb od 1 do n
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n) dla wyniku
liczby() {

    local n="$1"
    local wynik=""

    # Iteracja od 1 do n
    for ((i = 1; i <= n; i++)); do
        local wynik="$wynik$i"
    done

    echo "$wynik"

}

test1() {
    local n=5
    local wynik="12345"
    assertEqual "$(liczby $n)" "$wynik" $LINENO
}

test2() {
    local n="-1"
    local wynik=""
    assertEqual "$(liczby $n)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

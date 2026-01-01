# ZAD-05 — Usuń powtórzenia sąsiadujących znaków
#
# **Poziom:** ★★★
# **Tagi:** `string`, `compress`, `run-length`
#
# ### Treść
#
# Otrzymujesz napis. Usuń powtórzenia znaków występujących **bezpośrednio obok siebie**, pozostawiając jedno wystąpienie z każdej „serii”.
#
# ### Wejście
#
# * 1 linia: napis `S`
#
# ### Wyjście
#
# * 1 linia: napis po redukcji sąsiadów
#
# ### Przykład
#
# **Wejście:**
#
# ```
# AAAAAAAAAABBBBBBBBA
# ```
#
# **Wyjście:**
#
# ```
# ABA
# ```

source ../assert.sh

# Usuwa powtórzenia sąsiadujących znaków.
# Złożoność czasowa: O(n), gdzie n to długość napisu
# Złożoność pamięciowa: O(n)
usun_sasiadow() {
    local napis="$1"
    local wynik=""
    local poprzedni=""
    local i
    
    for ((i=0; i<${#napis}; i++)); do
        local znak="${napis:$i:1}"
        if [ "$znak" != "$poprzedni" ]; then
            wynik="$wynik$znak"
            poprzedni="$znak"
        fi
    done
    
    echo "$wynik"
}

test_usun_sasiadow() {
    local wynik=$(usun_sasiadow "AAAAAAAAAABBBBBBBBA")
    assertEqual "$wynik" "ABA" $LINENO
    
    local wynik2=$(usun_sasiadow "AABBCCDD")
    assertEqual "$wynik2" "ABCD" $LINENO
}

main() {
    test_usun_sasiadow
}

main "$@"

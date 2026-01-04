# ZAD-04 — Usuń powtórzenia znaków
#
# **Poziom:** ★★★
# **Tagi:** `string`, `set`, `unique`, `kolejność`
#
# ### Treść
#
# Otrzymujesz napis. Usuń wszystkie powtórzenia znaków tak, aby **każdy znak wystąpił tylko raz**, zachowując **kolejność pierwszych wystąpień**.
#
# ### Wejście
#
# * 1 linia: napis `S`
#
# ### Wyjście
#
# * 1 linia: napis z unikalnymi znakami
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
# AB
# ```
source ../assert.sh

# Usuwa powtórzenia znaków, zachowując pierwsze wystąpienia.
# Złożoność czasowa: O(n^2), gdzie n to długość napisu
# Złożoność pamięciowa: O(n)
usun_powtorzenia() {
    local napis="$1"
    local wynik=""
    local i

    for ((i = 0; i < ${#napis}; i++)); do
        local znak="${napis:$i:1}"
        # Sprawdź czy znak już jest w wyniku
        if [[ "$wynik" != *"$znak"* ]]; then
            wynik="$wynik$znak"
        fi
    done

    echo "$wynik"
}

test_usun_powtorzenia() {
    local wynik=$(usun_powtorzenia "AAAAAAAAAABBBBBBBBA")
    assertEqual "$wynik" "AB" $LINENO

    local wynik2=$(usun_powtorzenia "ABCABC")
    assertEqual "$wynik2" "ABC" $LINENO
}

main() {
    test_usun_powtorzenia
}

main "$@"

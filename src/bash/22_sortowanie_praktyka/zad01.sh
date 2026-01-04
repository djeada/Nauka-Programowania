# ZAD-01 — Sortowanie znaków w napisie
#
# **Poziom:** ★☆☆
# **Tagi:** `sort`, `string`
#
# ### Treść
#
# Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy napis.
#
# ### Wejście
#
# * 1 linia: napis `s`
#
# ### Wyjście
#
# * 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w Pythonie / Unicode)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Ala ma kota
# ```
#
# **Wyjście:**
#
# ```
#  Aaaaklmot
# ```
#
# ### Uwagi o formatowaniu
#
# * Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie wyjście zaczyna się od spacji).
source ../assert.sh

# Sortuje wszystkie znaki w napisie alfabetycznie.
# Złożoność czasowa: O(n log n), gdzie n to liczba znaków
# Złożoność pamięciowa: O(n)
sortuj_napis() {
    local napis="$1"
    echo "$napis" | grep -o . | sort | tr -d "\n"
    echo
}

test_sortuj_napis() {
    assertEqual "$(sortuj_napis "Ala ma kota")" "  Aaaaklmot" $LINENO
    assertEqual "$(sortuj_napis "kot ma Ale")" "  Aaeklmot" $LINENO
}

main() {
    test_sortuj_napis
}

main "$@"

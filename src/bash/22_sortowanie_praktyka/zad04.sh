# ZAD-04 — Sortowanie napisów według długości
#
# **Poziom:** ★☆☆
# **Tagi:** `sort`, `string`, `list`
#
# ### Treść
#
# Otrzymujesz listę napisów. Posortuj ją rosnąco według długości napisów.
#
# ### Wejście
#
# * 1 linia: liczba naturalna `N`
# * następnie `N` linii: napis (bez spacji)
#
# ### Wyjście
#
# * 1 linia: lista napisów posortowana jak w przykładzie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4
# abcd
# ab
# a
# abc
# ```
#
# **Wyjście:**
#
# ```
# ['a', 'ab', 'abc', 'abcd']
# ```

source ../assert.sh

sortuj_wzgledem_dlugosci() {
    local -n _lista_ref="$1"
    echo "${_lista_ref[@]}" | tr " " "\n" | awk '{print length($0), $0}' | sort -n -k1,1 | cut -d' ' -f2- | tr "\n" " "
}

test_sortuj_wzgledem_dlugosci() {
    local lista=(Ala ma kota a kot ma Ale)
    local oczekiwane=(a ma ma Ala Ale kot kota)
    local wynik=$(sortuj_wzgledem_dlugosci lista)
    assertArrayEqual lista oczekiwane wynik
}

main() {
    test_sortuj_wzgledem_dlugosci
}

main "$@"

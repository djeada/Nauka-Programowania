# ZAD-06 — Zamień litery „a” na „?”
#
# **Poziom:** ★☆☆
# **Tagi:** `string`, `replace`
#
# ### Treść
#
# Wczytaj napis i zamień wszystkie wystąpienia litery `a` na znak `?`.
#
# ### Wejście
#
# * 1. linia: napis
#
# ### Wyjście
#
# * 1. linia: napis po zamianie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Latarnik
# ```
#
# **Wyjście:**
#
# ```
# L?t?rnik
# ```
source ../assert.sh

# Zamiana wszystkich wystapien litery 'a' na znak '?'
# Zlozonosc czasowa: O(n), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(n) dla wyniku
zamien() {
    sed -r 's/a/?/g' <<<"$1"
}

test1() {
    local napis="pacZka!"
    local wynik="p?cZk?!"
    assertEqual "$(zamien "$napis")" "$wynik" $LINENO
}

main() {
    test1
}

main "$@"

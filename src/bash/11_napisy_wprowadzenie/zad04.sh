# ZAD-04 — Zamień wszystkie małe litery na duże
#
# **Poziom:** ★☆☆
# **Tagi:** `string`, `upper`
#
# ### Treść
#
# Wczytaj napis i zamień wszystkie litery na wielkie.
#
# ### Wejście
#
# * 1. linia: napis
#
# ### Wyjście
#
# * 1. linia: napis po konwersji
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Rumcajs
# ```
#
# **Wyjście:**
#
# ```
# RUMCAJS
# ```

source ../assert.sh

na_wielkie_v1() {
    awk '{ print toupper($0) }' <<<"$1"
}

na_wielkie_v2() {
    tr a-z A-Z <<<"$1"
}

test1() {
    local napis="pacZka!"
    local wynik="PACZKA!"
    assertEqual "$(na_wielkie_v1 "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="pacZka!"
    local wynik="PACZKA!"
    assertEqual "$(na_wielkie_v2 "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

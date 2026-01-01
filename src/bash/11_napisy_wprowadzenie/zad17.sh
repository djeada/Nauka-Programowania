# ZAD-17 — Konwersja listy na napis
#
# **Poziom:** ★☆☆
# **Tagi:** `list`, `string`
#
# ### Treść
#
# Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`). Połącz liczby bez separatorów i wypisz jako napis.
#
# ### Wejście
#
# * 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`
#
# ### Wyjście
#
# * 1. linia: napis z połączonych liczb, np. `247`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [2, 4, 7]
# ```
#
# **Wyjście:**
#
# ```
# 247
# ```
#
# ### Uwagi
#
# * Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem sklej.

source ../assert.sh

liczby() {
    printf -v wynik '%s' "${lista[@]}"
    echo "$wynik"
}

test1() {
    local lista=(1 2 3 4)
    local wynik="1234"
    assertEqual "$(liczby)" "$wynik" $LINENO
}

test2() {
    local lista=()
    local wynik=""
    assertEqual "$(liczby)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

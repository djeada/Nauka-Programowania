# ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo
#
# **Poziom:** ★☆☆
# **Tagi:** `regex`, `string`
#
# ### Treść
#
# Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu jako samodzielne słowo (nie jako fragment innego słowa).
#
# ### Wejście
#
# Dwie linie:
#
# 1. `zdanie`
# 2. `slowo`
#
# ### Wyjście
#
# Jedna linia:
#
# * `Prawda` albo `Fałsz`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Siała baba mak.
# babcia
# ```
#
# **Wyjście:**
#
# ```
# Fałsz
# ```
source ../assert.sh

# Sprawdza, czy słowo (napis_b) występuje jako fragment w zdaniu (napis_a).
# Złożoność czasowa: O(n), gdzie n to długość napis_a
# Złożoność pamięciowa: O(1)
czy_podnapis() {
    local napis_a="$1"
    local napis_b="$2"

    if [[ $napis_a =~ $napis_b ]]; then
        echo "true"
    else
        echo "false"
    fi
}

test_czy_podnapis() {
    assertTrue $(czy_podnapis "abcdef" "cde") $LINENO
    assertTrue $(czy_podnapis "abcdef" "cdef") $LINENO
    assertFalse $(czy_podnapis "abcdef" "cdefg") $LINENO
    assertFalse $(czy_podnapis "abcdef" "abca") $LINENO
}

main() {
    test_czy_podnapis
}

main "$@"

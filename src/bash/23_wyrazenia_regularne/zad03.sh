# ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr
#
# **Poziom:** ★☆☆
# **Tagi:** `regex`, `string`
#
# ### Treść
#
# Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).
#
# ### Wejście
#
# Jedna linia:
#
# * `s`
#
# ### Wyjście
#
# Jedna linia:
#
# * `Prawda` — jeśli napis zawiera tylko cyfry
# * `Fałsz` — w przeciwnym razie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 1234
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```
source ../assert.sh

# Sprawdza, czy napis składa się wyłącznie z cyfr.
# Złożoność czasowa: O(n), gdzie n to długość napisu
# Złożoność pamięciowa: O(1)
wylacznie_cyfry() {
    local napis=$1

    if [[ $napis =~ ^[0-9]+$ ]]; then
        echo "true"
    else
        echo "false"
    fi
}

test_wylacznie_cyfry() {
    assertTrue $(wylacznie_cyfry "123") $LINENO
    assertTrue $(wylacznie_cyfry "12345") $LINENO
    assertFalse $(wylacznie_cyfry "123a") $LINENO
    assertFalse $(wylacznie_cyfry "a123") $LINENO
}

main() {
    test_wylacznie_cyfry
}

main "$@"

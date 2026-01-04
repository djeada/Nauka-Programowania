# ZAD-06 — Rotacje napisów
#
# **Poziom:** ★★★
# **Tagi:** `string`, `rotation`, `substring`
#
# ### Treść
#
# Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).
#
# ### Wejście
#
# * 1 linia: napis `A`
# * 2 linia: napis `B`
#
# ### Wyjście
#
# * 1 linia: `Prawda` albo `Fałsz`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# malpka
# pkamal
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```
source ../assert.sh

# Sprawdza, czy jeden napis jest rotacją drugiego.
# Złożoność czasowa: O(n), gdzie n to długość napisu
# Złożoność pamięciowa: O(n)
czy_rotacja() {
    local napis_a="$1"
    local napis_b="$2"

    # Jeśli długości różne, nie może być rotacją
    if [ ${#napis_a} -ne ${#napis_b} ]; then
        echo "Fałsz"
        return
    fi

    # Jeśli A jest rotacją B, to A jest podnapisem B+B
    local podwojony="${napis_b}${napis_b}"
    if [[ "$podwojony" == *"$napis_a"* ]]; then
        echo "Prawda"
    else
        echo "Fałsz"
    fi
}

test_czy_rotacja() {
    local wynik=$(czy_rotacja "malpka" "pkamal")
    assertEqual "$wynik" "Prawda" $LINENO

    local wynik2=$(czy_rotacja "abc" "xyz")
    assertEqual "$wynik2" "Fałsz" $LINENO
}

main() {
    test_czy_rotacja
}

main "$@"

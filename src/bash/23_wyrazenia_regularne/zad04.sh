# Tytul: Wiersze konczace sie okreslonym napisem.
# Tresc: Dostajesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace sie drugim napisem. Wiersz moze byc zakonczony dowolnym znakiem interpunkcyjnym.
# Dane wejsciowe: Dwa napisy.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla napisow:
# > Folgujmy paniom nie sobie, ma rada;
# Milujmy wiernie nie jest w nich przysada.
# Godnosci trzeba nie za nic tu cnota,
# Milosci pragna nie pragna tu zlota.
# oraz
# > da
# powinna zostac zwrocona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

source ../assert.sh

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


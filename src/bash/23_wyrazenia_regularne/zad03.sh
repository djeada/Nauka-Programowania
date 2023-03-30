# Tytul: Wyodrebnij cyfry z tekstu.
# Tresc: Dostajesz napis. Zwroc napis skladajacy sie z cyfr wystepujacych w tym napisie.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla napisu: “Terminator2001”, powinien zostac zwrocony napis: “2001”.

source ../assert.sh

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


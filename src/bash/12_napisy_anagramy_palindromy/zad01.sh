# Tytul: Sprawdzenie, czy slowo jest palindromem.
# Tresc: Napisz program, ktory sprawdzi, czy slowo jest palindromem. Palindromem jest slowo, ktore brzmi tak samo czytane od lewej do prawej i od prawej do lewej.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Wartosc logiczna.
# Przyklad:
# Dla otrzymanego napisu: “kajak”, powinna zostac zwrocona wartosc logiczna: Prawda.

source ../assert.sh

czy_palindrom() {
    local slowo="$1"
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

test_czy_palindrom() {
    assertTrue "czy_palindrom 'kajak'"
    assertFalse "czy_palindrom 'kot'"
}

main() {
    test_czy_palindrom
}

main "$@"

# Tytul: Sprawdz czy slowo wystepuje w zdaniu.
# Tresc: Dostajesz dwa napisy. Sprawdz, czy drugi napis wystepuje w pierwszym jako pojedyncze slowo.
# Dane wejsciowe: Dwa napisy.
# Dane wyjsciowe: Wartosc logiczna.
# Przyklad:
# Dla napisow: “Siala baba mak.” oraz “babcia”, powinna zostac zwrocona wartosc logiczna: Falsz.

source ../assert.sh

czy_haslo_poprawne() {
    local haslo=$1

    if [[ ${#haslo} -lt 8 || ${#haslo} -gt 20 ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[a-z]') ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[A-Z]') ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[0-9]') ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[! \# $ % & \\'' * + - / = ? ^ _ \` { | } ~]') ]]; then
        echo "false"
        return
    fi

    echo "true"
}

test_czy_haslo_poprawne() {
    assertFalse "$(czy_haslo_poprawne 'Ab1!')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'haslo')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'HASLO')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'HASLO123!@#')" $LINENO
    assertFalse "$(czy_haslo_poprawne '12345678')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'proste_haslo')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'Haslo123')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!#')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!#$')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!#$%&*')" $LINENO
}

main() {
    test_czy_haslo_poprawne
}

main "$@"


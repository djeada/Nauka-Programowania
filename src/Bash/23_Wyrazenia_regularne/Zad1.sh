#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy adres email. Sprawdz jego poprawnosc.
# Pamietaj, ze kazdy adres email sklada sie z identyfikatora uzytkownika, 
# znaku @ oraz nazwy domenowej.
# 
# Identyfikator uzytkownika sklada sie jedynie z:
# a) Malych (a-z) i wielkich (A-Z) liter.
# b) Cyfr (0-9).
# c) Znakow  ! # $ % & ' * + - / = ? ^ _ ` { | } ~.
# d) Kropki . pod warunkiem, ze nie jest pierwszym badz ostatnim znakiem i nie wystepuje dwukrotnie po sobie.
# 
# Nazwa domenowa sklada sie jedynie z:
# a) Malych (a-z) i wielkich (A-Z) liter.
# b) Cyfr (0-9).
# c) Kropki . oraz myslnika - pod warunkiem, ze nie sa pierwszym badz ostatnim znakiem i nie wystepuja dwukrotnie po sobie.

poprawny_identyfikator() {
    # Funkcja sprawdza, czy podany identyfikator jest poprawny.
    local identyfikator="$1"
    
    if [[ "${identyfikator:0:1}" == "." ]] || [[ "${identyfikator: -1}" == "." ]]; then
        echo "false"
        return
    fi

    if [[ "${identyfikator}" =~ [.]{2,} ]]; then
        echo "false"
        return
    fi

    if [[ "${identyfikator}" =~ ^[-a-zA-Z0-9!\#$%\&\'*+=?^_\`{|}~\\.\\\/]+$ ]]; then        echo "true"
    else
        echo "false"
    fi

}

poprawna_nazwa_domenowa() {
    # Funkcja sprawdza, czy podana nazwa domenowa jest poprawna.

    local nazwa_domenowa="$1"

    if [[ "${nazwa_domenowa:0:1}" == "." ]] || [[ "${nazwa_domenowa: -1}" == "." ]] || [[ "${nazwa_domenowa:0:1}" == "-" ]] || [[ "${nazwa_domenowa: -1}" == "-" ]]; then
        echo "false"
        return
    fi

    # check if there are any adjacent dots


    if [[ "${nazwa_domenowa}" =~ [.]{2,} ]] || [[ "${nazwa_domenowa}" =~ [-]{2,} ]]; then
        echo "false"
        return
    fi

        local wystapienia_kropki=`echo "${nazwa_domenowa}" | grep -o '\\.' | wc -l`

    if [ $wystapienia_kropki -lt 1 ]; then
        echo "false"
        return
    fi

    if [[ "$nazwa_domenowa" =~ ^[a-zA-Z0-9.-]+$ ]]; then
        echo "true"
    else
        echo "false"
    fi

}

czy_email_poprawny() {
    # Funkcja sprawdza, czy podany adres email jest poprawny.

    local email="$1"

    # count how many times '@' appears in the email
    local count=$(echo "$email" | grep -o "@" | wc -l)
    if [ $count -ne 1 ]; then
        echo "false"
        return
    fi

    local identyfikator="$(echo "$email" | cut -d '@' -f 1)"
    local nazwa_domenowa="$(echo "$email" | cut -d '@' -f 2)"

    if [[ "$(poprawny_identyfikator "$identyfikator")" == "true" ]] && [[ "$(poprawna_nazwa_domenowa "$nazwa_domenowa")" == "true" ]]; then
        echo "true"
    else
        echo "false"
    fi

}


test_czy_email_poprawny_pozytywne() {
    assertTrue $(czy_email_poprawny "email@example.com") $LINENO
    assertTrue $(czy_email_poprawny "firstname.lastname@example.com") $LINENO
    assertTrue $(czy_email_poprawny "email@subdomain.example.com") $LINENO
    assertTrue $(czy_email_poprawny "firstname+lastname@example.com") $LINENO
    assertTrue $(czy_email_poprawny "email@123.123.123.123") $LINENO
    assertTrue $(czy_email_poprawny "1234567890@example.com") $LINENO
    assertTrue $(czy_email_poprawny "email@example-one.com") $LINENO
    assertTrue $(czy_email_poprawny "_______@example.com") $LINENO
    assertTrue $(czy_email_poprawny "email@example.name") $LINENO
    assertTrue $(czy_email_poprawny "email@example.museum") $LINENO
    assertTrue $(czy_email_poprawny "email@example.co.jp") $LINENO
    assertTrue $(czy_email_poprawny "firstname-lastname@example.com") $LINENO
}

test_czy_email_poprawny_negatywne() {

    assertFalse $(czy_email_poprawny "plainaddress") $LINENO
    assertFalse $(czy_email_poprawny "#@%^%#$@#$@#.com") $LINENO
    assertFalse $(czy_email_poprawny "@example.com") $LINENO
    assertFalse $(czy_email_poprawny "Joe Smith <email@example.com") $LINENO	
    assertFalse $(czy_email_poprawny "email.example.com") $LINENO
    assertFalse $(czy_email_poprawny ".email@example.com") $LINENO
    assertFalse $(czy_email_poprawny "email..email@example.com") $LINENO
    assertFalse $(czy_email_poprawny "email@example.com (Joe Smith)") $LINENO
    assertFalse $(czy_email_poprawny "email@example") $LINENO
    assertFalse $(czy_email_poprawny "email@-example.com") $LINENO
    assertFalse $(czy_email_poprawny "email@example..com") $LINENO
    assertFalse $(czy_email_poprawny "Abc..123@example.com") $LINENO

}

main() {
    test_czy_email_poprawny_pozytywne
    test_czy_email_poprawny_negatywne
}


main "$@"


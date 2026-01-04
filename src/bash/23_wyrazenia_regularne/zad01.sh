# ZAD-01 — Sprawdź poprawność adresu e-mail
#
# **Poziom:** ★★☆
# **Tagi:** `regex`, `string`, `walidacja`
#
# ### Treść
#
# Otrzymujesz napis reprezentujący adres e-mail. Sprawdź, czy jest poprawny zgodnie z regułami:
#
# * Adres e-mail składa się z identyfikatora użytkownika, znaku `@` oraz nazwy domeny.
# * **Identyfikator użytkownika** może zawierać wyłącznie:
#
#   * litery `a–z`, `A–Z`,
#   * cyfry `0–9`,
#   * znaki specjalne: `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`,
#   * kropki `.`, ale:
#
#     * nie może być pierwszym ani ostatnim znakiem,
#     * nie może wystąpić dwukrotnie po sobie.
# * **Nazwa domeny** może zawierać wyłącznie:
#
#   * litery `a–z`, `A–Z`,
#   * cyfry `0–9`,
#   * kropki `.` oraz myślniki `-`, ale:
#
#     * nie mogą być pierwszym ani ostatnim znakiem,
#     * nie mogą wystąpić dwukrotnie po sobie.
#
# ### Wejście
#
# Jedna linia:
#
# * `email`
#
# ### Wyjście
#
# Jedna linia:
#
# * `Prawda` — jeśli e-mail jest poprawny
# * `Fałsz` — w przeciwnym razie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# adam@gmail.com
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```
source ../assert.sh

# Sprawdza, czy identyfikator użytkownika w adresie email jest poprawny.
# Złożoność czasowa: O(n), gdzie n to długość identyfikatora
# Złożoność pamięciowa: O(1)
poprawny_identyfikator() {
    local identyfikator="$1"

    if [[ "${identyfikator:0:1}" == "." ]] || [[ "${identyfikator: -1}" == "." ]]; then
        echo "false"
        return
    fi

    if [[ "${identyfikator}" =~ [.]{2,} ]]; then
        echo "false"
        return
    fi

    if [[ "${identyfikator}" =~ ^[-a-zA-Z0-9!\#$%\&\'*+=?^_\`{|}~\\.\\\/]+$ ]]; then
        echo "true"
    else
        echo "false"
    fi

}

# Sprawdza, czy nazwa domenowa w adresie email jest poprawna.
# Złożoność czasowa: O(n), gdzie n to długość nazwy domenowej
# Złożoność pamięciowa: O(1)
poprawna_nazwa_domenowa() {

    local nazwa_domenowa="$1"

    if [[ "${nazwa_domenowa:0:1}" == "." ]] || [[ "${nazwa_domenowa: -1}" == "." ]] || [[ "${nazwa_domenowa:0:1}" == "-" ]] || [[ "${nazwa_domenowa: -1}" == "-" ]]; then
        echo "false"
        return
    fi

    if [[ "${nazwa_domenowa}" =~ [.]{2,} ]] || [[ "${nazwa_domenowa}" =~ [-]{2,} ]]; then
        echo "false"
        return
    fi

    local wystapienia_kropki=$(echo "${nazwa_domenowa}" | grep -o '\.' | wc -l)

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

# Sprawdza, czy adres email jest poprawny zgodnie z regułami.
# Złożoność czasowa: O(n), gdzie n to długość adresu email
# Złożoność pamięciowa: O(n)
czy_email_poprawny() {

    local email="$1"

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

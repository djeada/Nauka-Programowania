# ZAD-02 — Sprawdź poprawność hasła
#
# **Poziom:** ★★☆
# **Tagi:** `regex`, `string`, `walidacja`
#
# ### Treść
#
# Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia wszystkie warunki:
#
# 1. Zawiera co najmniej jedną małą literę `[a–z]`.
# 2. Zawiera co najmniej jedną wielką literę `[A–Z]`.
# 3. Zawiera co najmniej jedną cyfrę `[0–9]`.
# 4. Zawiera co najmniej jeden znak specjalny spośród:
#    `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
# 5. Ma długość co najmniej 8 znaków.
# 6. Ma długość nie większą niż 20 znaków.
#
# ### Wejście
#
# Jedna linia:
#
# * `haslo`
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
# abc1234
# ```
#
# **Wyjście:**
#
# ```
# Fałsz
# ```

source ../assert.sh

# Sprawdza, czy hasło spełnia wszystkie wymagane warunki.
# Złożoność czasowa: O(n), gdzie n to długość hasła
# Złożoność pamięciowa: O(1)
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

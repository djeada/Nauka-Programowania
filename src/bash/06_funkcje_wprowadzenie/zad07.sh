# ZAD-07 — Weryfikacja nazwy użytkownika i hasła
#
# **Poziom:** ★★☆
# **Tagi:** `funkcje`, `while`, `string`, `porównania`
#
# ### Treść
#
# Napisz dwie funkcje:
#
# 1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca je (np. jako parę).
# 2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje:
#    `Dane poprawne. Dostęp przyznany.`
#
# ### Wejście
#
# * `pobierz_dane()` wczytuje dwie linie:
#
#   1. login
#   2. hasło
# * `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na próbę.
#
# ### Wyjście
#
# Jedna linia (tylko raz, po poprawnym dopasowaniu):
#
# * `Dane poprawne. Dostęp przyznany.`
#
# ### Ograniczenia / gwarancje
#
# * W pewnym momencie użytkownik poda poprawne dane.
#
# ### Uwagi o formatowaniu
#
# * **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
# * Porównanie jest czułe na wielkość liter.
inicjalizacjaDanych() {
    echo "podaj nazwe oraz haslo do zapamietania"
    read nazwaTemp
    read hasloTemp
    eval "$1=$nazwaTemp $2=$hasloTemp"
}

czyDanePoprawne() {

    staraNazwa=$1
    stareHaslo=$2

    nowaNazwa=""
    noweHaslo=""

    while [[ $nowaNazwa != $staraNazwa ]] || [[ $noweHaslo != $stareHaslo ]]; do
        read nowaNazwa
        read noweHaslo
    done

    echo "Logowanie do systemu przebieglo pomyslnie"
}

main() {
    nazwa=""
    haslo=""
    inicjalizacjaDanych nazwa haslo
    czyDanePoprawne $nazwa $haslo
}

main "$@"

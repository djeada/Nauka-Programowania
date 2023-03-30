# Tytul: Klucz to imie, wartosc lista wypozyczonych ksiazek.
# Tresc: Zbuduj prosta baze danych dla biblioteki oparta o slownik, w ktorym kluczami sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek. Baza danych powinna umozliwiac:
# 1. Dodanie wypozyczonej ksiazki do danego czytelnika.
# 2. Zwrocenie wypozyczonej ksiazki przez czytelnika.
# 3. Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.

source ../assert.sh

posortuj_wzgledem_napisow() {

    local klucze=($(echo "${!slownik[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

    for klucz in "${klucze[@]}"; do
        echo "$klucz ${slownik[$klucz]};"
    done
}

posortuj_wzgledem_liczb() {

    for klucz in "${!slownik[@]}"; do
        echo "$klucz ${slownik[$klucz]};"
    done | sort -n -k2
}

test_posortuj_wzgledem_napisow() {
    local -A slownik=([a]=2 [c]=1 [b]=3)
    local wynik=($(posortuj_wzgledem_napisow))
    local oczekiwane=(a 2; b 3; c 1;)
    assertElementsEqual wynik oczekiwane $LINENO
}

test_posortuj_wzgledem_liczb() {
    local -A slownik=([a]=2 [c]=1 [b]=3)
    local wynik=($(posortuj_wzgledem_liczb))
    local oczekiwane=(c 1; a 2; b 3;)
    assertElementsEqual wynik oczekiwane $LINENO
}

main() {
    test_posortuj_wzgledem_napisow
    test_posortuj_wzgledem_liczb
}

main "$@"


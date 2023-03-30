# Tytul: Wczytaj i rozdziel informacje o pracowniku.
# Tresc: Otrzymasz rekord z bazy danych reprezentujacy dane pracownika. Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje sa rozdzielone srednikami. Zapisz je w osobnych zmiennych i wypisz je razem z odpowiednimi komunikatami.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu:
# "Jan; Kowalski; Warszawa; Programista; 1000;",
# powinna zostac zwrocona lista:
# ["Imie: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawod: Programista", "Zarobki: 1000"].

source ../assert.sh

liczby() {
    printf -v wynik '%s' "${lista[@]}"
    echo "$wynik"
}

test1() {
    local lista=(1 2 3 4)
    local wynik="1234"
    assertEqual "$(liczby)" "$wynik" $LINENO
}

test2() {
    local lista=()
    local wynik=""
    assertEqual "$(liczby)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"


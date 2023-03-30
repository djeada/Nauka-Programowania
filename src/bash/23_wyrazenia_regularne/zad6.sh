# Tytul: Cyfry w slowach.
# Tresc: Dostajesz napis reprezentujacy zdanie. Zapisz w liscie cyfry, ktore sa czescia slow. Cyfry oddzielone od liter spacja powinny zostac pominiete.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego", powinna zostac zwrocona lista: ["29", "37", "3891", "3"].

source ../assert.sh

wiersze_konczace_sie_napisem() {
    local tekst=$1
    local koniec=$2

    for wiersz in $tekst; do
        if [[ $wiersz == *$koniec ]]; then
            echo $wiersz
        fi
    done

    echo "$tekst" | grep -E ".*$koniec"
}

test_wiersze_konczace_sie_napisem() {
    local tekst="Folgujmy paniom nie sobie, ma rada;
    Milujmy wiernie nie jest w nich przysada.
    Godnosci trzeba nie za nic tu cnota,
    Milosci pragna nie pragna tu zlota."
    local koniec="da"
    local wynik=($(wiersze_konczace_sie_napisem "$tekst" "$koniec"))
    local oczekiwane=('Folgujmy paniom nie sobie, ma rada;' 'Milujmy wiernie nie jest w nich przysada.')

    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_wiersze_konczace_sie_napisem
}

main "$@"


# Tytul: Znalezienie indeksu najmniejszego elementu w posortowanej i przesunietej w prawo liscie.
# Tresc: Dla otrzymanej listy liczb calkowitych, znajdz indeks najmniejszego elementu. Lista jest posortowana rosnaco, ale zostala przesunieta w prawo o okreslona liczbe miejsc. Przykladowo dla przesuniecia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.
# Dane wejsciowe: Lista liczb calkowitych oraz liczba naturalna okreslajaca przesuniecie w prawo.
# Dane wyjsciowe: Liczba calkowita.
# Przyklad:
# Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrocona liczba: 2.

source ../assert.sh

usun_duplikaty() {
    local pom=()
    declare -A histo

    for liczba in "${lista[@]}"; do
        if [[ -z  ${histo["$liczba"]} ]]; then
            pom+=("$liczba")
            histo["$liczba"]=1
        fi
    done
    lista=("${pom[@]}")
    unset histo
    unset pom
}

test1() {
    local lista=(3 5 3 3 2)
    local wynik=(3 5 2)
    usun_duplikaty
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
}

main "$@"


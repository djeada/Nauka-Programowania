# Tytul: Lista pracownikow z najwiekszymi zyskami.
# Tresc: Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwisko pracownika, drugim zysk z transakcji, jaka dany pracownik przeprowadzil. Znajdz pracownika, ktory przyniosl firmie najwiecej zysku.
# Dane wejsciowe: Lista par napisow i liczb naturalnych.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanej listy:
# [["Barnaba Barabash", 120],
# ["Jon Snow", 100],
# ["Kira Summer", 300],
# ["Barnaba Barabash", 200],
# ["Bob Marley", 110]]
# zostanie zwrocony napis: “Barnaba Barabash”.

source ../assert.sh

zbuduj_slownik() {
    local -a lista_a=($1)
    local -a lista_b=($2)
    local -A slownik=()
    local n=${#lista_a[@]}

    for ((i=0; i<n; i++)); do
        slownik[${lista_a[i]}]=${lista_b[i]}
    done

    for k in "${!slownik[@]}"; do
        echo "$k: ${slownik[$k]};"
    done
}

test_zbuduj_slownik() {
    local wynik=($(zbuduj_slownik "1 2 3 4 5" "a b c d e"))
    local oczekiwane=(
        "1: a;"
        "2: b;"
        "3: c;"
        "4: d;"
        "5: e;"
    )
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_zbuduj_slownik
}

main "$@"


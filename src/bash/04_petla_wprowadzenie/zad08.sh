# Tytul: Liczba kur i owiec na farmie.
# Tresc: Na farmie jest a glow i b nog. Znajdz liczbe kur i liczbe owiec.
# Dane wejsciowe: Dwie liczby naturalne.
# Dane wyjsciowe: Dwie liczby naturalne.
# Przyklad:
# Dla otrzymanych liczb 40 i 100, powinny zostac wypisane liczby 30 i 10.

main() {

    echo "Podaj liczby a glow i b nog: "
    read a
    read b

    for (( i=1; i<=$a; i++ )); do
        owieczki=$(($a - $i))

        if [[ $((2*$i + 4*$owieczki)) -eq $b ]]; then
            echo "Na farmie mamy $i kur i $owieczki owieczek"
            break
        fi

    done

}

main "$@"


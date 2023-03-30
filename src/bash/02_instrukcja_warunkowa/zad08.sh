# Tytul: Warunek trojkata.
# Tresc: Dla trzech pobranych od uzytkownika dlugosci bokow sprawdz, czy mozna z nich zbudowac trojkat. Jednostki sa umowne.
# Dane wejsciowe: Trzy liczby naturalne oznaczajace dlugosci bokow trojkata.
# Dane wyjsciowe: Komunikat o mozliwosci lub niemozliwosci zbudowania trojkata.
# Przyklad:
# Dla pobranych liczb: 1, 2 oraz 3, powinna zostac wypisana informacja, ze nie mozna zbudowac trojkata z podanych bokow.

main() {

    echo "Podaj trzy dlugosci bokow: "

    read a
    read b
    read c

    if [[ $(($a + $b)) > $c ]] && [[ $(($a + $c)) > $b ]] && [[ $(($b + $c)) > $a ]]; then
        echo "Z podanych dlugosci bokow mozna zbudowac trojkat"

    else
        echo "Z podanych dlugosci bokow nie mozna zbudowac trojkata"
    fi
}

main "$@"


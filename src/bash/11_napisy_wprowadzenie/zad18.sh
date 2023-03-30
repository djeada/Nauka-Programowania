# Tytul: Znajdz najdluzsze/najkrotsze slowo w zdaniu.
# Tresc: Otrzymasz napis reprezentujacy zdanie. Znajdz:
# a) najdluzsze slowo w zdaniu,
# b) najkrotsze slowo w zdaniu.
# Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, zwroc to slowo sposrod nich, ktore wystepuje w zdaniu jako pierwsze. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe:
# a) Napis.
# b) Napis.
# Przyklad:
# a) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "Kaczka".
# b) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "lubi".

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    local wynik=""

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                local wynik="$wynik$(echo "$slowo" | rev) "
            fi
        done

        if [ ${#wynik} -gt 0 ]; then
            echo "${wynik::-1}"
        else
            echo ""
        fi
    }

    test1() {
        local napis="Cameron Diaz"
        local wynik="noremaC zaiD"
        assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
    }

    test2() {
        local napis=""
        local wynik=""
        assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"


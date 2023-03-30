# Tytul: Policz wystapienia znaku.
# Tresc: Dla podanego napisu i znaku, znajdz liczbe wystapien tego znaku w napisie.
# Dane wejsciowe: Napis oraz znak.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanego napisu: "klamra" oraz znaku 'a', powinno zostac zwrocone: 2.

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                echo "$slowo"
            fi
        done

    }

    najdluzsze() {
        local zdanie="$1"
        awk 'length > maks_dlugosc { maks_dlugosc = length; najdluzsze = $0 } END { print najdluzsze }' <<< $(wypisz_slowa "$zdanie")
    }

    najkrotsze() {
        local zdanie="$1"
        local n=${#zdanie}
        awk -v n=$n 'BEGIN { min_dlugosc = n } length < min_dlugosc { min_dlugosc = length; najkrotsze = $0 } END { print najkrotsze }' <<< $(wypisz_slowa "$zdanie")
    }

    test1() {
        local napis="Kaczka lubi wiosne."
        local wynik="Kaczka"
        assertEqual "$(najdluzsze "$napis")" "$wynik" $LINENO
    }

    test2() {
        local napis="Kaczka lubi wiosne."
        local wynik="lubi"
        assertEqual "$(najkrotsze "$napis")" "$wynik" $LINENO
        assertEqual "$(najkrotsze "$napis")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

